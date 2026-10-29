#OR
#Q.2) Write a Python program to implement Caesar Cipher for both encryption and decryption of a given text.

def encrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - 65 + shift) % 26 + 65)
        elif ch.islower():
            result += chr((ord(ch) - 97 + shift) % 26 + 97)
        else:
            result += ch
    return result
def decrypt(text, shift):
    return encrypt(text, -shift)
text = input("Enter text: ")
shift = int(input("Enter shift value: "))
encrypted = encrypt(text, shift)
print("Encrypted text:", encrypted)
print("Decrypted text:", decrypt(encrypted, shift))
