import random

max_range = 100
print('Can you guess number from 1 to 100?')

random_number = random.randint(0,max_range)
guesses = 0

while True:
    print(random_number)
    guesses += 1
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Type a number!')
        continue

    if user_guess == random_number:
        print('Correct!')
        break
    elif user_guess > random_number:
        print('Hit lower!')
    else:
        print('Hit higher!')

print('You guess it in', guesses, 'tries.')

