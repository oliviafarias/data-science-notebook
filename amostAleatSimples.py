from random import sample
import pandas 

populacao = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# # Amostra Aleatória Simples - sample(nome da lista, tamanho da amostra)

# print(sample(populacao, 4))
# print(sample(populacao, 4))
# print(sample(populacao, 4))
# print(sample(populacao, 4))

# Mas, geralmente trabalhamos com alguma base de dados.

# import pandas as pd

df = pandas.DataFrame(populacao, columns= ["values"])
df

# print(df.sample(n = 4))

# Ao invés de passar o tamanho da amostra que queremos apra o Pandas, podemos passar a proporção do todo que queremos:
# Quero 1/3 de todos os dados

print(df.sample(frac = 0.33))

