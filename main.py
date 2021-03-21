operation = input('Welcome to the SG Banking\n'
                  '1:Take Money\n'
                  '2:Put Money\n'
                  '3:Money Transfer\n'
                  'Q:Quitting\n')

if operation == '1':
    balance = int(input('How much money do you have in your account?: '))
    money = int(input('How much money do you want to take out of your account?: '))

    if balance < money:
        print('You do not have the sufficient funds to process this transaction')
    else:
        print('Your remaining balance is: ', '£', (balance - money))

elif operation == '2':
    balance = int(input('How much money do you have in your account?: '))
    money = int(input('How much money do you want to deposit into your account?: '))
    print('Your new balance is: ', '£', (balance + money))

elif operation == '3':
    balance = int(input('How much money do you have in your account?: '))
    transfer = int(input('How much money will you transfer? '))
    if balance > transfer:
        print('You transfered ', '£', transfer, )
        print('Your remaining balance is ', '£', (balance - transfer))
    elif balance < transfer:
        print('There is not enough money in your account for this transfer\n'
              'Your balance is £', balance)
