#to write and then read
f=open("xyz.txt","w")
f.write("Chatur Ramalingam")
f.close()

f=open("xyz.txt","r")
print(f.read())
f.close()
