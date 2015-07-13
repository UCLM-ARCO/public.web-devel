#!/usr/bin/python
# -*- coding: utf-8; mode: python -*-

import SimpleHTTPServer
from SocketServer import TCPServer
import urlparse


class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def hello(self):
        self.wfile.write('<html><body>Hello, world!!</body></html>')

    def bye(self):
        self.wfile.write('<html><body>bye!!!</body></html>')

    def do_GET(self):
        parts = urlparse.urlparse(self.path)

        if parts.path == '/hello':
            self.hello()
        elif parts.path == '/bye':
            self.bye()


PORT = 8000
TCPServer.allow_reuse_address = True
httpd = TCPServer(("", PORT), Handler)

print("Serving at port: %s" % PORT)
httpd.serve_forever()
