import socket
from DES import DES
import threading
import os


IP = "127.0.0.2"
PORT = 12345
KEY = "12345678"



class Server():
    def __init__(self,port):
        self.host = socket.gethostname()
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.bind((IP,port))
        self.s.listen(1)
        self.sock,self.addr = self.s.accept()
        self.des = DES()
        print('Connection built')
        print(self.addr)

    def receiveMessage(self):
        info_encrypted = self.sock.recv(1024).decode()
        info = self.des.decrypt(info_encrypted, KEY)
        print('Client:' + info)

    def communicate(self):

        t = threading.Thread(target=self.receiveMessage)
        t.start()
        send_mes = ""
        while send_mes != 'exit':

          send_mes = input()
          if send_mes =='exit':
            break
          send_mes_encrypted = self.des.encrypt(send_mes,KEY)
          self.sock.send(send_mes_encrypted.encode())
          print("Message sent.")


        self.sock.close()
        self.s.close()
        os._exit(0 )





if __name__ == '__main__':
    server = Server(PORT)
    server.communicate()



# host = socket.gethostname()
# port = 12345
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind((host,port))
# s.listen(1)
# sock,addr = s.accept()
# print('Connection built')
# info = sock.recv(1024).decode()
# while info != 'exit':
#   print('MOOD:'+info)
#   send_mes = input()
#   sock.send(send_mes.encode())
#   if send_mes =='exit':
#     break
#   info = sock.recv(1024).decode()
# sock.close()
# s.close()