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

def print_shopping_list():
    with open('shopping_list/stored_list.txt', 'r') as a_file:
        read_file = a_file.read()
        if not read_file:
            print('There are 0 items in your shopping list.\n')
        else:
            print(f"Your current shopping list items are:\n\n{read_file}")
        

def add_to_cart(user_input):
    while True:
        print("What would you like to add ('Return' to return to main menu)?")
        user_input = input().lower()

        with open('shopping_list/stored_list.txt', 'a') as a_file:
            a_file.write(f'{user_input}\n')
        if user_input == "r":
            break

    
def clear_cart():
   with open('shopping_list/stored_list.txt', 'w'):
        print('Your shopping list has been cleared!\n')

def while_true():
    while True:
        print('What would you like to do? \n')
        user_input = input(' (P)rint the shopping list\n (A)dd an item to the shopping list\n (C)lear the shopping list\n (Q)uit\n').lower()


        if user_input == "p":
            print_shopping_list()

        elif user_input == "a":
            add_to_cart(user_input)

        elif user_input == "c":
            clear_cart()

        elif user_input == "q":
            print('-- GoodBye! --')
            break


while_true()
    


        















