n=int(input("Enter a number"))
sum=0
a=n
while n>0:
    r=n%10
    sum=sum+r**3
    n=n//10
if sum==a:    
    print("Armstrong")
else:
    print("Not Armstrong")
