import pandas as pd
df=pd.read_excel('something.xlsx')
df1=df.drop_duplicates()
df1=df.dropna()
print(df1.loc[:,['Name','Salary']])
