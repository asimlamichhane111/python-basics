w='KATHMANDU'
s=5
for i in range(0,9,2):
    for k in range(1,s+1):
        print(end='  ')
    for j in range(0,i+1):
        print(w[j],end=' ')
    print()
    s-=1
    
