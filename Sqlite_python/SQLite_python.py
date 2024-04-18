"""
How may functions are needed? REMEMBER THAT FUNCTIONS SHOULD ONLY DO ONE THING.
    - Get all func
        - Query 
        - Formatt (parse)
        - print
    - Add customer
        - Insert into database
        - Formatt (parse)
        - print
    - Update customer info
    - Search for one 
    - Delete by cust id
    - Print menu func


1. Print menu options
2. View all Customers in a table
3. Search for Customers by name (partial name)
4. Add a new Customer to the database
5. Update a Customer record (like changing their phone number)
6. Delete a Customer using their customer_id
7. Quit

"""

import sqlite3

conn =  sqlite3.connect('Sqlite_python/dp_customers.db')

cursor = conn.cursor()


def customer_menu():
    print('\n**** Customer Database ****\n')
    menu_options = ["[1] View All Customers", "[2] Search Customers", "[3] Add a New Customer", "[Q] Quit\n"]

    for i in menu_options:
        print(i)


def menu_selection():
    main_menu = input('(Press "Enter" to return to Main Menu) \n')
    print(main_menu)

#     if main_menu == 'Enter':
#         customer_menu()


def get_all_customers(user_input):
    space = ' '
    customer_data = cursor.execute('SELECT * FROM Customers').fetchall()

    print('\n--- Customers ---')
    print(f'ID Name{space*23}City{space*15}State{space*6}Phone{space*6}Email\n')


    for row in customer_data:
        print(f'{row[0]:<3}{row[1]:<26}{row[3]:<19}{row[4]:<11}{row[6]:<12}{row[7]}\n')



def search_customer(customer_id):
    customer_data = cursor.execute("SELECT name,street_address,city,state,phone,email FROM Customers WHERE customer_id = ?", (customer_id,)).fetchone()
    return customer_data



def add_customer():
    print('### New Customer ###')
    print('Please fill out the form below to add a new Customer:')
    customer_name = input('Customers name: ')
    customer_address = input('Customers address: ')
    customer_city = input('Customers city: ')
    customer_state = input('Customers state: ')
    customer_postal_code = input('Customers postal code: ')
    phone = input('Customers phone: ')
    email = input('Customers email: ')

    cursor.execute('INSERT INTO Customers (name, street_address, city, state, postal_code, phone, email) VALUES (?,?,?,?,?,?,?)',(customer_name, customer_address, customer_city, customer_state, customer_postal_code, phone, email))

    print(f'SUCCESS: Customer "{customer_name}" Successfully added!')

    conn.commit()


def delete_customer():
    print('Enter Customer ID: ')
    customer_id = input()
    customer_data = cursor.execute("SELECT customer_id, name FROM Customers WHERE customer_id = ?", (customer_id,)).fetchone()
    # print(customer_data[1])

    print(f'Are SURE you want to DELETE {customer_data[0]}:"{customer_data[1]}" (y/n)?')
    customer_answer = input()

    if customer_answer == 'y':
        print(f'"SUCCESS: Customer {customer_data[1]} succesfully Deleted!"')

        cursor.execute('DELETE FROM Customers WHERE customer_id = ?', (customer_id,)).fetchone()

    conn.commit()


    




# customer_menu()
# get_all_customers(1)
# print(search_customer(5))
add_customer()
# delete_customer()



