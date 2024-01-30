"""

Hello and Welcome to the Bank of Python

Please select from the following menu options: 
(B)alance
(D)eposit
(W)ithdraw
(Q)uit
d
How Much Would You Like to Deposit? 500
You have deposited $500.00

- - - - - - - - - - - - - - - - - - - - - - - - - - - -

Please select from the following menu options: 
(B)alance
(D)eposit
(W)ithdraw
(Q)uit
d
How Much Would You Like to Deposit? 1000
You have deposited $1000.00

- - - - - - - - - - - - - - - - - - - - - - - - - - - -

Please select from the following menu options: 
(B)alance
(D)eposit
(W)ithdraw
(Q)uit
w
How much would you like to withdraw? (0 to cancel): $40
Please take your $40.00. You balance is now $960.00

- - - - - - - - - - - - - - - - - - - - - - - - - - - -

Please select from the following menu options: 
(B)alance
(D)eposit
(W)ithdraw
(Q)uit
w
How much would you like to withdraw? (0 to cancel): $1000
This amount exceeds your balance of $960.00
How much would you like to withdraw? (0 to cancel): $0

- - - - - - - - - - - - - - - - - - - - - - - - - - - -

Please select from the following menu options: 
(B)alance
(D)eposit
(W)ithdraw
(Q)uit
q

Goodbye. Please come again


"""

def atm_bank():
    print("Hello and Welcome to the Bank of Python!\n")
    user_balance = 500

    def balance(user_balance):
        print(f"Your current balance is ${user_balance:,.2f}\n")
 
    

    def deposit(user_balance):
        deposit_amount = int(input('Enter the amount you\'d like to deposit: \n'))
        new_total_amount = user_balance + deposit_amount
        print(f"Your current balance is ${new_total_amount:,.2f}\n")
        return new_total_amount


    def withdraw_amount(user_balance):
        withdraw_amount = int(input('Enter the amount you\'d like to withdraw: \n'))
        new_total_amount = user_balance - withdraw_amount
        print(f"Your current balance is ${new_total_amount:,.2f}\n")
        return new_total_amount



    while True:
        print('Please select from the following menu options:\n (B)alance\n','(D)eposit\n','(W)ithdraw\n','(Q)uit\n')
        users_input = input()

        if users_input.lower() == 'b':
            balance(user_balance)
        elif users_input.lower() == 'd':
            user_balance = deposit(user_balance)
        elif users_input.lower() == 'w':
            user_balance = withdraw_amount(user_balance)
        elif users_input.lower() == 'q':
            return 'Goodbye. Please come again'
        

print(atm_bank())
      

"""
SUDO:
- Already have balance func
- Deposit: func (not working yet)
    - Paramaters -> Balance
        - Balance will be an integer

    - Users input -> Deposit 
        - Initally deposit will be a string

    - Balance + deposit = new total amount 
    - Reassign balance so that it's updating

- Withdraw:
    - Paramaters -> Balance
        - Balance will be an integer

    - Users input -> Deposit 
        - Initally deposit will be a string

    - Balance - withdraw anount = new total amount
    - Reassign balance so that it's updating

"""



