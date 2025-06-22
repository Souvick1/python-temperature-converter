import random

chars = "abcdefghijklmnopqrstuvwxyz0123456789@#$%^&*!ABCDEFGHIJKLMNOPQRSTUVWXYZ"
length = int(input("Enter password length: "))
password = ""

for a in range(length):
    password += random.choice(chars)

print(password)
