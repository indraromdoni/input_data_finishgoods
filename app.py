from flask import Flask, render_template, Response, request, flash, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import psycopg2
import pandas as pd
import os

upload_folder = "uploads"
allowed_file = {'xlsx', 'xls'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = upload_folder

'''@app.route('/')
def index():
    return render_template('index.html')'''

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        print(file.filename)
        file.save("uploads/" + file.filename)
        update_data()
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form><br>
    <a href="download">
        <button>Download excel template</button>
    </a>
    '''
@app.route('/download', methods=['GET', 'POST'])
def download_file():
    print("Download File")
    return send_from_directory(app.root_path, "uploads\Data Finish Goods.xlsx")

def update_data():
    print("Updating data!")
    print("\r")
    print("Update balance!")
    balance_data = pd.read_excel("uploads\\Data Finish Goods.xlsx", sheet_name=0)
    balance_dict = balance_data.to_dict()
    for i in balance_dict['BegBal']:
        cmd1 = f"UPDATE balance_stock_ingot SET begbal={balance_dict['BegBal'][i]}, incoming={balance_dict['Incoming'][i]}, delivery={balance_dict['Delivery'][i]}, qty_stock={balance_dict['Qty. Stock'][i]}, mapi={balance_dict['MAPI'][i]}, jti={balance_dict['JTI'][i]} WHERE nama_produk='{balance_dict['Nama Produk'][i]}';"
        print(cmd1)
        postgre_patch(cmd1)
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
                cmd2 = f"INSERT INTO schedule_delivery(customer, tgl, qty, remarks) VALUES ('{customer_dict['Customer '][cus]}', TO_DATE('{tgl}','dd-mm-yyyy'), {tgl_dict[tgl][cus]}, '{kete_dict['Keterangan'][cus]}');"
                print(cmd2)
                postgre_patch(cmd2)
    print("\r")

    peta_data = pd.read_excel("uploads\\Data Finish Goods.xlsx", sheet_name=2)
    print(peta_data)

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

def main():
    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == "__main__":
    main()