#!/home/developer/Documentos/4Linux/python_fundamentals/venv/bin/python3
import psycopg2
from conta import Conta, Poupanca

try:
    con = psycopg2.connect('host=localhost dbname=projeto user=admin password=4linux')
    cur = con.cursor()
except Exception as e:
    print('Erro: {}'.format(e))
    exit()

#conta = Conta('Douglas Louvres',5030323,500554)

for i in range(100000):
    cur.execute("INSERT INTO conta(titular,saldo) VALUES ('{}',{})".format('Cliente ' + str(i),5000 + i))
    con.commit()

cur.execute("SELECT * FROM conta;")

lol = cur.fetchall()

for x in range(1,101):
    print(lol)

cur.close()
con.close()