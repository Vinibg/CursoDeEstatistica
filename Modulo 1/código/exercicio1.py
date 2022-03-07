from operator import le
from posixpath import split
from tokenize import group
import pandas as pd
import random
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit


#Amostra aleatória
def amostragem_simples(dataset,amostras):
    #df_amaostra_aleatoria_simples = dataset.sample(n =100) #Primeira amostagem
    #df_amaostra_aleatoria_simples = dataset.sample(n =100, replace=False) # Linhas repitidas não aparecem
    return dataset.sample(n = amostras, random_state=1) #Retorna a mesma amostragem selecionada

####

###Amostragem sistemática
def amostragem_sistematica(dataset, amostras):
    intervalo = len (dataset) // amostras
    random.seed(1)
    inicio = random.randint(0,intervalo)
    indices = np.arange(inicio, len(dataset), step=intervalo)
    amostra_sistematica= dataset.iloc[indices]
    return amostra_sistematica
#####

###Amostragem por grupos
def amostragem_por_grupos(dataset, numero_grupos):
    intervalo = len(dataset) / numero_grupos
    grupos = []
    id_grupo = 0
    contagem = 0

    for _ in dataset.iterrows():
        grupos.append(id_grupo)
        contagem += 1
        if contagem > intervalo :
            contagem=0
            id_grupo += 1
        
    dataset['grupo'] = grupos
    grupos_selecionados = random.randint(0, numero_grupos)
    return dataset[dataset['grupo'] == grupos_selecionados]
###

#Amostra especificada
def amostra_estratifica(dataset, percentual,campo):
    #dataset['income']
    split = StratifiedShuffleSplit(test_size= percentual, random_state=1)

    for _,y in split.split(dataset, dataset[campo]):
        df_y = dataset.iloc[y]

    return df_y
###

###Amostra de reservatório
def amostragem_reservatorio(dataset, amostras):
    stream = []
    for i in range(len(dataset)):
        stream.append(i)

    i=0
    tamanho = len(dataset)
    reservatorio = [0] * amostras

    for i in range(amostras):
        reservatorio[i] = stream[i]

    while i < tamanho:
        j = random.randrange(i + 1)
        if j < amostras:
            reservatorio[j] = stream[i]
        i+=1

    return dataset.iloc[reservatorio]



###

dataset = pd.read_csv('/home/vinicius/Área de Trabalho/CursoDeEstatistica/Modulo 1/código/credit_data.csv')
print(dataset.shape)
df_amostrage_simples = amostragem_simples(dataset, 1000)
df_amostra_sistematica = amostragem_sistematica(dataset,1000)
df_amostragem_por_grupos = amostragem_por_grupos(dataset, 2)
df_amostra_estratifica = amostra_estratifica(dataset,0.5, "c#default")
df_amostragem_reservatorio = amostragem_reservatorio(dataset, 1000)

print(df_amostrage_simples.shape)
#print("Age:", df_amostrage_simples['age'].mean()," Income: ", df_amostrage_simples['income'].mean()," Loan: ", df_amostrage_simples['loan'].mean())
#print("Age:", df_amostra_sistematica['age'].mean()," Income: ", df_amostra_sistematica['income'].mean()," Loan: ", df_amostra_sistematica['loan'].mean())
#print("Age:", df_amostragem_por_grupos['age'].mean()," Income: ", df_amostragem_por_grupos['income'].mean()," Loan: ", df_amostragem_por_grupos['loan'].mean())
#print("Age:", df_amostrage_simples['age'].mean()," Income: ", df_amostrage_simples['income'].mean()," Loan: ", df_amostrage_simples['loan'].mean())
#print("Age:", df_amostragem_reservatorio['age'].mean()," Income: ", df_amostragem_reservatorio['income'].mean()," Loan: ", df_amostragem_reservatorio['loan'].mean())