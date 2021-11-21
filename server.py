import socket, threading
from codegenerator import Keys , Decoding , Encoding


k = Keys()
kpu = k['public']
kpri = k['private']

class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        self.clientAddress = clientAddress
        self.clientkey = ''
        print ("New connection added: ", clientAddress)

    def run(self):

        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            #print(msg)
            msg = Decoding(kpri , msg)
            msg = msg.split()
            if len(msg) > 0:
                if msg[0] == 'getAllports':
                    strToSend = ''
                    for index in range(socketThreads.__len__()):
                        if socketThreads[index].clientAddress[1] != self.clientAddress[1]:
                            strToSend += str(socketThreads[index].clientAddress[1]) + ', '
                    if strToSend == '':
                        strToSend = 'no other port'
                    self.csocket.send(bytes(Encoding(self.clientkey ,strToSend), 'UTF-8'))
                elif msg[0] == 'getAllGroups':
                    strToSend = ''
                    for key in groups.keys():
                        strToSend += key + ', '
                    if strToSend == '':
                        strToSend = 'no group'
                    self.csocket.send(bytes(Encoding(self.clientkey ,strToSend), 'UTF-8'))
                elif msg[0] == 'create' and msg[1] == 'group':
                    groups[msg[2]] = []
                    self.addToGroup(msg[2], self.clientAddress[1])
                elif msg[0] == 'join':
                    self.addToGroup(msg[1], self.clientAddress[1])
                elif msg[0] == 'add':
                    self.addToGroup(msg[3], int(msg[1]))
                elif msg[0] == 'leave' and msg[1] == 'group':
                    self.leaveGroup(msg[2])
                elif msg[0] == 'end':
                    for key in list(groups):
                        self.leaveGroup(key)
                    for index in range(socketThreads.__len__()):
                        if socketThreads[index].clientAddress[1] == self.clientAddress[1]:
                            socketThreads.pop(index)
                            break
                    self.csocket.close()
                    self._running = False
                    break
                elif msg[0] == 'send' and msg[1] == 'message' and msg[3] != 'group':
                    strToSend = ' '.join(msg[4:])
                    strToSend = 'message from ' + str(self.clientAddress[1]) + ': ' + strToSend
                    for index in range(socketThreads.__len__()):
                        if int(socketThreads[index].clientAddress[1]) == int(msg[3]):
                            socketThreads[index].csocket.send(bytes(Encoding(self.clientkey ,strToSend), 'UTF-8'))
                            break
                elif msg[0] == 'send' and msg[1] == 'message' and msg[3] == 'group':
                    groupName = msg[4]
                    strToSend = ' '.join(msg[5:])
                    strToSend = 'message from ' + str(self.clientAddress[1]) + ' in ' + groupName + ': ' + strToSend
                    if groupName in groups:
                        for index in range(groups[groupName].__len__()):
                            groups[groupName][index].csocket.send(bytes(Encoding(self.clientkey ,strToSend), 'UTF-8'))

        print('connection closed, ' + str(self.clientAddress[1]))

    def addToGroup(self, groupName, port):
        for index in range(socketThreads.__len__()):
            if int(socketThreads[index].clientAddress[1]) == int(port):
                groups[groupName].append(socketThreads[index])
                break

    def leaveGroup(self, groupName):
        if groupName in groups:
            for index in range(groups[groupName].__len__()):
                if groups[groupName][index].clientAddress[1] == self.clientAddress[1]:
                    groups[groupName].pop(index)
                    break
            if groups[groupName].__len__() == 0:
                groups.pop(groupName, None)


def startServer():
    LOCALHOST = "127.0.0.1"
    PORT = 12345
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((LOCALHOST, PORT))
    print("Server started")
    print("Waiting for client request..")
    server.listen(5)
    while True:
        server.listen(1)
        clientsock, clientAddress = server.accept()
        newthread = ClientThread(clientAddress, clientsock)
        newthread.csocket.send(bytes(str(kpu[0]) + ' ' + str(kpu[1]), 'UTF-8'))
        c = newthread.csocket.recv(1024).decode()
        ck = c.split()
        newthread.clientkey = (int(ck[0]), int(ck[1]))
        socketThreads.append(newthread)
        newthread.start()


#--------------------------------------
#main
socketThreads = []
groups = {}
startServer()
