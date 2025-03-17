import pandas as pd

# we use read.excel() to generate a pandas dataframe corresponding to the specified Excel file
df = pd.read_excel("uploads\\Data Finish Goods.xlsx", sheet_name=2, usecols="N:P", header=None).fillna(method="ffill", axis=1)[5:9]
dict_df = df.to_dict()
print(dict_df)