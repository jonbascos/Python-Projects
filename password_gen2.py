# password_gen2.py
import string
import random

random_letters = random.choice(string.ascii_letters)
random_digits = random.choice(string.digits)
random_punctuations = random.choice(string.punctuation)

number_of_letters = input('How many letters do you want your password to have? > ')
number_of_digits = input('How many digits do you want your password to have? > ')
number_of_punctuations = input('How many punctuations do you want your password to have? > ')

number_of_digits = int(number_of_digits)
number_of_letters = int(number_of_letters)
number_of_punctuations = int(number_of_punctuations)

total_characters = number_of_digits + number_of_letters + number_of_punctuations

random_password = ''
count = 0

while count < total_characters:
    
    while number_of_digits < number_of_digits:
        random_password = random_password + random_digits

    while number_of_letters < number_of_letters:
        random_password = random_password + random_letters

    while number_of_punctuations < number_of_punctuations:
        random_password = random_password + random_punctuations
print(random_password)
