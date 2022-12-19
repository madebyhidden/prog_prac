import socket
import pickle

sock = socket.socket()
sock.bind(('127.0.0.1', 8080))

sock.listen(1)
conn, addr = sock.accept()

msg = conn.recv(1024)
print(pickle.loads(msg))

conn.close()
