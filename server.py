import consts
import socket, threading
import db

dataBase=db.DataBase()

class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket,msgs,keep_last_msg):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        self.clientAddress=clientAddress
        self.msgs=msgs
        self.keep_last_msf=keep_last_msg
        self.username=""
        print ("New connection added: ", clientAddress)

    def run(self):
        print ("Connection from : ", self.clientAddress)
        run_flag=True
        while run_flag:
            data = self.csocket.recv(2048)
            run_flag,msg=self.handle_client(data)
            if not run_flag:
                break
            self.csocket.send(bytes(msg,'UTF-8'))


        print ("Client at ", self.clientAddress , " disconnected...")


    def send_handle(self,data):
        username,category,subject,description=data
        self.msgs[category].appand(data)



    def login_handle(self,name):
        self.username=name
        dataBase.add_user(name)
    def uplode_at_login_handle(self,data):
        pass
    def handle_client(self,data):
        msg = data.decode()
        res=""
        if msg == 'bye' or len(data) == 0:
            return False,res
        print(f"from client: {msg}")
        msg_split=msg.split("#")
        if msg_split==consts.SEND:
            res=self.send_handle(msg[1:])
        elif msg_split==consts.LOGIN:
            self.login_handle(msg[1:])
        elif msg_split==consts.UPLOAD_MSG_AT_LOGIN:
            res=self.uplode_at_login_handle(msg[1:])



        return True,res


class server:
    def __init__(self):
        self.msgs = {}
        self.keep_last_msg = {}
        self.LOCALHOST = consts.IP
        self.PORT = consts.PORT
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((self.LOCALHOST, self.PORT))
        print("Server started")
        print("Waiting for client request..")
        while True:
            server.listen(1)
            clientsock, clientAddress = server.accept()
            newthread = ClientThread(clientAddress, clientsock, self.msgs,self.keep_last_msg)
            newthread.start()


