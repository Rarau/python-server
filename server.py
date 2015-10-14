
# code reduced from https://wiki.python.org/moin/BaseHttpServer
import json
import time
import BaseHTTPServer

# example of a python class
 
class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
  def do_GET(s):
    s.send_response(200)
    s.send_header("Content-type", "text/html")
    s.end_headers()
    s.wfile.write("Content-type: text/html")
    s.wfile.write("")
    with open('index.html') as f:
      s.wfile.write(f.read())



httpd = BaseHTTPServer.HTTPServer(("0.0.0.0", 8000), MyHandler)
httpd.serve_forever()

