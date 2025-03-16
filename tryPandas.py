import pandas as pd

# we use read.excel() to generate a pandas dataframe corresponding to the specified Excel file
df = pd.read_excel("Data Finish Goods.xlsx", sheet_name=0)

# this line prints the type of "df"; this is a class specific to pandas, known as a pandas dataframe
print(type(df))

# this lines prints the dataframe
print(df)