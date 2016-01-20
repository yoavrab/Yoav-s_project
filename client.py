import socket


def main(server_ip, port):
    fi = open("abc.png", "wb")
    client_socket = socket.socket()
    client_socket.connect((server_ip, port))
    length = client_socket.recv(6)
    print length
    data = client_socket.recv(length)
    fi.write(length)
    client_socket.close()


if __name__ == "__main__":
    main("10.10.10.135", 3000)