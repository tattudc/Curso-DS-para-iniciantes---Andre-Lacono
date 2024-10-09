import pandas as pd

dados = pd.read_csv('fifa.csv')

#dados.head() #Mostra os dados iniciais
#dados.tail() #Mostra os dados finais
#dados.columns #Buscar columns
#dados.index #Buscar os index
#dados[['Name']] #Buscar pela Coluna
#dados.iloc[2,2] #Buscar dado da Linha e Coluna
#dados.loc[dados['Nationality']=='Brazil']
#dados.loc[dados['Age']==41] #Função pra encontrar a partir de uma coluna
#dados.sort_values('Name',ascending = False) #Função pra ordenar

dados['Total'] = dados['Acceleration'] + dados['Agility'] + dados['Reactions'] #Somar dados de colunas e criar uma nova coluna
dados = dados[['Name','Total']] #Filtrar dados
dados = dados.sort_values('Total', ascending = False) #Trazer dados ordenados
dados
#dados.to_csv('dados1.csv',index=False)
#dados.to_excel('dados2.xlsx',index=False)
#dados.to_csv('dados3.txt',index=False, sep='\t')