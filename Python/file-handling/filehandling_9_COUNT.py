#to count no. of chracters and no. of vowels in a file "xyz.txt"
f=open("xyz.txt","r")
txt=f.read()
print(len(txt))
vowel=['a','e','i','o','u']
count=0
for m in txt:
    if m in vowel:
        count+=1
        print(count)
f.close()
