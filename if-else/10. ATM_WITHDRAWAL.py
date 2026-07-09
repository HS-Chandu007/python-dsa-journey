
# PROBLEM: Mini Decision Challenge (ATM Withdrawal)

withdrawal_amount = int(input('Enter withdraw Amount: '))
account_balance = 500

if withdrawal_amount > 0:
    
    if account_balance < withdrawal_amount:
        print('Insufficient Balance')
    elif withdrawal_amount % 100 != 0:
        print('Invalid Amount')
    else:
        print('Transaction successfull')
else:
    print('Enter a postivie number')