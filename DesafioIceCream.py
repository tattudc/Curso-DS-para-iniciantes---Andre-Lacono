import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('IceCreamData.csv')
df

result = df.sort_values('Temperature',ascending = False)
result['Revenue'] = result['Revenue'].round(0)
celsius = (df['Temperature'] - 32) * 5/9
result['Temperature'] = celsius
result['Temperature'] = result['Temperature'].round(0)
result = result.loc[(result['Temperature'] >= 0)]
result

plt.plot(result['Temperature'], result['Revenue'],'r.--', label='US$')
plt.title('Ice Cream Truck')
plt.ylabel('Sales (US$)')
plt.xlabel('Temperature (Celsius)')
plt.legend()
plt.savefig('icecream_sales.pdf')
plt.show()