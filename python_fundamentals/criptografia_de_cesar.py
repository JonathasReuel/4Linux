#!/usr/bin/python3

import sys

alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','x','z']
tam = len(alfabeto) - 1

def criptografar(message, quantidade):
	nova_palavra = ''
	for i in message:
		if (alfabeto.index(i) + quantidade) > tam:
			j = (alfabeto.index(i) + quantidade) - tam
			nova_palavra += alfabeto[j]
		else:
			nova_palavra += alfabeto[alfabeto.index(i) + quantidade]

	return print('Palavra Criptografada: %s' % nova_palavra)

def decriptografar(message, quantidade):
	nova_palavra = ''
	for i in message:
		if (alfabeto.index(i) - quantidade) < 0:
			j = tam + (alfabeto.index(i) - quantidade)
			nova_palavra += alfabeto[j]
		elif (alfabeto.index(i) - quantidade) == 0:
			nova_palavra += alfabeto[0]
		else:
			nova_palavra += alfabeto[alfabeto.index(i) - quantidade]
	return print('Palavra Decriptografada: %s' % nova_palavra)

def main():
	if len(sys.argv) == 1:
		print('''O script requer dois parâmetros obrigatórios:
				\n-criptografar/decriptografar e a palavra para criptografia/decriptografia.
				\nTambém pode ser utilizado o parâmetro opcional de quantidade de letras
				\npara utilizar nos processos criptográficos.''')
	else:
		command = sys.argv[1].lower()
		message = sys.argv[2].lower()

		if len(sys.argv) < 4:
			qtd = 3
		else:
			qtd = int(sys.argv[3])

		comandos = {'criptografar':criptografar,'decriptografar':decriptografar}

		try:
			comandos[command](message,qtd)
		except KeyError as e:
			print('Chave errada: {}'.format(e))


if __name__ == '__main__':
	main()