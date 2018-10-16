#!/usr/bin/python3

nomes = ['jonathas','douglas','durvalina','geronimo']

s = input('buscar por nome: ')

for nome in nomes:
	if s == nome:
		print('esta na lista')
		break
else:
	print('nao esta na lista')