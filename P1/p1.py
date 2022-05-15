import pandas as pd

dataset = pd.read_csv("./happines_report_2022-1.csv")

#Os 10 países mais felizes
df_mais_felizes = dataset.sort_values(by='Happiness score',ascending=False).head(10)

#Os 10 países menos felizes
df_mais_felizes = dataset.sort_values(by='Happiness score',ascending=True).head(10)

# Os valores máximo e mínimo de Happines Score
df_happines_max = dataset["Happiness score"].max()
df_happines_min = dataset["Happiness score"].min()

#Explained by: Perceptions of corruption
#Para os valores de Percepção de Corrupção, extrair: contagem, média, desvio padrão, valor mínimo, valor máximo e valores do primeiro, segundo e terceiro quartis
perceptions_of_corruption = dataset["Explained by: Perceptions of corruption"]
perceptions_of_corruption_media = perceptions_of_corruption.mean()
perceptions_of_corruption_desvio_padrao = perceptions_of_corruption.std()
perceptions_of_corruption_max = perceptions_of_corruption.max()
perceptions_of_corruption_min = perceptions_of_corruption.min()