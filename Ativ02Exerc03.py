"""
3)	Faça um programa que leia 3 números inteiros e mostre o menor deles.
"""
#!/usr/bin/env python
# -*- coding: latin1 -*-

a = int(input('Informe um número inteiro: '))
b = int(input('Informe um número inteiro: '))
c = int(input('Informe um número inteiro: '))

if a < b and a < c:
    menor = a
elif b < a and b < c:
    menor = b
else:
    menor = c
print(f'O menor número digitado foi: {menor}')
