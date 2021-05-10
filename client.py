import socket
import threading
import encrypte
nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if ": " in message:
                message_dec = encrypte.caesar_dec(message.split(": ")[1],N) 
                name = message.split(": ")[0]
                message = name+": "+message_dec
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break

text = "ATTACKATONCE"
s = 4 

#Number of shifting
N=3
# Sending Messages To Server
def write():
    while True:
        message = '{}: {}'.format(nickname, encrypte.caesar_enc(input(''),N))
        client.send(message.encode('ascii'))
        
      
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

