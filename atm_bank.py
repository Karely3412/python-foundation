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

    def balance():
        user_balance = 500
        view_balance = print(f"Your current balance is ${user_balance:.2f}")
        return view_balance
    

    def deposit(depo_amou):
        deposit_amount = input('Enter the amount you\'d like to deposit: ')
        new_total_amount = depo_amou + int(deposit_amount)
        view_new_balance = print(f"Your current balance is ${new_total_amount:.2f}")
        return view_new_balance



    while True:
        print('Please select from the following menu options:\n (B)alance\n','(D)eposit\n','(W)ithdraw\n','(Q)uit\n')
        users_input = input()

        if users_input.lower() == 'b':
           user_balance = balance()
        elif users_input.lower() == 'd':
            deposit(user_balance)
        elif users_input.lower() == 'w':
            print('balance test')
        elif users_input.lower() == 'q':
            return 'Goodbye. Please come again'
        




print(atm_bank())
      





