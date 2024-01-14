"""

I'm thinking of a number between 1 and 100.
What is your guess? 50
Too low

What is your guess? 75
Too high

What is your guess? 68
Too high

What is your guess? 67
That's correct!!!!

"""


def high_low():
    player_1 = input('Player 1 enter a number: \n')
    print('I\'m thinking of a number between 1 and 100..\n')
    player_2 = input('..Can you guess what it is? ')

    while True:
        next_guess = input('Guess again! ')

        if player_2 < player_1 and next_guess < player_1:
            print(f'Too low! Try again!{next_guess}\n')
        elif  player_2 > player_1 and next_guess > player_1: 
            print(f'Too high! Try again!{next_guess}\n')
        else:
            print('You nailed it!')
            break


high_low()
    

"""









"""