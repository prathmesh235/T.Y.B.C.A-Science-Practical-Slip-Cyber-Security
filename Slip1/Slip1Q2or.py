common_passwords = ["123456", "password", "admin123",
                    "qwerty", "welcome", "abc123"]
target_password = input("Enter target password: ")
if target_password in common_passwords:
    print("Password found in dictionary!")
    print("Password is weak.")
else:
    print("Password not found in dictionary.")
