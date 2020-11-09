"""
1)	Faça um programa que leia a idade de uma pessoa expressa em dias e mostre-a expressa em anos, meses e dias.
"""
#!/usr/bin/env python
# -*- coding: latin1 -*-

idade_dias = int(input('Informe sua idade em dias: '))
idade_anos = idade_dias / 365
idade_dias = idade_dias % 365
idade_meses = idade_dias / 30
idade_dias = idade_dias % 30

print(f'Sua idade é de {int(idade_anos)} ano(s), '
      f'{int(idade_meses)} mes(es) e '
      f'{int(idade_dias)} dia(s)')
