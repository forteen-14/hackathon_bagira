import socket
import consts


def start_connection():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((consts.IP, consts.PORT))
    return client


def handle_client_by_code(server_code, data):
    if server_code == consts.SEND:
        # CODE#username#category#subject#descreption
        msg_to_send = {"CODE":200, }
        pass
    elif server_code == consts.LOGIN:
        # CODE#username
        # TO-DO IN GUI
        pass
    elif server_code == consts.UPLOAD_MSG_AT_LOGIN:
        # CODE#username CODE#CATEGORY:{USERNAME:TEXT:USERNAME:TEXT}#CATEGORY:{USERNAME:TEXT:USERNAME:TEXT}
        list_of_categories = data.split("#")
        for category in list_of_categories:
            list_of_messages = category.split(",")
            for message in list_of_messages:
                # show the message in gui
                pass
    elif server_code == consts.UPLOAD_MSG_AT_LOGIN:
        # CODE#username CODE#CATEGORY:{USERNAME:TEXT:USERNAME:TEXT}
        pass


def keep_connection(client):
    while True:
        in_data = client.recv(1024)
        sever_msg = in_data.decode()
        server_code = sever_msg[0:2]
        user = handle_client_by_code(server_code, sever_msg[2:])
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
