import socket

s = socket.socket()
s.bind(('localhost', 8000))
s.listen(5)

print("Server waiting for client...")
c, addr = s.accept()

size = int(input("Enter number of frames to send: "))
l = list(range(size))

ws = int(input("Enter Window Size: "))

st = 0
i = 0

while i < len(l):
    st = i + ws

    print("Sending frames:", l[i:st])
    c.send(str(l[i:st]).encode())

    ack = c.recv(1024).decode()

    if ack:
        print(ack)
        i += ws
    else:
        break

c.close()
s.close()