#  i.e. sending/reciving data without termination the connection

import socket
import time
import pickle


#using HEADER can resolve the problem of how long (i tsize) the

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientSocket, address = s.accept()
    print(f"Connection to {address} has been esteblished!")


    tempObj = {1: "Hey", 2: "There"}
    msg = pickle.dumps(tempObj)

    msg = bytes(f'{len(msg):<{HEADERSIZE}}', 'utf-8') + msg

    clientSocket.send(bytes(msg))



#clientSocket.close()  ->  it's not needed i.e. connection ain't terminated
