import pandas as pd

df = pd.read_csv("Results 2016-2019.csv")
df['zip_code']=df['zip_code'].astype(int)
cn = df.groupby(['zip_code', 'item_description', 'store_number'])
cn=cn.agg({'bottles_sold': 'sum', 'sale_dollars': 'sum'})
cn.to_csv("Final_Table.csv")