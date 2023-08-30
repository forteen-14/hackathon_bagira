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
    msg_to_send = f"{consts.SEND}#{user.name}#{catagory}#{msg}"
    client.sendall(bytes(str(msg_to_send), 'UTF-8'))


def login(client):
    # we would get that from gui
    user_name = "idk"
    msg_to_send = f"{consts.LOGIN}#{user_name}"
    client.sendall(bytes(str(msg_to_send), 'UTF-8'))
    time.sleep(0.1)
    get_user_info(client)


def get_user_info(client):
    data = client.recv(1024)
    sever_msg = data.decode()
    user_info = sever_msg.split("#")
    user.name = user_info[1]
    user.help_given = user_info[2]
    user.help_got = user_info[3]
    print(sever_msg)


def get_last_msg(client):
    msg_to_send = f"{consts.LAST_MSGS}"
    client.sendall(bytes(str(msg_to_send), 'UTF-8'))
    data = client.recv(1024)
    sever_msg = data.decode()
    print("tttt",sever_msg)




def keep_connection(client):
    login(client)
    send_msg_to_everyone(consts.DANGER, "im stuck", client)
    get_last_msg(client)
    client.close()


def main():
    try:
        client = start_connection()
        keep_connection(client)
    except:
        print("ERROR: Connection failed")


if __name__ == '__main__':
    main()
