nvezes = 0
p = 'você'

with open('casmurro.txt', encoding='utf8') as livro:
    linhas = livro.read()

import re
from collections import Counter

palavras = linhas.split()
tamanho = len(palavras)
print("O texto tem : " + str(tamanho) + " palavras")

palavras = linhas.split('você')
tamanho = len(palavras)
print("O texto tem : " + str(tamanho) + ' "vocês"')



