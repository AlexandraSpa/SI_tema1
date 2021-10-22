from hashlib import md5
from base64 import b64decode
from base64 import b64encode

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


class aesModeEbc:
    def __init__(self, key):
        self.key = key
        self.cipher = AES.new(self.key, AES.MODE_ECB)

    def encrypt(self, data):
        data = pad(data.encode('utf-8'), AES.block_size)
        encrypted_text = cipher.encrypt(data)
        return b64encode(encrypted_text).decode("utf-8")

    def decrypt(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        cipher = AES.new(self.key, AES.MODE_ECB)
        plain_text = cipher.decrypt(encrypted_text)
        return unpad(plain_text, AES.block_size).decode("utf-8")