import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('eccouncil.org', 443))
print(s)
s.getpeername()
s.close()
s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

import socket
def check_availability(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, int(port)))
        s.close()
        return True
    except:
        return False
    
def get_input(prompt= ''):
    try:
        return raw_input(prompt)
    except NameError:
        return input(prompt)

host = get_input('Device Name or IP Address: ')
port = get_input('Port number: ')

reachable = check_availability(host, port)
if reachable:
    print("The host is reachable on the given port")
else:
    print("The host is NOT reachable on the given port")

