#Q.2 Write a Python program to simulate a SHA-256 hash generator that accepts user input text and computes its corresponding 256-bit hash value.

import hashlib
text = input("Enter text: ")
hash_value = hashlib.sha256(text.encode())
print("SHA-256 Hash:", hash_value.hexdigest())

