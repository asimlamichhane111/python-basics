n=int(input("Enter a number"))
count1=0
count2=0
while n>0:
    r=n%10
    if (r==1):
        count1+=1
    elif(r==2):
        count2+=1
    n=n//10
if(count1==count2):    
    print("Good number")
else:
    print("Not a good number")
    

