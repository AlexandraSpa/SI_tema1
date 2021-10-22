import socket
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

ClientSocket = socket.socket()
host = '127.0.0.1'
port = 1233

print('Waiting for connection with KM')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

while True:
    start_input = input('Enter the number:\n 1. Say Something\n 2. exit\n')
    if start_input == "2":
        break
    else:
        Input = input('Say Something:')
        ClientSocket.send(str.encode(Input))
        Response = ClientSocket.recv(1024)
        print(Response.decode('utf-8') + '\n')

ClientSocket.close()


class B:
    def __init__(self, k2_key):
        self.k2_key = k2_key


