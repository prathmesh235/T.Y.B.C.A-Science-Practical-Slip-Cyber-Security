PHISHING AND ALGORITHM TO IDENTIFY PHISHING EMAILS
Q. What is phishing? Explain the step-by-step algorithm to identify phishing emails. [10 Marks]

1. WHAT IS PHISHING?
Phishing is a cyber attack in which an attacker pretends to be a trusted person or organisation (bank, company, colleague) and tricks the victim, usually through email, into revealing sensitive data such as passwords, OTP or card details, or into clicking a malicious link. It is a form of social engineering.
Types: Email phishing, Spear phishing (targeted), Whaling (executives), Smishing/Vishing (SMS/call).
Example: A fake email says "Your bank account is blocked, click here to verify"; the link opens a fake site that steals login details.

2. ALGORITHM TO IDENTIFY PHISHING EMAILS
Input: received email | Output: Phishing / Suspicious / Legitimate
Step 1: Check sender address - misspelled or unofficial domain (paypa1.com), free email ID used by a company.
Step 2: Check email headers - SPF/DKIM/DMARC failure, Reply-To different from From.
Step 3: Check greeting and language - generic greeting ("Dear Customer"), spelling or grammar mistakes.
Step 4: Check urgency or threat - "Act now", "Account will be blocked", "You won a prize".
Step 5: Check requests for sensitive data - password, OTP, PIN or CVV asked by email means HIGH suspicion.
Step 6: Inspect links without clicking - hover to compare text and real URL; shortened URLs, IP addresses, no HTTPS.
Step 7: Inspect attachments - unexpected .exe, .zip or macro-enabled files.
Step 8: Verify through another channel - contact the organisation on its official website or phone number.
Step 9: Classify - high score = PHISHING, medium = SUSPICIOUS, low = LEGITIMATE.
Step 10: Report and act - do not click, delete, report to IT/provider; if data was entered, change passwords and inform the bank.

