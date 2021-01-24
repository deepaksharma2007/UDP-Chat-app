import socket
import os
import threading

s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

ip = input("\n\tEnter ur IP :")
port = 1234

s.bind( (ip,port) )

ser_ip = input("\n\tEnter server IP : ")
ser_port  = 5007

os.system('tput setaf 3')
os.system('figlet -c -k Python Chat APP')

def rece():
    while True:
        os.system('tput setaf 2')
        msg = s.recvfrom(1024)
        if msg[0].decode() == "exit":
             os._exit(1)
        print('\n\t\t\t\t\t\t\tReceived ->  ' + msg[0].decode())

def send():
    while True:
        os.system('tput setaf 2')
        msg = input('\n').encode()
        s.sendto(msg , (ser_ip , ser_port))
        if msg.decode() == "exit":
           os._exit(1)

t1 = threading.Thread( target=rece )
t2 = threading.Thread( target=send )

t1.start()
t2.start()

