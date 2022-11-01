import socket

import server


def user(host='localhost', port=server.port1):
    try:
        with socket.socket() as s:
            print(">>> Соединение с сервером")
            s.connect((host, port))
            while True:
                inp = input(">>> Input: ")
                if inp == "exit":
                    s.close()
                    print(">>> Разрыв соединения с сервером")
                    break
                print(">>> Отправка данных серверу")
                s.send(inp.encode())
                print(">>> Прием данных от сервера")
                data = s.recv(1024)
                print('>>> Echoing: ', data.decode())

    except KeyboardInterrupt:
        exit(0)


if __name__ == '__main__':
    user()
