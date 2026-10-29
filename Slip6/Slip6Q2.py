#Q.2) Write a Python program to check password strength: Length ≥ 8 and password must contain digits and special characters

password = input("Enter password: ")
has_digit = any(ch.isdigit() for ch in password)
has_special = any(not ch.isalnum() for ch in password)
if len(password) >= 8 and has_digit and has_special:
    print("Strong password")
else:
    print("Weak password")
