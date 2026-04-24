<h1>🚀 WireGuard Peer Manager</h1>

<p>Simple Python script to manage WireGuard peers easily.</p>

<p>No manual config editing. Just run and use.</p>

<hr>

<h2>📦 What is this?</h2>

<ul>
  <li>➕ Add new WireGuard peers</li>
  <li>📱 Generate QR codes (for mobile)</li>
  <li>📋 List all peers</li>
  <li>❌ Remove peers</li>
</ul>

<p>Everything is automatic:</p>
<ul>
  <li>Keys are generated</li>
  <li>IP is assigned</li>
  <li>Config is updated</li>
  <li>WireGuard reloads live</li>
</ul>

<hr>

<h2>⚙️ Requirements</h2>

<ul>
  <li>Linux (Ubuntu/Debian)</li>
  <li>Python 3</li>
  <li>WireGuard</li>
  <li>qrencode</li>
  <li>curl</li>
</ul>

<p><b>Install dependencies:</b></p>

<pre><code>sudo apt update
sudo apt install wireguard qrencode curl -y
</code></pre>

<hr>

<h2>📥 Install</h2>

<pre><code>git clone https://github.com/yourusername/wireguard-peer-manager.git
cd wireguard-peer-manager
</code></pre>

<hr>

<h2>▶️ Usage</h2>

<p>Run the script as root:</p>

<pre><code>sudo python3 app.py
</code></pre>

<p>You will see:</p>

<pre><code>1. Add new peer
2. List peers
3. Show QR for existing peer
4. Remove peer
</code></pre>

<hr>

<h2>🧪 Example</h2>

<h3>➕ Add a peer</h3>
<ul>
  <li>Choose <b>1</b></li>
  <li>Enter name (example: phone)</li>
</ul>

<p>Done ✅</p>

<hr>

<h3>📋 List peers</h3>
<p>Choose <b>2</b></p>

<hr>

<h3>📱 Show QR</h3>
<p>Choose <b>3</b> → enter peer name</p>

<hr>

<h3>❌ Remove peer</h3>
<p>Choose <b>4</b> → enter peer name</p>

<hr>

<h2>📁 Files</h2>

<ul>
  <li><b>Server config:</b> /etc/wireguard/wg0.conf</li>
  <li><b>Peer configs:</b> /etc/wireguard/peers/</li>
</ul>

<hr>

<h2>⚠️ Notes</h2>

<ul>
  <li>Run as root (sudo required)</li>
  <li>Default subnet: 10.0.0.x</li>
  <li>Default port: 51820</li>
</ul>

<hr>
