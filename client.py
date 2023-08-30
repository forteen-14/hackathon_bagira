import socket
import consts
import user
import time


user = user.User("name", 0, 0)


def start_connection():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((consts.IP, consts.PORT))
    return client


def send_msg_to_everyone(catagory, msg, client):
    msg_to_send = {"CODE": consts.SEND, "USERNAME": user.name, "CATEGORY": consts.RESCUE_FROM_CAR, "MSG": "im stuck in my car"}
    client.sendall(bytes(str(msg_to_send), 'UTF-8'))


def login(client):
    # we would get that from gui
    user_name = "idk"
    msg_to_send =f"{consts.LOGIN}#{user_name}"
    client.sendall(bytes(str(msg_to_send), 'UTF-8'))
    time.sleep(0.1)
    get_user_info(client)


def get_user_info(client):
    data = client.recv(1024)
    sever_msg = data.decode()
    user_info = data.split("#")
    user.name = user_info[0]
    user.help_given = user_info[1]
    user.help_got = user_info[2]


def upload_msg_at_login(client):
    msg_to_send = {"CODE": consts.UPLOAD_MSG_AT_LOGIN}


def keep_connection(client):
    while True:
        login(client)
        print(user)
    client.close()


def main():
    try:
        client = start_connection()
        keep_connection(client)
    except:
        print("ERROR: Connection failed")


if __name__ == '__main__':
    main()
