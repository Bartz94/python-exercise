import random

user_wins = 0
computer_wins = 0
hand_options = ['rock', 'paper', 'scissors']

while True:
    user_input = input('Type rock/paper/scissors or Q to quit: ').lower()
    if user_input == 'q':
        break

    if user_input not in hand_options:
        print('Not a valid option')
        continue

    random_number = random.randint(0, 2)
    computer_choice = hand_options[random_number]
    print('Computer picked', hand_options[random_number])

    if user_input == 'rock' and computer_choice == 'scissors':
        print('You won this round!')
        user_wins += 1
    elif user_input == 'paper' and computer_choice == 'rock':
        print('You won this round!')
        user_wins += 1

    elif user_input == 'scissors' and computer_choice == 'paper':
        print('You won this round!')
        user_wins += 1
    elif user_input == computer_choice:
        print('Its a draw!')

    else: 
        print('You lost this round!')
        computer_wins += 1


print('You won', user_wins, 'times.')
print('The computer won', computer_wins, 'times.')