from http.server import BaseHTTPRequestHandler, HTTPServer


class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = "Testing testing 1 2 3"
        self.wfile.write(bytes(message, "utf8"))
        return

    def do_POST(self):


def run():
    print("1")


server_address = ('127.0.0.1', 8088)
httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
print("IP,Port: ", server_address)
httpd.serve_forever()
print("Server running")