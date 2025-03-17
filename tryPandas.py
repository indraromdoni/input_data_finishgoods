import pandas as pd

# we use read.excel() to generate a pandas dataframe corresponding to the specified Excel file
df = pd.read_excel("Data Finish Goods.xlsx", sheet_name=0)
dict_df = df.to_dict()
print(dict_df['Nama Produk'])