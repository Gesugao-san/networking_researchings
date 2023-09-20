#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-


import http.server
import socketserver
import urllib.request

class MyProxy(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        url = self.path
        if url.startswith('/?info_hash=') or url.startswith('/?'):
            #url = 'http://tracker.gbitt.info/announce' + url
            url = 'http://tracker.openbittorrent.com/announce' + url
            self.path = url
        print(url)
        self.send_response(200)
        self.end_headers()
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
    httpd.shutdown()
    #httpd.socket.close()


# https://stackoverflow.com/a/71341150/8175291


