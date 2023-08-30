import socket
import consts


def start_connection():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((consts.IP, consts.PORT))
    return client


def keep_connection(client):
    while True:
        in_data = client.recv(1024)
        print("From Server :", in_data.decode())
        out_data = input()
        client.sendall(bytes(out_data, 'UTF-8'))
        if out_data == 'bye':
            break
    client.close()


def main():
    try:
        client = start_connection()
        keep_connection(client)
    except:
        print("ERROR: Connection failed")


if __name__ == '__main__':
    main()
