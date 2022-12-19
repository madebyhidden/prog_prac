import socket

web = socket.socket()

web.connect(('google.com', 80))

msg='''GET /index.nginx-debian.html HTTP/1.1
Host: google.com

'''

web.send(msg.encode())
response = web.recv(1024).decode()
web.close()

print(response)
