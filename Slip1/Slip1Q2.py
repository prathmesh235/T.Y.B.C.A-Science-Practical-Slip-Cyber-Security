username = input("Enter username: ")
password = input("Enter password: ")
with open("login.txt", "w") as file:
    file.write("Username: " + username + "\n")
    file.write("Password: " + password + "\n")
print("Login details saved successfully.")

