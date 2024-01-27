"""

**** Big12 Football Teams ****
Baylor Bears
Iowa State Cyclones
Texas Longhorns

What would you like to do?
(A)dd a new team, 
(R)emove a team, 
(Q)uit?
A

Add a Team
Team Location: BYU
Team Mascot: Cougars

- BYU has been added to the Big12 -

**** Big12 Football Teams ****
Baylor Bears
Iowa State Cyclones
Texas Longhorns
BYU Cougars

What would you like to do?
(A)dd a new team, 
(R)emove a team, 
(Q)uit?
R

Remove a team
Which team would you like to remove?
Texas

- Texas has been removed from the Big12 -

**** Big12 Football Teams ****
Baylor Bears
Iowa State Cyclones
BYU Cougars

What would you like to do?
(A)dd a new team, 
(R)emove a team, 
(Q)uit?
Q

- Goodbye -


"""

def football_teams():

    print('**** Big12 Football Teams ****\n')
    question = input('What would you like to do? \n')
    # print(question)

    while True:

        # statement1 = input('Enter a Team Location: ')
        # statement2 = input('Enter a Team Mascot: ')

        options_list = [
        '(A)dd a new team', 
        '(R)emove a team', 
        '(Q)uit?'
        ]

        def the_loop(list):
            for i in options_list:
                print(i)


        answers_obj = {
        "answer1": ' has been added to the Big12',
        "answer2": ' has been removed from the Big12',
        "answer3": '- See ya later aligator! -'

        }


        empty_dict = {}

        if question == 'a' or question == 'A':
            print(f'{answers_obj["answer1"]}\n')
            print('Anything else you\'d like to do? \n')
            the_loop(options_list)
            question = input()

        elif question == 'r' or question == 'R':
            print(f'{answers_obj["answer2"]}\n')
            question = input('Anything else you\'d like to do? \n')
            the_loop(options_list)

        elif question == 'q' or question == 'Q':
            print(f'{answers_obj["answer3"]}\n')
            break


        
football_teams()





