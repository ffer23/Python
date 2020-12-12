"""
CALCULADORA IMC UTILIZANDO BANCO DE DADOS
"""

# -*- coding: utf-8 -*-

import sqlite3

# Cria conexão e cursor
con = sqlite3.connect('cliente.db')
cur = con.cursor()

# Seleciona todos os registros
cur.execute('select * from cliente')

# Recupera Resultados
recset = cur.fetchall()

# Mostra
for rec in recset:
    print('%d  |  %s  |  %s  |  %.2f  |  %.2f  |  %.2f  |  %s' % rec)

# Fecha a conexão
con.close()
