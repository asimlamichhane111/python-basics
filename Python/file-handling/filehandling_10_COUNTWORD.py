#to input a word and count how many times it occurs in a file "xyz.txt"
count=0
word=(input("Enter a word:"))
f=open("xyz.txt","r")
text=f.read().split()
for w in text:
    if w==word:
        count+=1
print(count)
f.close()
