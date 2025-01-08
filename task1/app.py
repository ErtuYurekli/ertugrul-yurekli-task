from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Merhaba Konzek")

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8000), MyHandler)
    print("Sunucu http://0.0.0.0:8000 adresinde başlatılıyor.")
    server.serve_forever()
