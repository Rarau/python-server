
# code reduced from https://wiki.python.org/moin/BaseHttpServer
import json
import time
import BaseHTTPServer

# example of a python class
 
class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
  def do_GET(s):
    """Respond to a GET request."""
    s.send_response(200)
    s.send_header("Content-type", "text/html")
    s.end_headers()
    s.wfile.write("<html><head><title>Title goes here.</title></head>")
    s.wfile.write("<body><p>This is a test.</p>")
    s.wfile.write("<p>You accessed path: %s</p>" % s.path)
    s.wfile.write("<ul>")

    url_segments = s.path.split("/")
	
    for seg in url_segments:
		s.wfile.write("<li>%s</li>" % seg)

    data = url_segments[1].split("+")
    result = 0
    message = ""
    for op in data:
        result += int(op)
        message += "+" + str(op) + " "
        
    message += " = " + str(result)
    
    
    json_result = ["result", result]
    json_result["operands"] = data

    s.wfile.write("<p>%s</p>" % json.dumps(json_result))
	
    s.wfile.write("</ul></body></html>")


httpd = BaseHTTPServer.HTTPServer(("0.0.0.0", 8000), MyHandler)
httpd.serve_forever()

