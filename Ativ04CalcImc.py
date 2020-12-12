"""
Calculadora IMC utilizando Banco de Dados
"""

# -*- coding: utf-8 -*-

import sqlite3

# Cria conexão e cursor
con = sqlite3.connect('cliente.db')
cur = con.cursor()

# Cria Tabela
sql = 'create table cliente '\
    '(Código integer primary key, '\
    'Nome varchar(100),  '\
    'Endereço varchar (300), '\
    'Peso float, '\
    'Altura float, '\
    'IMC float, '\
    'Análise varchar(100))'
cur.execute(sql)

# Fecha Conexão
con.close()

print("Banco SQLite criado com sucesso")
