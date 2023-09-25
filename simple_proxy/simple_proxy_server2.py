#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-


import http.server
import socketserver
import urllib.request

class MyProxy(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        url = self.path
        bt_client_detected = False
        if url.startswith('/?info_hash=') or url.startswith('/?'):
            print('BitTorent client request detected, replacing URL.')
            bt_client_detected = True
            params = url
            #url = 'http://tracker.gbitt.info/announce' + params
            #url = 'http://tracker.openbittorrent.com/announce' + params
            url = 'http://tracker.files.fm:6969/announce' + params
            #self.path = url
        print('url:', url)
        #print('self:', str(self))
        self.send_response(200)
        self.end_headers()  # ConnectionAbortedError: [WinError 10053]
        if bt_client_detected:
            answer = urllib.request.urlopen('http://tracker.files.fm:6969/announce' + params)
            print('data:', answer.getheaders())
            print('data:', answer.info())
            #self.copyfile(urllib.request.urlopen('http://tracker.openbittorrent.com/announce' + params), self.wfile)
            self.copyfile(answer, self.wfile)
            #self.copyfile(urllib.request.urlopen('http://tracker.gbitt.info/announce' + params), self.wfile)
            self.copyfile(urllib.request.urlopen(url), self.wfile)
        else:
            self.copyfile(urllib.request.urlopen(url), self.wfile)

    def do_POST(self):
        url = self.path

        # - post data -
        content_length = int(self.headers.get('Content-Length', 0)) # <--- size of data
        if content_length:
            content = self.rfile.read(content_length)               # <--- data itself
        else:
            content = None

        req = urllib.request.Request(url, method="POST", data=content)
        output = urllib.request.urlopen(req)

        # ---

        self.send_response(200)
        self.end_headers()
        self.copyfile(output, self.wfile)

# --- main ---

PORT = 1234

httpd = None

try:
    socketserver.TCPServer.allow_reuse_address = True   # solution for `OSError: [Errno 98] Address already in use`
    httpd = socketserver.TCPServer(('', PORT), MyProxy)
    print(f"Proxy at: http://localhost:{PORT}")
    httpd.serve_forever()
except KeyboardInterrupt:
    print("Pressed Ctrl+C")
#finally:
if httpd:
    if httpd.socket:
        httpd.socket.close()
    httpd.shutdown()


# https://stackoverflow.com/a/71341150/8175291


