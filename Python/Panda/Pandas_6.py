import pandas as pd
df=pd.read_excel('something.xlsx')
df1=df.drop_duplicates()
print(df1)
