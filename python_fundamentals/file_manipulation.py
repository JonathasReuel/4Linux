#!/usr/bin/python3

try:
	with open('nome','x') as f:
		f.write('\tOlá\n')

except FileExistsError as e:
	with open('nome2','w') as f:
		f.write('\tOlá\n\toi\n\n{}'.format(e))

f = open('teste.txt','w')
f.write('Curso Python')
f.close()