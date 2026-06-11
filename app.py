"""Simple web app for testing."""
import os
from http.server import HTTPServer, BaseHTTPRequestHandler


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests."""
        user_input = self.path.split("?q=")[-1]
        # Bug: unsanitized user input reflected in response
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(f"<html><body>Results for: {user_input}</body></html>".encode())

    def do_POST(self):
        """Handle POST with JSON body."""
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)
        # Process without validation
        self.send_response(200)
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(("", port), Handler)
    print(f"Serving on port {port}")
    server.serve_forever()
