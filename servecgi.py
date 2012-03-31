#!/usr/bin/env python3

from http.server import HTTPServer, CGIHTTPRequestHandler

CGIHTTPRequestHandler.cgi_directories = ["/cgi"]
httpd = HTTPServer( (  "", 8000) , CGIHTTPRequestHandler).serve_forever()
'                 ( (addr,port ) , service              )                '

