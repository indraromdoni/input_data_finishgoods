import psycopg2

conn = psycopg2.connect(host="192.168.25.208", 
                        port=5436, 
                        database="finish_goods", 
                        user="postgres",
                        password="Postgre@sql1")

cur = conn.cursor()
cmd = "SELECT * FROM balance_stock_ingot ORDER BY no DESC LIMIT 100"
res = cur.execute(cmd)
data = cur.fetchall()
print(res)
print(data[0][8])