#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-


# a truly minimal HTTP proxy

import http.server
import socketserver
import urllib.request
import webbrowser

# netstat -ano | findstr :1234
PORT = 1234
server_address = ('', PORT)

BaseHandler = http.server.SimpleHTTPRequestHandler

class ProxyServerHandler(BaseHandler):
    #def _set_response(self):
        #self.send_response(200)
        #self.send_header('Content-type', 'text/html;')# charset=iso-8859-1')
        #self.send_header('encoding', 'iso-8859-1')
        #self.end_headers()


    #def do_HEAD(self):


    def do_GET(self):
        # self.wfile.write(bytes("It Works!", "utf-8"))
        print("\n= GET request =\nPath: \"%s\"\nHeaders:\n\"%s\"\n", str(self.path) + '', str(self.headers) + '')
        #self._set_response()
        #self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))
        self.copyfile(urllib.request.urlopen(self.path), self.wfile)



    #def do_POST(self):
    #    self.copyfile(urllib.request.urlopen(self.path), self.wfile)
    def do_POST2(self):
        # read the content-length header
        content_length = int(self.headers.get("Content-Length"))
        # read that many bytes from the body of the request
        body = self.rfile.read(content_length)

        self.send_response(200)
        self.end_headers()
        # echo the body in the response
        self.wfile.write(body)


    def do_POST(self):
        # read the content-length header
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        # read that many bytes from the body of the request

        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        #print("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
        #        str(self.path), str(self.headers), post_data.decode('utf-8'))
        print("\n= POST request =\nPath: \"%s\"\nHeaders:\n\"%s\"\nBody:\n(unable to render sorry)\n",
                str(self.path) + '', str(self.headers) + '')
        # UnicodeDecodeError: 'iso-8859-1' codec can't decode byte 0xbb in position 11: invalid start byte

        #self._set_response()
        #self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))
        self.wfile.write(post_data)



httpd = socketserver.ThreadingTCPServer(server_address, ProxyServerHandler)
#webbrowser.open('http://localhost:' + str(PORT))
print("Serving at port:", PORT)

print('Starting httpd...\n===')
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
httpd.server_close()
print('\n===\nStopping httpd...')



### illness history :/
# https://stackoverflow.com/a/4412630/8175291
# http://web.archive.org/web/20200730224052/http://effbot.org/librarybook/simplehttpserver.htm
# https://stackoverflow.com/a/54966412/8175291
# https://gist.github.com/ayanamist/1391007
# https://github.com/MollardMichael/python-reverse-proxy
# https://gist.github.com/mdonkers/63e115cc0c79b4f6b8b3a6b797e485c7
# https://stackoverflow.com/a/5552623/8175291
# https://stackoverflow.com/q/37612100/8175291
# https://stackoverflow.com/a/23596784/8175291
# https://stackoverflow.com/q/26663235/8175291
# https://gist.github.com/phrawzty/62540f146ee5e74ea1ab
# https://parsiya.net/blog/2020-11-15-customizing-pythons-simplehttpserver/
# https://spin.atomicobject.com/2022/07/18/python-http-proxy-server/
# https://stackoverflow.com/a/71341150/8175291


# https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection.request
# #  ---   If body is a string, it is encoded as ISO-8859-1
