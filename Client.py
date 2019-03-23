import socket
from DES import DES


PORT = 12345
KEY = "12345678"




class Client():
    def __init__(self,port):
        self.port = port
        self.host = socket.gethostname()
        self.s = socket.socket()
        self.s.connect((self.host,self.port))
        print('Linked')
        self.des = DES()



    def communicate(self):
        info = ""
        while info != "exit":
            if info != "":
                print('Server:' + info)
            send_mes = input("Please input the message you want to send:")
            send_mes_encrypted = self.des.encrypt(send_mes,KEY)
            self.s.send(send_mes_encrypted.encode())
            print("Message sent.")
            if send_mes == "exit":
                break
            info_encrypted = self.s.recv(1024).decode()
            # print(info_encrypted)
            info = self.des.decrypt(info_encrypted,KEY)
        self.s.close()



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