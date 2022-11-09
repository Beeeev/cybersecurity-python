import socket
import argparse
import threading

parser = argparse.ArgumentParser(description = "This is the server application") 
parser.add_argument('--host', metavar = 'host', type = str, nargs = '?', default = socket.gethostname())
parser.add_argument('--port', metavar = 'port', type = str, nargs = '?', default = 9999)
args = parser.parse_args()

print(f"Starting server on IP: {args.host} on port {args.port}")

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
    s.bind((args.host, args.port))
    s.listen(5)
except Exception as e:
    print(f"Can't bind because of {e}")
    raise SystemExit

def new_client(client, connection):
    ip = connection[0]
    port = connection[1]
    print(f"This is a new client from {ip} on port {port}")
    while True:
        msg = client.recv(1024)
        if msg.decode() == 'close':
            break
        print(f"Incoming message from {ip}:{port} > {msg.decode()}")
        reply = f"You said: {msg.decode()}"
        client.sendall(reply.encode('utf-8'))
        print(f"The client from address {ip}:{port} has disconnected")
        client.close()


while True:
    try:
        client_ip, client_addr = s.accept()
        print(client_ip, client_addr)
        threading._start_new_thread(new_client, (client_ip, client_addr))
    except KeyboardInterrupt:
        print("Abortion of the server requested")
        break
    except Exception as e:
        print(f"Something went wrong: {e}")
