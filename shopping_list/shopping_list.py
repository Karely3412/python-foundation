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



def add_to_cart(user_input):
    print("What would you like to add ('Return' to return to main menu)?")
    user_input = input()

    with open('shopping_list/stored_list.txt', 'a') as a_file:
        a_file.write(user_input)

    
def clear_cart():
   with open('shopping_list/stored_list.txt', 'w'):
        print('Your shopping list has been cleared!\n')


while True:
    print('What would you like to do? \n')
    user_input = input(' (P)rint the shopping list\n (A)dd an item to the shopping list\n (C)lear the shopping list\n (Q)uit\n').lower()


    if user_input == "p":
        print('There are 0 items in your shopping list')
    elif user_input == "a":
        add_to_cart(user_input)
    elif user_input == "c":
        clear_cart()
    elif user_input == "r":
        print('testing r')
    elif user_input == "q":
        print('-- GoodBye! --')
        break
    
        















