from http.server import SimpleHTTPRequestHandler, HTTPServer

# Define host and port for the web server
host = "localhost"
port = 8000

# Set up the HTTP server
class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<html><body><h1>Hello, World!</h1></body></html>")

# Create the server object
server = HTTPServer((host, port), MyHandler)

print(f"Starting server at http://{host}:{port}")
try:
    # Run the server
    server.serve_forever()
except KeyboardInterrupt:
    print("\nShutting down the server...")
    server.server_close()