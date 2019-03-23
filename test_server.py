import sys
import socket
import threading, time
import User

# global variable
userlist = []


def hand_user_con(usr):
    try:
        isNormar = True
        while isNormar:
            data = usr.skt.recv(1024)
            time.sleep(1)
            msg = data.split('|')  # 分析消息
            if msg[0] == 'login':
                print
                'user [%s] login' % msg[1]
                usr.username = msg[1]
                notice_other_usr(usr)
            if msg[0] == 'talk':
                print
                'user[%s]to[%s]:%s' % (usr.username, msg[1], msg[2])
                send_msg(msg[1], msg[2])  # 发送消息给目标用户，参数1：目标用户，参数2：消息内容
            if msg[0] == 'exit':
                print
                'user [%s] exit' % msg[0]
                isNormar = False
                usr.close()
                userlist.remove(usr)
    except:
        isNormar = False


# 通知其他用户以上的好友
def notice_other_usr(usr):
    if (len(userlist) > 1):
        print
        'The two users'
        userlist[0].skt.send(("login|%s" % userlist[1].username))
        userlist[1].skt.send(("login|%s" % userlist[0].username))
    else:
        print
        'The one users'


def send_msg(username, msg):
    for usr in userlist:
        if (usr.username == username):
            usr.skt.send(msg)


# 程序入口
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 9999))
    s.listen(5)
    print
    u'waiting for connection...'
    while True:
        sock, addr = s.accept()  # 等待用户连接
        user = User.User(sock)
        userlist.append(user)
        t = threading.Thread(target=hand_user_con, args=(user,));
        t.start()
    s.close()


if __name__ == "__main__":
    main()