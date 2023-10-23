# Amostragem Sistemática
    # Ex.:Tenho uma população com 12 dados e vou pegar a amostra a partir do 2 de 3 em 3:

import numpy as np
import pandas

populacao = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
tamanho_populacao = len(populacao)

# for i in range(1, tamanho_populacao, 3):
#     print(i)

# Salvando a amostra como uma nova lista:

amostra_sistematica_exemplo = []

for i in range(1, tamanho_populacao, 3):
    amostra_sistematica_exemplo.append(populacao[i])

print(amostra_sistematica_exemplo)

# Para calcularmos uma amostra sistemática no pandas, a lógica é a mesma. Vamos utilizar os índices do pandas para filtrar somente as posições que queremos:
df = pandas.DataFrame(populacao, columns= ["values"])
df

np.arange(1, 12, step = 3) # arange - função do numpy para pegar como arrayß

def amostragem_sistematica(df, inicio = 0, step = 3): #Recebe como parametro o DataFrame, o valor de início e o passo (3 em 3)
    indexes = np.arange(inicio, df.shape[0], step=step) # Um array com o valor de inicio, tamanho do DataFrame e o passo (step)
    amostra = df.iloc[indexes] # Amostra seria o DataFrame pegando apenas os indices que eu quero
    return amostra

print(amostragem_sistematica(df, 1, 3))


