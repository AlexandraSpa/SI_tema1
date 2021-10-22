import hashlib
import socket
from _thread import *
import socket
import hashlib
from hashlib import md5
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

ServerSocket = socket.socket()
host = '127.0.0.1'
port = 1233
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waiting for a Connection..')
ServerSocket.listen(5)


def threaded_client(connection):
    connection.send(str.encode('Welcome to the Server!'))
    while True:
        data = connection.recv(1024)
        reply = 'Server Says: ' + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()


while True:
    if input('Waiting for a command: ') == "exit":
        break
    else:
        Client, address = ServerSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        start_new_thread(threaded_client, (Client,))
        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))

ServerSocket.close()


class KeyManager:
    def __init__(self, k_key, k2_key):
        self.k_key = md5(k_key.encode('utf8')).digest()
        self.k2_key = k2_key
    def send_key(self, mode):
        if mode == "ECB":
            aesModeEbc.init()
            return "you need to use AES_mode_ECB"

        else:
            aesModeCbc.init()
            return "you need to use AES_mode_CBC"



