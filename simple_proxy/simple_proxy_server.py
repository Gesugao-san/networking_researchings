#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# a truly minimal HTTP proxy

import http.server
import socketserver
import urllib.request
import webbrowser

PORT = 1234

BaseHandler = http.server.SimpleHTTPRequestHandler

class ProxyServerHandler(BaseHandler):
    #def do_HEAD(self):
    def do_GET(self):
        self.copyfile(urllib.request.urlopen(self.path), self.wfile)
    #def do_POST(self):
    #    self.copyfile(urllib.request.urlopen(self.path), self.wfile)

httpd = socketserver.ThreadingTCPServer(('', PORT), ProxyServerHandler)
print("Serving at port:", PORT)
#webbrowser.open('http://localhost:' + str(PORT))
httpd.serve_forever()


# https://stackoverflow.com/a/4412630/8175291
# http://web.archive.org/web/20200730224052/http://effbot.org/librarybook/simplehttpserver.htm
# https://stackoverflow.com/a/54966412/8175291
# https://gist.github.com/ayanamist/1391007


