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

        if int(player_2) < int(player_1) :
            print('Too low! Try again! ')
        elif  int(player_2) > int(player_1) : 
            print("Too high! Try again! ")
        else:
            print('You nailed it!')
            break

        player_2 = input('Guess again!(: ')

high_low()
    