n=int(input("Enter a number"))
sum=0
a=n
while n>0:
    r=n%10
    sum=sum*10+r
    n=n//10
if sum==a:    
    print("Palindrome")
else:
    print("Not a Palindome")
