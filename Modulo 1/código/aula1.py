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
def amostra_estratifica(dataset, percentual):
    #dataset['income']
    split = StratifiedShuffleSplit(test_size= percentual, random_state=1)

    for _,y in split.split(dataset, dataset['income']):
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

dataset = pd.read_csv('/home/vinicius/Área de Trabalho/CursoDeEstatistica/Modulo 1/código/census.csv')




#amostragem_por_grupos(dataset,100)
#amostra_estratifica(dataset,0.003071)
#am = amostragem_reservatorio(dataset, 100)
#print(am.head())
#print (len(dataset)//10)
#print(amostragem_por_grupos(dataset,100))