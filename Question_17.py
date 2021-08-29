# Write a program that computes the net amount of a bank account based a transaction log from console input. 
# The transaction log format is shown as following: D 100 \n W 200
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300 \n D 300 \n W 200 \n D 100
# Then, the output should be: 500

balance = 0

while True:
    user_input = input("Enter '1' to Deposit or Withdraw, '2' to check balance, '3' to Exit: ")
    if user_input == '1':
        transaction = input("Enter 'D -amount-' to Deposit, 'W -amount-' to Withdraw: ").split(' ')
        if transaction[0].lower() == 'd':
            balance += int(transaction[1])
            print('Amount added.')
        elif transaction[0].lower() == 'w':
            if balance == 0:
                print("You don't have enough balance!")
            elif balance < int(transaction[1]):
                print('Your current balance is lower.')
            else:
                balance -= int(transaction[1])
                print('Amount Withdrawn.')
    elif user_input == '2':
        print('Current balance is - ', balance)
    elif user_input == '3':
        print('Thank you!')
        break



