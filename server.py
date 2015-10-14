
# code reduced from https://wiki.python.org/moin/BaseHttpServer
import json
import time
import BaseHTTPServer

# example of a python class
 
class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
  def do_GET(s):
    print "Content-type: text/html"
    print
    with open('index.html') as f:
      print f.read()



httpd = BaseHTTPServer.HTTPServer(("0.0.0.0", 8000), MyHandler)
httpd.serve_forever()

