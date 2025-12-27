import random
def generate_password(lenght):
    lowerCase = "abcdefghijklmnopqrstuvwxyz"
    upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    sp_char = "!@#$%^&*()<>/?|"
    all_chars = lowerCase + upperCase + numbers + sp_char
    password = ""
    for _ in range(lenght):
        password += random.choice(all_chars)
    return password
password_lenght = int(input("enter password lenght: "))
print("Generated pasword: ", generate_password(password_lenght))