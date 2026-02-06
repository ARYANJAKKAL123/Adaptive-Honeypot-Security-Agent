from analyzer import analyze_path
from logger import log_event
print("SERVER FILE STARTED")

from http.server import BaseHTTPRequestHandler, HTTPServer

class HoneypotServer(BaseHTTPRequestHandler):

    def do_GET(self):
        ip = self.client_address[0]
        path = self.path

        print("IP:", ip)
        print("Requested Path:", path) 
        print("---------------------")
        
        result = analyze_path(path)
    
    
        reason = str(result[0])
        score = str(result[1])
        final_reason = reason + " |score: " + score
        log_event( ip , path , final_reason)
      
        

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Living Honeypot Active")

server = HTTPServer(("localhost", 8000), HoneypotServer)

print("Honeypot running on http://localhost:8000")

server.serve_forever()
