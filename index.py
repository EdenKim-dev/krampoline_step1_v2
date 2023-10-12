from http.server import SimpleHTTPRequestHandler, HTTPServer


class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write("Hello krampoline!".encode('utf-8'))


PORT = 3000

with HTTPServer(("", PORT), CustomHandler) as httpd:
    print(f"서버는 {PORT} 포트에서 실행 중입니다. 종료하려면 Ctrl+C를 누르세요.")
    httpd.serve_forever()
