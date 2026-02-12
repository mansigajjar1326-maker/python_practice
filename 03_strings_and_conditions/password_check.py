# Simple password strength checker

password = input("Create a password: ")

if len(password) >= 8:
    print("Strong password")
else:
    print("Weak password (minimum 8 characters required)")
