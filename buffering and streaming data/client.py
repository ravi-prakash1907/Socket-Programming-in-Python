import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

HEADERSIZE = 10


while True:
    fullMsg = ''
    newMsg = True
    while True:
        msg = s.recv(16)
        if newMsg:
            print(f"New msg length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            newMsg = False

        fullMsg += msg.decode("utf-8")

        if len(fullMsg)-HEADERSIZE == msglen:
            print("Full msg recieved!!")
            print(fullMsg[HEADERSIZE:])
            newMsg = True
            fullMsg = ''

    print(fullMsg)
