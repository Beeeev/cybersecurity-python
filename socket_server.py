import socket
import sys
server = '192.168.1.18'
port = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, int(port)))
except socket.error as error:
    print('Binding failed!')
    sys.exit()
s.listen(1)
print("Server Started")

connection, address = s.accept()
ip, port = str(address[0]), str(address[1])

while True:
    data = connection.recv(1024)
    print('Incoming message from:' + ip + ':' + port)
    print(data.decode())
    if str(data.decode()) == 'close':
        break
