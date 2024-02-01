import http.server
import socketserver
import webbrowser

PORT = 3123
URL = f"http://localhost:{PORT}/index.html"

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

print(f"Serving at port {PORT}")
webbrowser.open(URL)
httpd.serve_forever()

