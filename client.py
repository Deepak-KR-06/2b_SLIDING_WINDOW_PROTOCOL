import socket

s = socket.socket()
s.connect(('localhost', 8000))

while True:
    data = s.recv(1024).decode()

    if data:
        print("Received frames:", data)

        s.send("ACK: Frames received".encode())
    else:
        break

s.close()