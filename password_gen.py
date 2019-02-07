# password_gen.py
import string
import random
password_length = input('How many characters should your password be? > ')
password_length = int(password_length)
random_password = ''
count = 0
while count < password_length:
    random_generator = random.choice(string.ascii_letters + string.digits + string.punctuation)
    random_password = random_password + random_generator
    count = count + 1
print(random_password)
