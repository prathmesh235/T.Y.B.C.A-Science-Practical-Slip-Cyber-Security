from itertools import product

characters = "abcdefghijklmnopqrstuvwxyz"
target_password = input("Enter a 3-character test password: ")

if len(target_password) != 3 or any(ch not in characters for ch in target_password):
    print("Enter exactly 3 lowercase English letters.")
else:
    found = False
    attempts = 0

    for combination in product(characters, repeat=3):
        guess = ''.join(combination)
        attempts += 1

        if guess == target_password:
            print("Password found:", guess)
            print("Attempts:", attempts)
            found = True
            break

    if not found:
        print("Password not found.")
