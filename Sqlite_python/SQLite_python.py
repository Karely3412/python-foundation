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


def customer_detail(customer_data):

    print("\n+++ Customer Detail +++")
    print(f'{"ID:":<10}{customer_data[0]}\n{"Name:":<10}{customer_data[1]}\n{"Address:":<10}{customer_data[2]}\n{"City:":<10}{customer_data[3]}\n{"State:":<10}{customer_data[4]}\n{"Zipcode:":<10}{customer_data[5]}\n{"Phone:":<10}{customer_data[6]}\n{"Email:":<10}{customer_data[7]}\n')


def get_all_customers():
    space = ' '
    customer_data = cursor.execute('SELECT * FROM Customers').fetchall()

    print('\n--- Customers ---')
    print(f'ID Name{space*23}City{space*15}State{space*6}Phone{space*6}Email\n')


    for row in customer_data:
        print(f'{row[0]:<3}{row[1]:<26}{row[3]:<19}{row[4]:<11}{row[6]:<12}{row[7]}\n')
    

    # print("\nEnter a Customer ID to View a Customer:")
    # print("Press 'Enter' to return to Main Menu")
    # customer_answer = input()
    
    # if customer_answer == 'enter' and customer_answer == '':
    #     customer_menu()
    # else:
    #     searched_cust = search_customer(customer_answer)
    #     customer_detail(searched_cust)



def search_customer(customer_id):
    # cursor.execute("SELECT customer_id, name, street_address, city, state, postal_code, phone, email FROM Customers WHERE customer_id = ?", (customer_id,)).fetchone()
    customer_data = cursor.execute("SELECT customer_id, name, street_address, city, state, postal_code, phone, email FROM Customers WHERE customer_id = ?", (customer_id,)).fetchone()
    # print(customer_data)

    if customer_id == None:
        print("User not found.")
    else:
        return customer_data

    # customer_detail(customer_data)



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



def update_customer(customer_id, user_input):
    id_search_results = search_customer(customer_id)

    if user_input == "n":
        print(f"\nCurrent Customer Name: {id_search_results[1]}\n")
        print('Enter new customer name:')
        name_field =input()
        name_update = 'UPDATE Customers SET name=? WHERE customer_id=?'

        cursor.execute(name_update, (name_field, str(id_search_results[0])))
        print(f"\nNew Customer Name: {name_field}")


        
    if user_input == "a":
        print(f"\nCurrent Customer Address: {id_search_results[2]}\n")
        print('Enter New Customer Address:')
        address_field =input()
        address_update = 'UPDATE Customers SET street_address=? WHERE customer_id=?'

        cursor.execute(address_update, (address_field, str(id_search_results[0])))
        print(f"\nNew Customer Address: {address_field}")

    if user_input == "c":
        print(f"\nCurrent Customer City: {id_search_results[3]}\n")
        print('Enter New Customer City:')
        city_field =input()
        city_update = 'UPDATE Customers SET city=? WHERE customer_id=?'

        cursor.execute(city_update, (city_field, str(id_search_results[0])))
        print(f"\nNew Customer City: {city_field}")

    if user_input == "s":
        print(f"\nCurrent Customer State: {id_search_results[4]}\n")
        print('Enter New Customer State:')
        state_field =input()
        state_update = 'UPDATE Customers SET state=? WHERE customer_id=?'

        cursor.execute(state_update, (state_field, str(id_search_results[0])))
        print(f"\nNew Customer State: {state_field}")


    if user_input == "z":
        print(f"\nCurrent Customer Zipcode: {id_search_results[5]}\n")
        print('Enter New Customer Zipcode:')
        zipcode_field =input()
        zipcode_update = 'UPDATE Customers SET postal_code=? WHERE customer_id=?'

        cursor.execute(zipcode_update, (zipcode_field, str(id_search_results[0])))
        print(f"\nNew Customer State: {zipcode_field}")
    
    if user_input == "p":
        print(f"\nCurrent Customer Phone: {id_search_results[6]}\n")
        print('Enter New Customer Phone:')
        phone_field =input()
        phone_update = 'UPDATE Customers SET phone=? WHERE customer_id=?'

        cursor.execute(phone_update, (phone_field, str(id_search_results[0])))
        print(f"\nNew Customer State: {phone_field}")

    if user_input == "e":
        print(f"\nCurrent Customer Email: {id_search_results[7]}\n")
        print('Enter New Customer Email:')
        email_field =input()
        email_update = 'UPDATE Customers SET email=? WHERE customer_id=?'

        cursor.execute(email_update, (email_field, str(id_search_results[0])))
        print(f"\nNew Customer State: {email_field}")


    conn.commit()


def delete_customer(customer_id):
    
    customer_data = cursor.execute("SELECT customer_id, name FROM Customers WHERE customer_id = ?", (customer_id,)).fetchone()
    # print(customer_data[1])

    print(f'Are you SURE you want to DELETE {customer_data[0]}:"{customer_data[1]}" (y/n)?')
    customer_answer = input()

    if customer_answer == 'y':
        print(f'\n"SUCCESS: Customer {customer_data[1]} succesfully Deleted!"')

        cursor.execute('DELETE FROM Customers WHERE customer_id = ?', (customer_id,)).fetchone()


    conn.commit()


    
while True:

    customer_menu()
    user_input = input()

    if user_input == "1":
        get_all_customers()
        while True:
            print("\nEnter a Customer ID to View a Customer:")
            print("Press 'Enter' to return to Main Menu")
            customer_answer = input()
            if customer_answer == '':
                break
            else:
                results = search_customer(customer_answer)
                customer_detail(results)

                print("To update a field, enter the first letter of the field.")
                print("To delete this record, type 'DELETE'.")
                print("To return to the main menu, press 'Enter'.")
                user_input = input(">>> ")

                if user_input == 'delete':
                    delete_customer(results[0])
                    break
                if customer_answer == '':
                    break
                else:
                    update_customer(results[0], user_input)
                    break

    if user_input == '2':
        while True:
            print("\nEnter a Customer ID to View a Customer:")
            print("Press 'Enter' to return to Main Menu")
            customer_answer = input()
            if customer_answer == '':
                break
            results = search_customer(customer_answer)
            customer_detail(results)


    



