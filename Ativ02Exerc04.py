"""
4)	Implementar uma função que retorne verdadeiro se o número for primo (falso caso contrário). Testar de 1 a 100.
"""
#!/usr/bin/env python
# -*- coding: latin1 -*-

def primos(numero):
    divisores = 0
    if numero == 1:
        print(f'{numero}: Falso')
    else:
        for divisor in range(1, numero):
            if numero % divisor == 0:
                divisores = divisores + 1
                if divisores > 1:
                    break
        if divisores > 1:
            print(f'{numero}: Falso')
        else:
            print(f'{numero}: Verdadeiro -> é número primo')


for numero in range(1, 101):
    primos(numero)
