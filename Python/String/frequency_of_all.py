word=input('Enter a word')
mylist=[]
for x in word:
    if x not in mylist:
        mylist.append(x)
for x in mylist:
    print(x,':',word.count(x))
