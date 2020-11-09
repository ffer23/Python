"""
5)	Escreva uma função que:
a)	Receba uma frase como parâmetro.
b)	Retorne uma nova frase com cada palavra com as letras invertidas.
"""
#!/usr/bin/env python
# -*- coding: latin1 -*-

frase = 'A gratidão é a memória do coração'
print(frase)
print('Escrevendo a frase ao contrário temos:')
print(frase[::-1])

frase2 = input('Agora tente você... escreva uma frase: ')
print('Sua frase ao contrário fica assim:')
print(frase2[::-1])

res = input('Se você gostou digite sim, e se não gostou digite não: ')
if res == 'sim':
    print('Fico feliz que tenha gostado!', '\U0001F60A' * 3)
else:
    print('Que pena que não gostou!', '\U0001F631' * 3)
