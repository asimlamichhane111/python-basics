a=int(input('Enter the first number'))
b=int(input('Enter the second number'))
try:
    c=a+b
    print('Result=',c)
except ValueError as ve:
    print(ve)
else:
    print('Success')
