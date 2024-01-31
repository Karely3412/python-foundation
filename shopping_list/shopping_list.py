"""
Welcome to your shopping list program!

--------------------------
What would you like to do?

(P)rint the shopping list
(A)dd an item to the shopping list
(C)lear the shopping list
(Q)uit
p

There are 0 items in your shopping list

--------------------------
What would you like to do?

(P)rint the shopping list
(A)dd an item to the shopping list
(C)lear the shopping list
(Q)uit
a

What would you like to add ('Return' to return to main menu)?
Butter

"Butter" has been added to the shopping list

What would you like to add ('Return' to return to main menu)?
Eggs

"Eggs" has been added to the shopping list

What would you like to add ('Return' to return to main menu)?
Cheese

"Cheese" has been added to the shopping list

What would you like to add ('Return' to return to main menu)?


--------------------------
What would you like to do?

(P)rint the shopping list
(A)dd an item to the shopping list
(C)lear the shopping list
(Q)uit
p

You shopping list:
Butter
Eggs
Cheese

--------------------------
What would you like to do?

(P)rint the shopping list
(A)dd an item to the shopping list
(C)lear the shopping list
(Q)uit
c

Your shopping list has been cleared

--------------------------
What would you like to do?

(P)rint the shopping list
(A)dd an item to the shopping list
(C)lear the shopping list
(Q)uit
q

Exiting the program. Your shopping list has been saved in 'shopping_list.txt'.
Goodbye!


"""


print('Welcome to your shopping list program!\n')
print('What would you like to do? \n')

menu = [
'(P)rint the shopping list',
'(A)dd an item to the shopping list',
'(C)lear the shopping list',
'(Q)uit'
]

for i in menu: 
    print(i)

user_input = input('')













