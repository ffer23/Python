"""
CALCULADORA IMC UTILIZANDO BANCO DE DADOS
"""

# -*- coding: utf-8 -*-

import sqlite3

# Cria conexão e cursor
con = sqlite3.connect('cliente.db')
cur = con.cursor()

nome = input("Nome: ")
end = input("Endereço: ")
peso = float(input("Peso(kg): "))
altura = float(input("Altura(cm): "))
res = 0.0
analise = ''


def calcular():
    global peso
    global altura
    altura = altura/100
    global res
    res = peso / (altura * altura)


calcular()

if res < 17:
    analise = "Muito abaixo do peso"
elif 17 <= res < 18.49:
    analise = "Abaixo do peso"
elif 18.50 <= res < 24.99:
    analise = "Peso normal"
elif 25 <= res < 29.99:
    analise = "Acima do peso"
elif 30 <= res < 34.99:
    analise = "Obesidade I"
elif 35 <= res < 39.99:
    analise = "Obesidade II (severa)"
else:
    analise = "Obesidade III (mórbida)"


print('Nome: %s | Endereço: %s | Peso: %.2f | Altura: %.2f | IMC: %.2f | %s' % (nome, end, peso, altura, res, analise))

# Sentença SQL para inserir registros
sql = 'insert into cliente values (null, ?, ?, ?, ?, ?, ?)'

# Dados
recset = [(nome, end, peso, altura, res, analise)]

# Insere os registros
for rec in recset:
    cur.execute(sql, rec)

# Confirma a transação
con.commit()

# Fecha a conexão
con.close()
