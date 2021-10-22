# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import socket
from hashlib import md5
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    key = "key"
    print(md5(key.encode('utf8')).digest())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
