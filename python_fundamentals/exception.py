#!/usr/bin/python3

convidados = ['douglas','lucas','joao']

try:
	pos = int(input('Digite posicao do convidado: '))
	print(convidados[pos - 1])

except ValueError:
	print('Apenas numeros')

except IndexError:
	print('A lista tem {} convidados'.format(len(convidados)))
	
except Exception as e:
	print(e)