# rock_paper_scissors.py
import random
print('Let\'s play Rock, Paper, Scissors')
random_list = ['rock', 'paper', 'scissors']
play_again = 'y'
play_again = play_again.lower()

while play_again == 'y':
    players_choice = input('Please choose Rock, Paper, or Scissors > ')
    players_choice = players_choice.lower()
    computers_choice = random.choice(random_list)

    if players_choice == computers_choice:
        print('You tied!')
        play_again = input('Would you like to play again (y/n)?')
    elif players_choice == random_list[0]:
        if computers_choice == 'paper':
            print(f'Computer\'s {computers_choice} covered your rock! YOU LOST! ')
            play_again = input('Would you like to play again (y/n)?')
        else:
            print(f'Your rock broke the computer\'s scissors!  YOU WIN!')
            play_again = input('Would you like to play again (y/n)?')
    elif players_choice == random_list[1]:
        if computers_choice == 'rock':
            print(f'Your paper covered the computer\'s rock! YOU WIN!')
            play_again = input('Would you like to play again (y/n)?')
        else:
            print(f'The computer\'s scissors cut up your paper! YOU LOST!')
            play_again = input('Would you like to play again (y/n)?')
    elif players_choice == random_list[2]:
        if computers_choice == 'rock':
            print(f'The computer\'s rock demolished your scissors!  YOU LOST!')
            play_again = input('Would you like to play again (y/n)?')
        else:
            print(f'Your scissors cut the computer\'s paper to shreds!  YOU WIN!')
            play_again = input('Would you like to play again (y/n)?')
