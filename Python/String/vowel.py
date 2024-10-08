word=input('Enter a word')
count=0
for x in word:
    if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
        count+=1
print("No. of vowels = ",count)
