from http.server import SimpleHTTPRequestHandler, HTTPServer
import urllib.request

class Proxy(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/data.csv":
            url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRbEmtPcluRdAkQRAlO8uaKvnTlBHBkN84fXf1YyVbK6kKopJfwPcZ_bkl8UhCz8KClvGVEkY1ady2a/pub?output=csv"
            self.send_response(200)
            self.send_header("Content-type", "text/csv")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            with urllib.request.urlopen(url) as f:
                self.wfile.write(f.read())
        else:
            super().do_GET()

if __name__ == "__main__":
    print("📡 Serwer działa na http://localhost:8000")
    HTTPServer(('localhost', 8000), Proxy).serve_forever()