import http.server
import socketserver
import signal

port = 8080
signal.signal(signal.SIGINT, signal.SIG_DFL)
Handler = http.server.SimpleHTTPRequestHandler

def server_init():
    http_daemon = socketserver.TCPServer(("", port), Handler)
    print("HTTP Server is now listening on port: ", port)
    http_daemon.serve_forever()
 
server_init()
