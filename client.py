import socket
import consts


def start_connection():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((consts.IP, consts.PORT))
    client.sendall(bytes("This is from Client", 'UTF-8'))
    return client


def keep_connection(client):
    while True:
        in_data = client.recv(1024)
        sever_msg = in_data.decode()
        server_code = sever_msg[0:2]
        if server_code == consts.SEND:
            pass
        elif server_code == consts.LOGIN:
            #CODE#username CODE#CATEGORY:{USERNAME:TEXT:USERNAME:TEXT}#CATEGORY:{USERNAME:TEXT:USERNAME:TEXT}


        elif server_code == consts.UPLOAD_MSG_AT_LOGIN:
            pass
        print("From Server :", sever_msg)
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
