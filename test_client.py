import sys
import socket
import threading, time

# global variable
isNormar = True
other_usr = ''


def recieve_msg(username, s):
    global isNormar, other_usr
    print('Please waiting other user login...')
    s.send(('login|%s' % username).encode())
    while (isNormar):
        data = s.recv(1024)  # 阻塞线程，接受消息
        msg = data.split('|')
        if msg[0] == 'login':
            print
            u'%s user has already logged in, start to chat' % msg[1]
            other_usr = msg[1]
        else:
            print
            msg[0]


# 程序入口
def main():
    global isNormar, other_usr
    try:
        print('Please input your name:')
        usrname = input()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("127.0.0.1", 9999))
        t = threading.Thread(target=recieve_msg, args=(usrname, s))
        t.start()
    except:
        print
        'connection exception'
        isNormar = False
    finally:
        pass
    while isNormar:
        msg = input()  # 接受用户输入
        if msg == "exit":
            isNormar = False
        else:
            if (other_usr != ''):
                s.send("talk|%s|%s" % (other_usr, msg))  # 编码消息并发送
    s.close()


if __name__ == "__main__":
    main()