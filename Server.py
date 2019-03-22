import socket
from DES import DES



PORT = 12345
KEY = "12345678"



class Server():
    def __init__(self,port):
        self.host = socket.gethostname()
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.bind((self.host,port))
        self.s.listen(1)
        self.sock,self.addr = self.s.accept()
        self.des = DES()
        print('Connection built')



    def communicate(self):
        info = self.sock.recv(1024).decode()
        # info = self.des.DES(info_encrypted,KEY,1)
        while info != 'exit':
          print('MOOD:'+info)
          send_mes = input()
          self.sock.send(send_mes.encode())
          if send_mes =='exit':
            break
          info = self.sock.recv(1024).decode()
        self.sock.close()
        self.s.close()





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