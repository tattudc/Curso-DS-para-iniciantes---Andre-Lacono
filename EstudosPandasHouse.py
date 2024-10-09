import pandas as pd
import re
df = pd.read_csv('house.csv')
#filter1 = df.loc[(df['Rooms']==3) & (df['Type'] == 'h') & (df['Price'] <= 500000)] #Pesquisa por tipo e preço
#filter1

#filter2 = df.loc[df['Address'].str.contains('Turner st|Turner Rd', flags=re.I)] #Pesquisa endereço não importa se tá maiuscula ou minuscula
#filter2

#filter3 = df.loc[(df['Address'].str.contains('^59', flags=re.I)) & (df['Price'] <= 500000)] #Pesquisar Endereço n59 e preço abaixo de 500k
#filter3

#filter4 = df.loc[df['SellerG']=='Nelson',['Method','Type']] = 'Pending' #Trocar dados
df.groupby(['SellerG']).count().sort_values('Rooms',ascending = False).head(10) #Pode somar com sum de acordo com criterios, count conta e mean faz a media