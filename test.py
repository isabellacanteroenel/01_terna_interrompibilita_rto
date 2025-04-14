import requests
from bs4 import BeautifulSoup
 
# URL do site
url = 'http://80.76.69.149:8080/datascope/login.do'
 
# Fazer a requisição GET
response = requests.get(url)
 
# Verificar o status da requisição
if response.status_code == 200:
    # Criar o objeto BeautifulSoup com o conteúdo HTML
    soup = BeautifulSoup(response.text, 'html.parser')
 
    # Encontrar todos os links (tags <a>)
    links = soup.find_all('a')
 
    # Imprimir o texto de cada link
    for link in links:
        site_name = link.get_text(strip=True)  # Extrair o texto do link
        if site_name:  # Verificar se o texto não está vazio
            print(site_name)
else:
    print('Erro ao acessar o site:', response.status_code)