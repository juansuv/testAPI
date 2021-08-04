import requests
from bs4 import BeautifulSoup
import pandas as pd
import json 


columnas = ['Image', 'Price', 'Title', 'Description','Rating']
data = pd.DataFrame(columns=columnas)

def insert_product(soup,df):
    for item in soup:
        image=item.find('img')['src']
        price=item.find('h4',class_='pull-right price').string
        title=item.find('a',class_='title').string
        description=item.find('p',class_='description').string
        rating=item.find('p',class_='pull-right').string
        
        datos={
            'Image':image,'Price':price,'Title':title ,'Description':description,'Rating':rating
        }
        
        df=df.append(datos,ignore_index=True)
    return df

def insert_product_subcategory(soup,df):
    res = json.loads(str(soup))
    for item in res:       
        image='None'
        price=item['price']
        title=item['title']
        description=item['description']
        rating=0        
        datos={
            'Image':image,'Price':price,'Title':title ,'Description':description,'Rating':rating
        }        
        df=df.append(datos,ignore_index=True)
    return df



baseurl='https://webscraper.io/test-sites/e-commerce/scroll/' 
           
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}


r = requests.get(baseurl)
soup= BeautifulSoup(r.content, 'lxml')

links=soup.find_all('a', class_='category-link')
links=[link['href'] for link in links]
productlist = soup.find_all('div', class_='thumbnail')
data=insert_product(productlist,data)


for link in links:    
    r = requests.get(f'https://webscraper.io/{link}/')
    soup= BeautifulSoup(r.content, 'lxml')
    productlist = soup.find_all('div', class_='thumbnail')
    data=insert_product(productlist,data)
   
    sublinks=soup.find_all('a', class_='subcategory-link')
    sublinks=[link['href'] for link in sublinks]
    for sublink in sublinks:
        
        r = requests.get(f'https://webscraper.io/{sublink}/')
        soup2= BeautifulSoup(r.content, 'lxml')
        print("-----------------------------------------------------------------------")
        productlistsub = soup2.find_all('div', class_='row ecomerce-items ecomerce-items-scroll')
        
        for productsub in productlistsub:
            data=insert_product_subcategory(productsub['data-items'],data)
        
               
print(data)


