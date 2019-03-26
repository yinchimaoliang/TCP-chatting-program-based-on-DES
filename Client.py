import socket
from DES import DES
import threading
import os

IP = "127.0.0.2"
PORT = 12345
KEY = "12345678"




class Client():
    def __init__(self,port):
        self.port = port
        self.host = socket.gethostname()
        self.s = socket.socket()
        self.s.connect((IP,self.port))
        print('Linked')
        self.des = DES()


    def receiveMessage(self):
        info_encrypted = self.s.recv(1024).decode()
        # print(info_encrypted)
        info = self.des.decrypt(info_encrypted, KEY)
        print('Server:' + info)


    def communicate(self):
        receive = threading.Thread(target = self.receiveMessage)
        receive.start()
        send_mes = ""
        while send_mes != 'exit':
            send_mes = input()
            if send_mes == "exit":
                break
            send_mes_encrypted = self.des.encrypt(send_mes, KEY)
            self.s.send(send_mes_encrypted.encode())
            print("Message sent.")
        self.s.close()
        os._exit(0)



if __name__ == '__main__':
    server = Client(PORT)
    server.communicate()


# s= socket.socket()
# host = socket.gethostname()
# port = 12345
# s.connect((host,port))
# print('Linked')
# info = ''exit
# while info != 'exit':
#   print('SCIENCE:'+info)
#   send_mes=input()
#   s.send(send_mes.encode())
#   if send_mes =='exit':
#     break
#   info = s.recv(1024).decode()
# s.close()