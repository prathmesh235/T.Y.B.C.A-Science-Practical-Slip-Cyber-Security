#Q.2) Write a Python program that accepts a sentence from the user and encrypts it using Caesar Cipher

text = input("Enter a sentence: ")
shift = 3
result = ""
for ch in text:
    if ch.isupper():
        result += chr((ord(ch) - 65 + shift) % 26 + 65)
    elif ch.islower():
        result += chr((ord(ch) - 97 + shift) % 26 + 97)
    else:
        result += ch
print("Encrypted sentence:", result)
