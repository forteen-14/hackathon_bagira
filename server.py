import consts
import socket, threading
import db

dataBase=db.DataBase()
#msg={
# "category1':[[user1:msg1],[user2:msg2]]
# "category2':[[user3:msg31],[user4:msg4]]
# }

#keep_last_msg={
# "category1':[user1,msg1]
# "category2':[user2:msg2]
# }
class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket,msgs,keep_last_msg):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        self.clientAddress=clientAddress
        self.msgs=msgs
        self.keep_last_msg=keep_last_msg
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


    def sent_handle(self,data):
        username,category,description=data
        msg={username:description}
        self.msgs[category].appand(msg)
        self.keep_last_msg[category]=[username,description]


    def make_last_msgs_packet(self):
        str=f"{consts.LAST_MSGS}#"
        for category,chat in self.keep_last_msg.items():
            name,msg=chat
            str+=f"{category}:[{name}:{msg}]#"
        print(str)
        return str

    def login_handle(self,name):
        self.username=name
        res=""
        if not dataBase.user_exists(name):  # user not exist
            dataBase.add_user(name)
        name,help_got,help_given=dataBase.get_all_data_by_name(name)
        res+=f"{consts.LOGIN}#{name}#{help_got}#{help_given}#"
        res+=self.uplode_at_login_handle()
        print(res)
        return res
    def uplode_at_login_handle(self):
        res=("")
        for catgory,chat in self.msgs.items():
            res += f"{catgory}:["
            for msg in chat:
                res+=f"{msg[0]}:{msg[1]}:"
            res+="]"

        return res
    def handle_client(self,data):
        msg = data.decode()
        print(msg)
        res=""
        if msg == 'bye' or len(data) == 0:
            return False,res
        print(f"from client: {msg}")
        msg_split=msg.split("#")
        if msg_split==consts.SEND:
            res=self.sent_handle(msg[-1])
        elif msg_split==consts.LOGIN:
            res=self.login_handle(msg[1:])

        return True,res







msgs = {}
keep_last_msg = {}
LOCALHOST = consts.IP
PORT = consts.PORT
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock, msgs,keep_last_msg)
    newthread.start()


