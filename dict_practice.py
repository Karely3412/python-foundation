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

    teams_dict = {
        'Chicago': 'Bears',
        'Dallas': 'Cowboys',
        'Miami': 'Dolphins'
    }
    
    while True:
        
        options_list = [
        '(A)dd a new team', 
        '(R)emove a team', 
        '(Q)uit?'
        ]

        def the_loop(options_list):
            for i in options_list:
                print(i)


        answers_obj = {
        "answer1": ' has been added to the Big12',
        "answer2": ' has been removed from the Big12',
        "answer3": '- See ya later aligator! -'

        }

        if question.lower() == 'a':
            team_location = input('Enter a Team Location: ')
            team_mascot = input('Enter a Team Mascot: ')

            teams_dict[team_location] = team_mascot
            print(teams_dict)

            print(f'{team_location} {team_mascot}{answers_obj["answer1"]}\n')

        elif question.lower() == 'r':
            team_location = input('Enter a Team Location: ')
            team_mascot = teams_dict[team_location]

            del teams_dict[team_location]
            print(teams_dict)

            print(f'{team_location} {team_mascot}{answers_obj["answer2"]}\n')

        elif question.lower() == 'q':
            print(f'{answers_obj["answer3"]}\n')
            break

        print('Anything else you\'d like to do? \n')
        the_loop(options_list)
        question = input()

        
football_teams()





