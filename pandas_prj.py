###
Projeto de do módulo "Análise de Dados com Python e Pandas"
do BootCamp de Data Engineer do Banco Carrefour - Digital Innovation One
Informações sobre as manifestações da Ouvidoria relacionadas à pandemia de Coronavírus (COVID-19) recebidas pelo Governo do Estado de Santa Catarina, coletadas no Portal de Dados Abertos do Governo / CGE Trabalho meramente educacional, visando aplicar os conceitos de data engineering para aprimoramento pessoal/profissional.
Originalmente, os tratamentos foram realizados no Colaboratory/Google.
Autor: Omar Sega
12/08/2021
###


#Importar o Panda
import pandas as pd

#Importar dataframe lendo o arquivo csv
df = pd.read_csv("/data.csv")

#Listando as 5 primeiras linhas do Dataframe
df.head(5)

#Total de linhas e colunas do df
df.shape

#Listando os tipos
df.dtypes

#Informações estatísticas do df
df.describe

#Verificando total de missing values do df
df.isnull().sum()

#Uma vez que se trata de um projeto com pretensões de fixação de conteúdo, o tratamento de dados
#será feito excluindo-se missing values
df.dropna(inplace=True)

#Após o tratamento de dados acima, nosso df aprensenta agora a seguinte quantidade de linhas/colunas:
df.shape

#Gráfico de barras sobre as ocorrências enviadas à Ouvidoria Estadual de SC sobre a COVID-19:
import matplotlib.pyplot as plt
df["natureza"].value_counts(ascending=False).plot.bar(title="Tipos de Ocorrência Ouvidoria SC -Covid-19:", color="magenta")
plt.xlabel("Tipo de evento da entrante na Ouvidoria")
plt.ylabel("Quantidade de eventos")
plt.legend(["ocorrências"])
plt.style.use("ggplot");
#para salvar a img:
#plt.savefig("ocorrencias_ouvidoria_sc.png");








