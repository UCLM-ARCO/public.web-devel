#!/usr/bin/python
# -*- coding: utf-8; mode: python -*-

import SimpleHTTPServer
from SocketServer import TCPServer
import httplib


class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(httplib.OK)
        self.end_headers()
        self.wfile.write('<html><body>Hello, <b>world</b>!!</body></html>')


PORT = 8000
TCPServer.allow_reuse_address = True
httpd = TCPServer(("", PORT), Handler)

print("Serving at port: %s" % PORT)
httpd.serve_forever()
