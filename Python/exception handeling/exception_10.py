#Index Error
countries=['Nepal','India','China','Japan','Russia']
i=int(input('Enter the index value'))
try:
    print('Country at index',i,'is',countries[i])
except IndexError as ie:
    print(ie)
