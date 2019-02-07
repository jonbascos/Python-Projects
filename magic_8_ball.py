print('Welcome to the Magic 8 Ball')
import random
input('Ask the Magic 8 Ball if you will win the lottery tomorrow: ')
result_list = ['Yes', 'No', 'Heck No!', 'Eventually', 'You Wish!', 'Most Definitely']
print(random.choice(result_list))
next_question = input('Would you like to ask another question? yes/no ')

while next_question == 'yes':
    input('Ask another question: ')
    print(random.choice(result_list))
    next_question = input('Would you like to ask another question? yes/no ')
print('Thanks for playing!')
