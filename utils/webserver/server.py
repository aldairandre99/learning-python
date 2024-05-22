from http.server import BaseHTTPRequestHandler,HTTPServer

import time 

HOSTNAMA = "localhost"
PORT = 8080

class Server(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.end_headers()
    self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
    self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
    self.wfile.write(bytes("<body>", "utf-8"))
    self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
    self.wfile.write(bytes("</body></html>", "utf-8"))

    
if __name__ == "__main__":
  webServer = HTTPServer((HOSTNAMA,PORT),Server)
  print(f"Server started http://{HOSTNAMA}:{PORT}")
  
  try:
    webServer.serve_forever()
  except KeyboardInterrupt:
    pass

  webServer.server_close()
  print("Server stopped.")
