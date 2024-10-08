x=int(input('Enter the marks in 1st subject'))
y=int(input('Enter the marks in 2nd subject'))
z=int(input('Enter the marks in 3rd subject'))
total=x+y+z
print('Total marks obtained',total)
percent=(total/300)*100
print('Percentage of marks obtained',percent)
if x>=50 and y>=50 and z>=50:
    print('Pass')
    if percent>=80:
        print('Distinction')
    elif percent>=60:
        print('First Division')
    else:
        print('Second Division')
else:
    print('Fail')
