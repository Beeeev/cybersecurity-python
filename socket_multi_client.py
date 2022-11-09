import socket
import argparse
parser = argparse.ArgumentParser(description = "This is the client application")
parser.add_argument('--host', metavar = 'host', type = str, nargs = '?', default = socket.gethostname())
parser.add_argument('--port', metavar = 'port', type = str, nargs = '?', default = 9999)
args = parser.parse_args()
print(f'Attempting to connect to the server: {args.host} on port {args.port}')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((args.host, args.port))
    except Exception as e:
        print(f"Can't connect to the server because {e}")
        raise SystemExit
    while True:
        msg = input("Our message: ")
        s.sendall(msg.encode('utf-8'))
        if msg == 'close':
            print("Disconnecting...")
            break
        data = s.recv(1024)
        print(f"The server echoed back: {data.decode()}")
