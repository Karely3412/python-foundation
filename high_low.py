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
    player_1 = int(input('Player 1 enter a number: \n'))      # <- integer 

    while player_1 >= 101:
        player_1 = int(input("Oops! Choose a number between 1-100:\n "))

    print('I\'m thinking of a number between 1 and 100..\n')


    player_2 = int(input('..Can you guess what it is? '))     # <- integer

    while True:

        if player_2 < player_1 :
            print('Too low! Try again!\n ')
        elif  player_2 > player_1 : 
            print("Too high! Try again!\n ")
        else:
            print('You nailed it!')
            break

        player_2 = int(input('Guess again!(:\n '))

high_low()
    