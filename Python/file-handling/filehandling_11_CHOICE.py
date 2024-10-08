#menudriven program (choice of  write,read,append)

a=int(input("Enter your choice:"))
if a==1:
    f=open("xyz.txt","w")
    f.write(input("Enter the text you wanna write"))
    f.close()
elif a==2:
    f=open("xyz.txt","r")
    print(f.read())
    f.close()
elif a==3:
    f=open("xyz.txt","a")
    f.write(input("Enter the text you wanna write"))
    f.close()
else:
    print("Invalid choice")



