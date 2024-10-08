class AgeError(Exception):
    def __init__(self,msg):
        super().__init__(msg)
eligibleage=18
actualage=int(input('Enter your age'))
try:
    if actualage<eligibleage:
        raise AgeError('Not Eligible to vote')
    else:
        print('Eligible to vote')
except AgeError as ae:
    print(ae)
