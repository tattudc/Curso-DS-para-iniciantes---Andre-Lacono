import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

gas = pd.read_csv('gas_prices.csv')
gas

#plt.title('Valores do combustível em US$')
#plt.plot(gas['Year'],gas['Australia'],'r.-' ,label='Australia')
#plt.plot(gas['Year'],gas['Italy'],'y.-' , label='Italy')
#plt.plot(gas['Year'],gas['USA'],'b.-' , label='USA')
#plt.plot(gas['Year'],gas['Japan'],'g.-' , label='Japan')

list_country = ['Australia','USA','Canada','Italy','Maxico','France','Germany']

for country in gas:
    if country in list_country:
        plt.plot(gas['Year'],gas[country], label =[country], marker='.')

plt.xticks(gas['Year'][::2])
plt.xlabel('Years')
plt.ylabel('US$')

plt.legend()
plt.savefig('country.png')
plt.show()