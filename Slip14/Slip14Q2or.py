#OR
#Q.2) Write a program to display ASCII values of characters before encryption
text = input("Enter text: ")
print("Character and ASCII values:")
for ch in text:
    print(ch, "=", ord(ch))
