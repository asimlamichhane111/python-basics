def replacing(countries):
    for i in range(len(countries)):
        countries[i]=countries[i].replace('a','e')
        return countries
countries=['Argentina','Zimbawe','Uganda','Slovakia']
print(replacing(countries))



