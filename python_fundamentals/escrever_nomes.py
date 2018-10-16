#!/usr/bin/python3

nomes = ['yasmin','rafael','jessica']

with open('escrever_nomes.txt','w') as f:
	for row in nomes:
		f.write(row + '\n')