#Q.2.Write a Python program to shift each alphabet by 2 positions.

text = input("Enter a message: ")
result = ""
for ch in text:
    if ch.isupper():
        result += chr((ord(ch) - 65 + 2) % 26 + 65)
    elif ch.islower():
        result += chr((ord(ch) - 97 + 2) % 26 + 97)
    else:
        result += ch
print("Encrypted text:", result)
