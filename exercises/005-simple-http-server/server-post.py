#!/usr/bin/python
# -*- coding: utf-8; mode: python -*-

import SimpleHTTPServer
from SocketServer import TCPServer
import httplib
import cgi


class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(httplib.OK)
        self.end_headers()
        self.wfile.write('<html><body>Hello, world!!</body></html>')

    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type']})

        for item in form.list:
            print("-- {}".format(item))

        self.root_redirect()

    def root_redirect(self):
        print("redirecting to root")
        self.send_response(301)
        self.send_header('Location', '/')
        self.end_headers()


PORT = 8000
TCPServer.allow_reuse_address = True
httpd = TCPServer(("", PORT), Handler)

print("Serving at port: %s" % PORT)
httpd.serve_forever()
