#Q.2. Write a Python program to detect spam emails using predefined keywords.

spam_keywords = ["win", "free", "prize", "offer", "lottery", "cash"]
email = input("Enter email message: ").lower()
for keyword in spam_keywords:
    if keyword in email:
        print("Spam email detected!")
        break
else:
    print("Email is not spam.")
