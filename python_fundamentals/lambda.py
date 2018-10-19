#!/usr/bin/python3

#Primeiro exemplo de Lambda
for x in range(1,11):
    print((lambda x :  x ** 2)(x))

#Lambda com List Comprehension
quadrados = [(lambda x : x ** 2)(y) for y in range(1,11)]

print(quadrados)

del quadrados

#Map com lambda
quadrados = list(map(lambda x:x ** 2,range(1,11)))
print(quadrados)