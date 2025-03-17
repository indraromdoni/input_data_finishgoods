from flask import Flask, render_template, Response, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
import psycopg2
import pandas as pd

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
    </form>
    '''
def update_data():
    print("Updating data!")
    balance_data = pd.read_excel("uploads\\Data Finish Goods.xlsx", sheet_name=0)
    balance_dict = balance_data.to_dict()
    print(balance_dict)

    delivery_data = pd.read_excel("uploads\\Data Finish Goods.xlsx", sheet_name=1)
    delivery_dict = delivery_data.to_dict()
    print(delivery_dict)

    peta_data = pd.read_excel("uploads\\Data Finish Goods.xlsx", sheet_name=2)
    print(peta_data)

def postgre_patch():
    conn = psycopg2.connect(host="192.168.25.208", 
                        port=5436, 
                        database="finish_goods", 
                        user="postgres",
                        password="Postgre@sql1")

    cur = conn.cursor()
    cmd = "SELECT * FROM balance_stock_ingot ORDER BY no DESC LIMIT 100"
    res = cur.execute(cmd)
    data = cur.fetchall()

def main():
    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == "__main__":
    main()