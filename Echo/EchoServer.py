import socket

sock = socket.socket()
sock.bind(('localhost', 9091))
sock.listen()
conn, addr = sock.accept()
print(addr)

msg = ''

while msg != "exit":
    data = conn.recv(1024)
    if not data:
        break
    msg = data.decode()
    conn.send(data)
    print(msg)

conn.close()