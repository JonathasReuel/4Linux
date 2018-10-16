#!/usr/bin/python3

import sys

alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','x','z']
tam = len(alfabeto) - 1

def criptografar(message):
	nova_palavra = ''
	for i in message:
		if (alfabeto.index(i) + 3) > tam:
			j = (alfabeto.index(i) + 3) - tam
			nova_palavra += alfabeto[j]
		else:
			nova_palavra += alfabeto[alfabeto.index(i) + 3]

	return print(nova_palavra)

def decriptografar(message):
	nova_palavra = ''
	for i in message:
		if (alfabeto.index(i) - 3) <= 0:
			j = tam + (alfabeto.index(i) - 3)
			nova_palavra += alfabeto[j]
		else:
			nova_palavra += alfabeto[alfabeto.index(i) - 3]
	return print(nova_palavra)

def main():
	command = sys.argv[1].lower()
	message = sys.argv[2].lower()
	if command == 'criptografar':
		criptografar(message)
	elif command == 'decriptografar':
		decriptografar(message)
	else:
		print('Comando não reconhecido!')

if __name__ == '__main__':
	main()