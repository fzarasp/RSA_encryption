import socket
import sys
import time
from codegenerator import Keys , Decoding , Encoding




host = '127.0.0.1'
port = 12345
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
s.settimeout(2)
closeConnection = False
key = Keys()
keypu = key['public']
keypr = key['private']
serverkeystr = s.recv(1024).decode()
sk = serverkeystr.split()
serverkey = (int(sk[0]), int(sk[1]))
s.send(bytes(str(keypu[0]) + ' ' + str(keypu[1]), 'UTF-8'))
while True:
    while True:
        msg = input("your message: ")
        if msg == 'listen':
            break

        s.send(bytes(Encoding(serverkey, msg), 'UTF-8'))
        if msg == 'end':
            closeConnection = True
            break
        if msg == 'getAllports' or msg == 'getAllGroups':
            data = s.recv(1024)
            data = data.decode()
            #print(data)
            data = Decoding(keypr , data)
            print(data)
    if closeConnection:
        break
    while True:
        try:
            time.sleep(1)
            try:
                data = s.recv(1024)
                data = data.decode()
                #print(data)
                data = Decoding(keypr , data)
                print(data)
            except socket.timeout:
                pass
        except KeyboardInterrupt:
            break


s.close()
