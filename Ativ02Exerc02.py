"""
2)	Elaborar um programa que lê 3 valores a,b,c e verifica se eles formam ou não um triângulo.
Supor que os valores lidos são inteiros e positivos.
Caso os valores formem um triângulo, calcular e escrever a área deste triângulo.
Se não formam triângulo escrever os valores lidos.
(Se a > b + c não formam triângulo algum, se a é o maior).

Usei a fórmula de Heron (Teorema de Herão) para calcular a área, visto que não temos a informação
da altura do triângulo e essa fórmula serve para qualquer triângulo.

"""
#!/usr/bin/env python
# -*- coding: latin1 -*-

import math

a = int(input('Informe o valor de a em cm: '))
b = int(input('Informe o valor de b em cm: '))
c = int(input('Informe o valor de c em cm: '))

p = (a + b + c) / 2
area = p * (p - a) * (p - b) * (p - c)

if area > 0:
    print('A área do triangulo é de %.2f centímetros quadrados' % (math.sqrt(area)))
else:
    print('Não forma triângulo!')
    print(f'a = {a}, b = {b}, c = {c}')
