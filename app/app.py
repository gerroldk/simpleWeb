#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json
from socketserver import ThreadingMixIn
import threading

print("Reading config")

try:
    with open("/config/config.txt") as f:
        config = f.read()
        print(config)

except Exception as e:
    print(e.__class__)
    raise e

hostName = "0.0.0.0"
serverPort = 5000


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/config":
            self.send_response(200)
            self.send_header("Content - type", "text / html")
            self.end_headers()
            content = open("/config/config.txt", 'rb').read()
            self.wfile.write(content)
        else:
            self.send_response(404)
        return


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""


if __name__ == "__main__":
    webServer = ThreadedHTTPServer((hostName, serverPort), Handler)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        passwebServer.server_close()
        print("Server stopped.")
