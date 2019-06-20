import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

HEADERSIZE = 10


while True:
    fullMsg = b''
    newMsg = True
    while True:
        msg = s.recv(16)      #it's a buffer of 1024bytes how many size of data we want to accept once
        if newMsg:
            print(f"New msg length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            newMsg = False

        fullMsg += msg  #.decode("utf-8")

        if len(fullMsg)-HEADERSIZE == msglen:
            print("Full msg recieved!!")

            d = pickle.loads(fullMsg[HEADERSIZE:])
            print(d)
            
            print(fullMsg[HEADERSIZE:])
            newMsg = True
            fullMsg = b''

    print(fullMsg)
