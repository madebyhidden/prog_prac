import socket

sock = socket.socket()
msg = ''
sock.connect(('localhost', 9091))

while msg != "exit":
    msg = input()
    if msg == "exit":
        break
    sock.send(msg.encode())
    data = sock.recv(1024)
    print(data.decode())

sock.close()