import requests
from bs4 import BeautifulSoup
import csv

# URL de la página web
url = 'https://sueciabarbershop.cl/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extraer datos específicos
    titulos = soup.find_all('h1')
    
    # Imprimir los títulos 
    with open('datos.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Titulo']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for titulo in titulos:
            writer.writerow({'Titulo': titulo.text})
else:
    print(f'Error al acceder a la página: {response.status_code}')
