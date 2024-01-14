


def christmas_tree():
    asterisk = '*'
    first_input = input('How many layers tall would you like your tree? ')
    sec_input = input('Virtual elves need a character or symbol to start constructing your tree! ')
    tree_base = f'{asterisk*3:^50}\n{asterisk*3:^50}'

    our_tree = '' 

    for i in range(0, int(first_input)):
        our_tree += f'{sec_input} '
        print(f'{our_tree:^50}')


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