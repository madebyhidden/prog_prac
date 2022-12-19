import socket
import pickle

sock = socket.socket()
sock.connect(('127.0.0.1', 8080))

p, g, a = 7, 5, 3
A = g ** a % p

sock.send(pickle.dumps((p, g, A)))
sock.close()