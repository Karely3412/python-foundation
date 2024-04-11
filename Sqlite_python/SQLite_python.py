"""
How may functions are needed?
    - Get all func
        - Query 
        - Formatt
        - print
    - Add customer
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


def get_all_customers():
    space = ' '

    customer_data = cursor.execute('SELECT * FROM Customers').fetchall()
    # print(customer_data)
    print('\n--- Customers ---')
    print(f'ID Name{space*23}City{space*15}State{space*6}Phone{space*6}Email\n')

    columns = ['customer_id', 'name', ' city', 'state', 'phone', 'email']

    for row in customer_data:
       print(f'{row[0]:<4}{row[1]:<26}{row[3]:<19}{row[4]:<11}{row[5]:<12}{row[6]}\n')






# customer_menu()
get_all_customers()



