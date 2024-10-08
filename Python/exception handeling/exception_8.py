class InsufficientBalanceError(Exception):
    def __init__(self,msg):
        super().__init__(msg)
balance=int(input('Enter balance amount'))
amount=int(input('Enter withdraw amount'))
try:
    if amount>balance:
        raise InsufficientBalanceError('Not Enough Balance')
    else:
        print('Going to Withdraw')
        balance=balance-amount
        print('Withdraw Amount= ',amount)
        print('Balance after Withdraw=',balance)
        print('Withdraw Successful')
except InsufficientBalanceError as ie:
    print(ie)
