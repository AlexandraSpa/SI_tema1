from hashlib import md5
from base64 import b64decode
from base64 import b64encode

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


class aesModeCbc:
    def __init__(self, key, iv):
        self.key = md5(key.encode('utf8')).hexdigest()
        self.iv = Random.new().read(self.block_size)
        self.cipher = AES.new(self.key.encode("utf8"), AES.MODE_CBC, iv)

    def encrypt(self, data):
        data = pad(data.encode('utf-8'), AES.block_size)
        encrypted_text = cipher.encrypt(data)
        return b64encode(iv + encrypted_text).decode("utf-8")

    def decrypt(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        iv = encrypted_text[:AES.block_size]
        cipher = AES.new(self.key.encode("utf8"), AES.MODE_CBC, iv)
        plain_text = cipher.decrypt(encrypted_text[self.block_size:])
        return unpad(plain_text, AES.block_size).decode("utf-8")
