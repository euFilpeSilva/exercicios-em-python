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