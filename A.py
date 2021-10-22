import socket

ClientSocket = socket.socket()
host = '127.0.0.1'
port = 1233
socket_to_b = socket.socket()
port_b = 1234

try:
   socket_to_b.bind((host, port_b))
except socket.error as e:
    print(str(e))

print('Waiting for a Connection..')
socket_to_b.listen(5)

def send_message(connection):
    connection.send(str.encode('Hi B!'))
    connection.close()


print('Waiting for connection with KM')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

#Response = ClientSocket.recv(1024)
while True:
    start_input = input('Enter the number:\n 1. Say Something\n 2. exit\n 3.Send B a message')
    if start_input == "2":
        break
    elif start_input == "1":
        Input = input('Say Something:')
        ClientSocket.send(str.encode(Input))
        Response = ClientSocket.recv(1024)
        print(Response.decode('utf-8') + '\n')
    else:
        while True:
            b, address = socket_to_b.accept()
            print('Connected to: ' + address[0] + ':' + str(address[1]))
            send_message(b)
            print('Message sent!')

ClientSocket.close()

class A:
    def __init__(self, k2_key):
        self.k2_key = k2_key
    def send_mode(self, mode):
