import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientSocket, address = s.accept()
    print(f"Connection to {address} has been esteblished!")
    data = bytes("Welcome to the server!", "utf-8") #bytes("Welcome to the server!", 'utf-8')
    clientSocket.send(data)
    clientSocket.close()
