import psycopg2
import pandas as pd

def postgre_patch(cmd: str):
    conn = psycopg2.connect(host="192.168.25.208", 
                        port=5436, 
                        database="finish_goods", 
                        user="postgres",
                        password="Postgre@sql1")

    cur = conn.cursor()
    res = cur.execute(cmd)
    conn.commit()
    cur.close()
    conn.close()

balance_data = pd.read_excel("uploads\\Data Finish Goods.xlsx", sheet_name=0)
balance_dict = balance_data.to_dict()
for i in balance_dict['BegBal']:
    #cmd1 = f"UPDATE balance_stock_ingot SET begbal={balance_dict['BegBal'][i]}, incoming={balance_dict['Incoming'][i]}, delivery={balance_dict['Delivery'][i]}, qty_stock={balance_dict['Qty. Stock'][i]}, mapi={balance_dict['MAPI'][i]}, jti={balance_dict['JTI'][i]} WHERE nama_produk='{balance_dict['Nama Produk'][i]}';"
    cmd1 = f"INSERT INTO public.balance_stock_ingot(nama_produk, begbal, incoming, delivery, qty_stock, mapi, jti) VALUES ('{balance_dict['Nama Produk'][i]}', {balance_dict['BegBal'][i]}, {balance_dict['Incoming'][i]}, {balance_dict['Delivery'][i]}, {balance_dict['Qty. Stock'][i]}, {balance_dict['MAPI'][i]}, {balance_dict['JTI'][i]});"
    print(cmd1)
    postgre_patch(cmd1)