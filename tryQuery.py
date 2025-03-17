import pandas as pd

def update_data():
    print("Updating data!")
    print("\r")
    print("Update balance!")
    balance_data = pd.read_excel("uploads\\Data Finish Goods.xlsx", sheet_name=0)
    balance_dict = balance_data.to_dict()
    for i in balance_dict['BegBal']:
        cmd1 = f"UPDATE balance_stock_ingot SET begbal={balance_dict['BegBal'][i]}, incoming={balance_dict['Incoming'][i]}, delivery={balance_dict['Delivery'][i]}, qty_stock={balance_dict['Qty. Stock'][i]}, mapi={balance_dict['MAPI'][i]}, jti={balance_dict['JTI'][i]} WHERE nama_produk='{balance_dict['Nama Produk'][i]}';"
        print(cmd1)
    print("\r")

    print("Update schedule!")
    customer_data = pd.read_excel("uploads\\Data Finish Goods.xlsx", sheet_name=1, usecols=(0,))
    customer_dict = customer_data.to_dict()
    tgl_data = pd.read_excel("uploads\\Data Finish Goods.xlsx", sheet_name=1, usecols='K:AO')
    tgl_data.fillna(0)
    tgl_dict = tgl_data.to_dict()
    kete_data = pd.read_excel("uploads\\Data Finish Goods.xlsx", sheet_name=1, usecols='AP')
    kete_data.fillna(0)
    kete_dict = kete_data.to_dict()
    for cus in customer_dict['Customer ']:
        for tgl in tgl_dict.keys():
            if tgl_dict[tgl][cus] != 0:
                cmd2 = f"INSERT INTO schedule_delivery(customer, tgl, qty, remarks) VALUES ({customer_dict['Customer '][cus]}, {tgl}, {tgl_dict[tgl][cus]}, {kete_dict['Keterangan'][cus]});"
                print(cmd2)
    print("\r")

    print("Update peta!")
    peta_data = pd.read_excel("uploads\\Data Finish Goods.xlsx", sheet_name=2, usecols="A", header=None).ffill(axis=1)[5:9]
    peta_dict = peta_data.to_dict()
    print(peta_dict)

update_data()