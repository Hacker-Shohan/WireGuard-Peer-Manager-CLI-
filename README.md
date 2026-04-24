<h1>🚀 WireGuard Peer Manager (CLI)</h1>

<p>A simple yet powerful Python script to <b>manage WireGuard VPN peers</b> directly from the command line — no manual config editing needed.</p>

<p>This tool automates:</p>
<ul>
  <li>Peer creation</li>
  <li>IP allocation</li>
  <li>Config generation</li>
  <li>QR code output (for mobile)</li>
  <li>Live WireGuard updates (no restart)</li>
</ul>

<hr>

<h2>✨ Features</h2>
<ul>
  <li>➕ Add new peers instantly</li>
  <li>📱 Generate QR codes for mobile clients</li>
  <li>📋 List all configured peers</li>
  <li>🔗 Show real-time connection status</li>
  <li>❌ Remove peers cleanly</li>
  <li>⚡ No WireGuard restart required (live sync)</li>
  <li>🔐 Auto key + preshared key generation</li>
  <li>🧠 Smart IP allocation (10.0.0.x)</li>
</ul>

<hr>

<h2>📦 Requirements</h2>
<ul>
  <li>Linux server (Ubuntu/Debian recommended)</li>
  <li>Python 3</li>
  <li>WireGuard installed (wg, wg-quick)</li>
  <li>qrencode</li>
  <li>curl</li>
</ul>

<p><b>Install dependencies:</b></p>

<pre><code>sudo apt update
sudo apt install wireguard qrencode curl -y
</code></pre>

<hr>
<h2>⚙️ Setup</h2>

<ol>
  <li><b>Clone the repo:</b></li>
</ol>

<pre><code>git clone https://github.com/yourusername/wireguard-peer-manager.git
cd wireguard-peer-manager
</code></pre>

<ol start="2">
  <li><b>Make executable:</b></li>
</ol>

<pre><code>chmod +x wg-add-peer.py
</code></pre>

<ol start="3">
  <li><b>Run as root:</b></li>
</ol>

<pre><code>sudo python3 wg-add-peer.py
</code></pre>

<hr>

<h2>🖥️ Usage</h2>

<pre><code>1. Add new peer
2. List peers
3. Show QR for existing peer
4. Remove peer
</code></pre>

<hr>

<h3>➕ Add Peer</h3>
<ul>
  <li>Automatically generates keys</li>
  <li>Assigns IP</li>
  <li>Updates server config</li>
  <li>Syncs WireGuard live</li>
  <li>Outputs QR code for mobile apps</li>
</ul>

<hr>

<h3>📋 List Peers</h3>
<ul>
  <li>Shows all configured peers</li>
  <li>Displays live status:</li>
</ul>

<pre><code>wg show wg0
</code></pre>

<hr>

<h3>📱 Show QR</h3>
<ul>
  <li>Regenerate QR for any existing peer config</li>
</ul>

<hr>

<h3>❌ Remove Peer</h3>
<ul>
  <li>Removes peer from live WireGuard session</li>
  <li>Deletes from wg0.conf</li>
  <li>Deletes saved config file</li>
</ul>

<hr>

<h2>🔐 Security Notes</h2>
<ul>
  <li>Peer configs are stored with <b>600 permissions</b></li>
  <li>Uses preshared keys for extra encryption</li>
  <li>Requires root privileges</li>
</ul>

<hr>

<h2>⚠️ Important</h2>

<p><b>Generate server keys if missing:</b></p>

<pre><code>wg genkey | tee /etc/wireguard/server_private.key | wg pubkey > /etc/wireguard/server_public.key
</code></pre>

<ul>
  <li>Default subnet: 10.0.0.0/24</li>
  <li>Default port: 51820</li>
</ul>

<hr>

<h2>🧠 How It Works</h2>
<ul>
  <li>Parses wg0.conf to detect used IPs</li>
  <li>Assigns next available IP</li>
  <li>Appends peer config</li>
  <li>Applies changes using wg set + syncconf</li>
  <li>No downtime required</li>
</ul>

<hr>

<h2>🛠️ Future Improvements</h2>
<ul>
  <li>Web UI dashboard</li>
  <li>Peer bandwidth stats</li>
  <li>Expiry / time-limited peers</li>
  <li>Multi-subnet support</li>
  <li>Docker support</li>
</ul>

<hr>

<h2>🤝 Contributing</h2>
<p>Pull requests are welcome. For major changes, open an issue first.</p>

<hr>

<h2>📜 License</h2>
<p>MIT License</p>

<hr>

<h2>💬 Author</h2>
<p>Made by <b>Shohanur Rahman</b></p>
