print('1.add /n 2.sub /n 3.mul /n 4.div')
choice=int(input('Enter your choice'))
if choice>4:
    print('Invalid choice')
else:
    a=int(input('Enter the 1st number'))
    b=int(input('Enter the 2nd number'))
    match choice:
          case 1:
              print('Sum is: ',(a+b))
          case 2:
              print('Difference is: ',(a+b))
          case 3:
              print('Product is: ',(a+b))
          case 4:
              print('Quotient is: ',(a+b))
     
