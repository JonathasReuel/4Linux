#!/usr/bin/python3

n1 = float(input('Digite a primeira nota do aluno:\n'))
n2 = float(input('Digite a segunda nota do aluno:\n'))
n3 = float(input('Digite a terceira nota do aluno:\n'))
n4 = float(input('Digite a quarta nota do aluno:\n'))

media = ((n1*2) + (n2*3) + (n3*4) + (n4*1))/4

print('Média: %s\n' % (media))

if media >= 7.0:
	print('Aluno aprovado!')
elif media < 5.0:
	print('Aluno reprovado!')
elif media >= 5.0:
	print('Aluno em exame!')
	exame = float(input('Insira a nota do exame:'))
	print('Nota do exame: %s\n' % (exame))
	media = (media + exame) / 2
	if media >= 5.0:
		print('Aluno Aprovado!')
	else:
		print('Aluno Reprovado!')
	print('Média final: %s' % (media))