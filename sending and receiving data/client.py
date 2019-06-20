import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET refers to the address family ipv4. The SOCK_STREAM means connection oriented TCP protocol.
s.connect((socket.gethostname(), 1234))

def recieveComplete():
    msg = s.recv(1024)      #it's a buffer of 1024 bytes how many size of data we want to accept once
    print(msg.decode("utf-8"))

def recievePartially():
    while True:
        msg = s.recv(8)
        if len(msg) > 0:
            print(msg.decode("utf-8"))
        else:
            break

def joinShortMsg():
    fullMsg = ''
    while True:
        msg = s.recv(8)
        if len(msg) <= 0:
            break

        fullMsg += msg.decode("utf-8")

    print(fullMsg)

#recieveComplete()
#recievePartially()
joinShortMsg()

s.close()
