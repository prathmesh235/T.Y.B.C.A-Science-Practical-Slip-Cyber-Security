BRUTE FORCE ATTACKS
Q. Explain Brute Force Attacks with an example, detailing Simple, Dictionary, and Hybrid brute force types. [10 Marks]

1. WHAT IS A BRUTE FORCE ATTACK?
A brute force attack is a trial-and-error method in which an attacker systematically tries many passwords, PINs or encryption keys until the correct one is found. It needs no vulnerability in the system; it depends only on computing power and time. Weak and short passwords are cracked quickly.
Example: An attacker targets a login page for the username "admin" and uses a tool to try thousands of passwords per minute (a, b, c ... 0000, 0001 ... password123) until the site accepts one. A 4-digit PIN has only 10,000 combinations, so it can be cracked in seconds.

2. TYPES OF BRUTE FORCE ATTACKS

1. Simple (Pure) Brute Force
The attacker tries every possible combination of characters (letters, digits, symbols) one by one: a, b, ... aa, ab, ... aaa and so on.
Guaranteed to succeed eventually, but very slow for long passwords.
Example: Cracking a 4-digit PIN by trying 0000 to 9999.

2. Dictionary Attack
The attacker tries words from a pre-made list (dictionary) of common passwords, names and words, instead of all combinations.
Much faster, but works only if the password is a common or predictable word.
Example: Trying password, welcome, iloveyou, qwerty123, admin@123.

3. Hybrid Brute Force
A combination of both: dictionary words are modified with numbers, symbols or capital letters, since users often make small changes to common words.
Faster than simple brute force and catches slightly modified words.
Example: From the word "summer" it tries Summer1, summer@2024, Summer!, s&mmer.

