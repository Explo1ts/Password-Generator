import random
import string
import os
import time

def generate_password(password_len, chars_set):
    password = ""
    for _ in range(password_len):
        password_char = random.choice(chars_set)
        password += password_char
    return password

print("Welcome To The Advanced Password Generator")

lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
numbers = string.digits
special_chars = "!@#$%^&*()-+="

chars = lowercase_letters + uppercase_letters + numbers + special_chars

while True:

    password_len = int(input("What length would you like your password to be? (8 - 64 characters)\n"))

    if password_len < 8 or password_len > 64:
        print("Password length must be between 8 and 64 characters.")
        continue

    password_count = int(input("How many passwords would you like to generate?\n"))

    if password_count <= 0:
        print("You must enter a positive number for password count.")
        continue

    seed = int(time.time())

    with open("Passwords.txt", "w") as file:

        for _ in range(password_count):

            password = generate_password(password_len, chars)
            print(f"Here is your password: {password}")
            file.write(f"{password}\n")

        print(f"\n{password_count} passwords have been saved to Passwords.txt.")

    continue_choice = input("Would you like to generate more passwords? (yes/no): ")

    if continue_choice.lower() != 'yes':
        break