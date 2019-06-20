#  i.e. sending/receiving data without termination the connection

import socket
import time

#using HEADER can resolve the problem of how long (in size) the message is sent/received

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientSocket, address = s.accept()
    print(f"Connection to {address} has been esteblished!")

    msg = "Welcome to the server!"
    msg = f'{len(msg):<{HEADERSIZE}}' + msg
    # <{HEADERSIZE}  ------------> '<' is for left allign.. can be also   '>' or '^'

    clientSocket.send(bytes(msg, "utf-8"))

    while True:
        time.sleep(3)
        msg = f"The time is! {time.time()}"
        msg = f'{len(msg):<{HEADERSIZE}}' + msg
        clientSocket.send(bytes(msg, "utf-8"))


#clientSocket.close()  ->  it's not needed i.e. connection ain't terminated
