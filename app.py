#!/usr/bin/env python3
import subprocess
import os
import sys

WG_CONF = "/etc/wireguard/wg0.conf"
WG_PEERS_DIR = "/etc/wireguard/peers"

def run(cmd):
    return subprocess.check_output(cmd, shell=True).decode().strip()

def get_next_ip():
    """Find next available IP in 10.0.0.x range"""
    used = []
    if os.path.exists(WG_CONF):
        with open(WG_CONF) as f:
            for line in f:
                if "AllowedIPs = 10.0.0." in line:
                    ip = line.strip().split("10.0.0.")[1].split("/")[0]
                    used.append(int(ip))
    for i in range(2, 255):
        if i not in used:
            return f"10.0.0.{i}"
    print("No available IPs!")
    sys.exit(1)

def get_server_pubkey():
    key_file = "/etc/wireguard/server_public.key"
    if not os.path.exists(key_file):
        print("❌ Server public key not found at /etc/wireguard/server_public.key")
        print("Run this once:")
        print("wg genkey | tee /etc/wireguard/server_private.key | wg pubkey > /etc/wireguard/server_public.key")
        return None
    with open(key_file) as f:
        return f.read().strip()

def get_server_ip():
    try:
        return run("curl -4 -s ifconfig.me")
    except:
        return input("Could not detect server IP. Enter manually: ").strip()

def add_peer(name):
    os.makedirs(WG_PEERS_DIR, exist_ok=True)

    server_pubkey = get_server_pubkey()
    if not server_pubkey:
        return

    # Generate peer keys
    private_key = run("wg genkey")
    public_key = run(f"echo '{private_key}' | wg pubkey")
    preshared_key = run("wg genpsk")

    peer_ip = get_next_ip()
    server_ip = get_server_ip()

    # Read server listen port
    listen_port = "51820"
    if os.path.exists(WG_CONF):
        with open(WG_CONF) as f:
            for line in f:
                if "ListenPort" in line:
                    listen_port = line.split("=")[1].strip()

    # Build client config
    client_conf = f"""[Interface]
PrivateKey = {private_key}
Address = {peer_ip}/32
DNS = 1.1.1.1

[Peer]
PublicKey = {server_pubkey}
PresharedKey = {preshared_key}
Endpoint = {server_ip}:{listen_port}
AllowedIPs = 0.0.0.0/0
PersistentKeepalive = 25
"""

    # Save client config
    peer_file = f"{WG_PEERS_DIR}/{name}.conf"
    with open(peer_file, "w") as f:
        f.write(client_conf)
    os.chmod(peer_file, 0o600)

    # Append peer to server config
    server_peer = f"""
# Peer: {name}
[Peer]
PublicKey = {public_key}
PresharedKey = {preshared_key}
AllowedIPs = {peer_ip}/32
"""
    with open(WG_CONF, "a") as f:
        f.write(server_peer)

    # Reload WireGuard live
    os.system(f"wg set wg0 peer {public_key} preshared-key <(echo '{preshared_key}') allowed-ips {peer_ip}/32 2>/dev/null")
    os.system(f"wg syncconf wg0 <(wg-quick strip /etc/wireguard/wg0.conf) 2>/dev/null")

    print(f"\n✅ Peer '{name}' added — IP: {peer_ip}")
    print("\n📱 Scan this QR code:\n")
    os.system(f"qrencode -t ansiutf8 < {peer_file}")
    print(f"\n💾 Config saved: {peer_file}")

def list_peers():
    print("\n📋 Configured peers:\n")
    if not os.path.exists(WG_CONF):
        print("No wg0.conf found.")
        return

    with open(WG_CONF) as f:
        content = f.read()

    peers = [line.split("Peer:")[1].strip() for line in content.splitlines() if "# Peer:" in line]

    if not peers:
        print("No peers configured yet.")
    else:
        for i, p in enumerate(peers, 1):
            print(f"{i}. {p}")

    print("\n🔗 Live status:\n")
    os.system("wg show wg0")

def remove_peer(name):
    peer_file = f"{WG_PEERS_DIR}/{name}.conf"
    if not os.path.exists(peer_file):
        print(f"Peer '{name}' not found.")
        return

    # Get public key
    pubkey = None
    with open(peer_file) as f:
        for line in f:
            if "PrivateKey" in line:
                privkey = line.split("=", 1)[1].strip()
                pubkey = run(f"echo '{privkey}' | wg pubkey")

    if pubkey:
        os.system(f"wg set wg0 peer {pubkey} remove")

    # Remove from config
    if os.path.exists(WG_CONF):
        with open(WG_CONF) as f:
            lines = f.readlines()

        new_lines = []
        skip = False

        for line in lines:
            if f"# Peer: {name}" in line:
                skip = True
                continue
            if skip and line.startswith("# Peer:"):
                skip = False
            if not skip:
                new_lines.append(line)

        with open(WG_CONF, "w") as f:
            f.writelines(new_lines)

    os.remove(peer_file)
    print(f"✅ Peer '{name}' removed.")

def show_qr(name):
    peer_file = f"{WG_PEERS_DIR}/{name}.conf"
    if not os.path.exists(peer_file):
        print(f"Peer '{name}' not found.")
        return

    print(f"\n📱 QR code for '{name}':\n")
    os.system(f"qrencode -t ansiutf8 < {peer_file}")

def main():
    if os.geteuid() != 0:
        print("❌ Run as root: sudo python3 app.py")
        sys.exit(1)

    while True:
        os.system("clear")
        print("━" * 40)
        print("   WireGuard Peer Manager")
        print("━" * 40)
        print("  1. Add new peer")
        print("  2. List peers")
        print("  3. Show QR for existing peer")
        print("  4. Remove peer")
        print("  5. Exit")
        print("━" * 40)

        choice = input("\nChoice [1-5]: ").strip()

        if choice == "1":
            name = input("Peer name (e.g. phone, laptop): ").strip()
            if name:
                add_peer(name)
            else:
                print("Name cannot be empty.")

        elif choice == "2":
            list_peers()

        elif choice == "3":
            name = input("Peer name: ").strip()
            show_qr(name)

        elif choice == "4":
            name = input("Peer name to remove: ").strip()
            remove_peer(name)

        elif choice == "5":
            print("👋 Exiting...")
            break

        else:
            print("Invalid choice.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
