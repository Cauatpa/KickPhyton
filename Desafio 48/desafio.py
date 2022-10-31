#COLETA DE DADOS!!!

import openpyxl
from bs4 import BeautifulSoup
import requests

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip,deflate,sdch',
    'Accept-Language':'pt-BR; q=0.9;en-US,en;q=0.8',
    'Connection':'Keep-alive',
    'Referer':'https://www.google.com.br',
}

resposta = requests.get("https://www.amazon.com.br/s?k=pc&__mk_pt_BR=ÅMÅŽÕÑ&crid=1QFK2NDX8YSHD&sprefix=pc%2Caps%2C212&ref=nb_sb_noss_1", headers = HEADERS)
resposta.text

soup = BeautifulSoup(resposta.text, 'html.parser')
soup
info = soup.find_all(class_="a-size-base-plus a-color-base a-text-normal")
prod = soup.find_all(class_= "a-price-whole")

produtos = []
prod2 = []

for i in info:
  produtos.append(i.text)

for j in prod:
  prod2.append(j.text)
  
produtos
prod2


#PLANILHA!!!

planilha = openpyxl.Workbook()

planilha.create_sheet('Produtos') 

aba_produtos = planilha['Produtos']
aba_produtos.append(['Produto', 'Preço'])

for i in range(1,len(produtos)):
  aba_produtos.append([produtos[i],prod2[i]])

planilha.save('produtos.xlsx')


###PDF!!



