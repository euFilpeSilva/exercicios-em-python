# Uma amostra de gauchos foi investigada em relação ao consumo de sal diario, obtendo se o seguinte:
# escreva em python uma lista com os valores mostrados acima e calcule:
# media aritmetica simples;
# media harmonica;
# media geometrica;
# moda;
# variancia;
# desvio padrão;


# RESOLUÇÃO:

amostras = [
 ('A',10),
 ('B', 13),
 ('C', 17),
 ('D', 9),
 ('E', 8),
 ('F', 11),
 ('G', 13),
 ('H', 7)
]

media = 0
for item in amostras:
 media += item[1]
print('A média é:',media/ len(amostras))

# //////////////////////////////////////////////////////////////

import statistics

amostras = [10,13,17,9,8,11,13,7]
print('A media harmonica é:',statistics.harmonic_mean(amostras))

# amostras = [
#  ('A',10),
#  ('B', 13),
#  ('C', 17),
#  ('D', 9),
#  ('E', 8),
#  ('F', 11),
#  ('G', 13),
#  ('H', 7)
# ]

# media = 0
# for item in amostras:
#  media += item[1]
# print('A média harmonica é:', len(amostras) / (1/10 + 1/13 + 1/17 + 1/9 + 1/8 + 1/11 + 1/13 + 1/7))

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////


import math
from scipy.stats.mstats import gmean

# amostras = [10,13,17,9,8,11,13,7]
# print('A media geometrica é:',gmean(amostras))

amostras = [
 ('A',10),
 ('B', 13),
 ('C', 17),
 ('D', 9),
 ('E', 8),
 ('F', 11),
 ('G', 13),
 ('H', 7)
]

media = 1
for item in amostras:
 media *= item[1]
print('A média geometrica é:',math.pow(media, 1/ len(amostras)) )

# /////////////////////////////////////////////////////////////////////////////////////////////

# Disciplina: Probabilidade estatistica
#Alunos:
#Lista 4

import math
from scipy.stats.mstats import gmean

# amostras = [10,13,17,9,8,11,13,7]
# print('A media geometrica é:',gmean(amostras))

amostras = [
 ('A',10),
 ('B', 13),
 ('C', 17),
 ('D', 9),
 ('E', 8),
 ('F', 11),
 ('G', 13),
 ('H', 7)
]

media = 1
for item in amostras:
 media *= item[1]
print('A média geometrica é:',math.pow(media, 1/ len(amostras)) )

# ///////////////////////////////////////////////////////////////////////////////

# Disciplina: Probabilidade estatistica
#Alunos:
#Lista 4 atividade 1

import statistics
from scipy.stats.mstats import gmean

amostras = [10,13,17,9,8,11,13,7]
print('A média da lista é:', statistics.mean(amostras))
print('A media harmonica é:',statistics.harmonic_mean(amostras))
print('A media geometrica é:',gmean(amostras))
print('A moda da lista é:',  statistics.mode(amostras))
print('A variância da lista é:', statistics.variance(amostras))
print('O desvio padrão da lista é:', statistics.stdev(amostras))

# //////////////////////////////////////////////////////////////////////////////////////////////////

#Disciplina: Probabilidade estatistica
#Alunos:
#Lista 4 atividade 2

import statistics
from scipy.stats.mstats import gmean

amostras = [67,75,63,72,77,78,81,77,80]

print('A média da lista é:', statistics.mean(amostras))
print('A media harmonica é:',statistics.harmonic_mean(amostras))
print('A media geometrica é:',gmean(amostras))
print('A moda da lista é:',  statistics.mode(amostras))
print('A variância da lista é:', statistics.variance(amostras))
print('O desvio padrão da lista é:', statistics.stdev(amostras))