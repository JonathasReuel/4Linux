#!/usr/bin/python3
from pymongo import MongoClient

try:
    con = MongoClient()  # Deve-se passar uma string de conexão, por padrão é o
    db = con['projeto']
except Exception as e:
    print("Erro: {}".format(e))
    exit()

#Atualizando registro do Mongo
db.conta.update({'_id':1},{"$set":{"titular":"Vacilao"}})

# Imprimir registros:
for registro in db.conta.find():
    print(registro)

# Imprimir registros com list comprehension
print([x for x in db.conta.find()])