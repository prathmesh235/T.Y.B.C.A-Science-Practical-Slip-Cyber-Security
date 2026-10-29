#or
#Q.2. Write a Python program to encrypt user input text using AES encryption

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import base64

key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_ECB)

text = input("Enter text to encrypt: ")
data = pad(text.encode(), AES.block_size)
encrypted = cipher.encrypt(data)

print("Encrypted text:", base64.b64encode(encrypted).decode())
