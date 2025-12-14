import random

def generate_password(length):
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"

    all_chars = lowercase + uppercase + numbers

    password = ""
    for _ in range(length):
        password += random.choice(all_chars)

    return password

# Example usage
password_length = int(input("Enter password length: "))
print("Generated password:", generate_password(password_length))
