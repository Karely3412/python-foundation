


def christmas_tree():
    asterisk = '*'
    first_input = int(input('How many layers tall would you like your tree? '))
    sec_input = input('Virtual elves need a character or symbol to start constructing your tree! ')
    tree_base = f'{asterisk*3:^{first_input*2}}\n{asterisk*3:^{first_input*2}}'
    

    while len(sec_input) > 1:
        sec_input = input('Please only enter one character.')

    our_tree = '' 

    for i in range(0, first_input):
        our_tree += f'{sec_input} '
        print(f'{our_tree:^{first_input*2}}')


    print(tree_base)
    


christmas_tree()



# for a str += makes more sense & for a list, .append() makes alot more sense



"""

    *
   * *
  * * *
 * * * *
* * * * *
   ***
   ***

   
"""
