
s=1
for i in range(10,-1,-2):
    for k in range(1,s+1):
        print(end='  ')
    for j in range(0,i+1):
        print('*',end=' ')
    print()
    s+=1
    
