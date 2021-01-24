import socket
import threading 
import os

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip = input("\n\t\tEnter Your IP : ")
port = 5007

s.bind( (ip,port) )

sip = input("\n\t\tEnter Server IP : ")
sport = 1234

print()
os.system('tput setaf 3')
os.system('figlet -c -f bubble.flf Python Chat App')

def send():
    while True:
        os.system('tput setaf 3')
        msg = input('\n').encode()
        s.sendto(msg,(sip,sport))
        if msg.decode() == "exit":
            os._exit(1)
        
def recv():
    while True:
        os.system('tput setaf 3')
        msg = s.recvfrom(1024)
        if msg[0].decode() == "exit":
            os._exit(1)
        
        print('\n\t\t\t\t\t\t\t\t\tReceived -> ' + msg[0].decode())

t1 = threading.Thread(target=send)
t2 = threading.Thread(target=recv)

t1.start()
t2.start()
