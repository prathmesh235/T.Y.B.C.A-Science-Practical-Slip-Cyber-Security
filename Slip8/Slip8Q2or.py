
#OR
#Q.2) Write a Python program to implement a dictionary attack using a list of common passwords to check whether a target password exists in the list

common_passwords = ["123456", "password", "admin123",
                    "qwerty", "welcome", "abc123"]
target = input("Enter target password: ")
if target in common_passwords:
    print("Password found in dictionary!")
else:
    print("Password not found in dictionary.")
