#OS module
import os
vowel=('a','e','i','o','u')
files =os.listdir("./")
for file in files:
    if file.startswith(vowel):
        print (file)
