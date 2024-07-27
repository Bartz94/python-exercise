# Game rules
# 1. Select players 2 to 4
# 2.You can only roll the dice during your turn
# 3. Rolling a 1 ends the turn and sets the turn score to zero
# 4. If you are happy with the total result, you can skip rolling and save it to your total
# 5. First one to exceed 50 points wins the game

# to run type: python diceGame.py
# Enjoy

import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)

    return roll

while True:
    players = input('Enter the number of players (1-4): ')
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print('Invalid, try again.')        

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_index in range(players):
        print('\nPlayer', player_index + 1, 'turn has started!')
        print('Total score: ', player_scores[player_index], '\n')
        current_score = 0

        while True:    
            should_roll = input("Would like to roll (y)? ")
            if should_roll.lower() != 'y':
                break
    
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else: 
                current_score += value
                print('You rolled a: ', value)

                print('Your score is: ', current_score)
    
        player_scores[player_index] += current_score
        print('Your total score is: ', player_scores[player_index])

max_score = max(player_scores)
winning_player = player_scores.index(max_score)
print("Player", winning_player + 1, 'is the winner with a score of: ', max_score)