from bs4 import BeautifulSoup
import requests
import pandas as pd


url = 'https://listado.mercadolibre.com.ar/procesadores#D[A:procesadores]'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


#Nombres de Publicaciones

namePub = soup.find_all('h2', class_='ui-search-item__title')

nameList = list()

count = 0

for i in namePub:
    if count < 20:
        nameList.append(i.text)
    else:
        break
    count += 1

# print(nameList, len(nameList))

#Precios de Tablets

pricePub = soup.find_all('span', class_='price-tag-fraction')

priceList = list()

count = 0

for i in pricePub:
    if count < 20:
        priceList.append(i.text)
    else:
        break
    count += 1

# print(priceList, len(priceList))

#Reviews del Producto

reviewsPub = soup.find_all('span', class_='ui-search-reviews__amount')

revList = list()

count = 0

for i in reviewsPub:
    if count < 20:
        revList.append(i.text)
    else:
        break
    count += 1




#Arma Tabla

df = pd.DataFrame({'Producto': nameList,'Precio':priceList,'Cant de Reviews': revList}, index=list(range(1,21)))
#df['Producto'] = df['Producto'].str.replace('"','')
print(df)
df.to_csv('preciosProductos.csv', index=False)