import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url='http://py4e-data.dr-chuck.net/known_by_Aamna.html'#Pedimos la direccion
html=urllib.request.urlopen(url).read()#abrimos la pagina read lee todo el archivo
soup=BeautifulSoup(html,'html.parser')#Convierte todos esos bits en un objeto manejable por python
count=int(input('Enter count: '))
position=int(input('Enter position: '))

band=0
position-=1
count-=1
tags=soup('a')
print(url)
#print(tags)
while band <= count:

    print(tags[position].get('href',None))
    url = tags[position].get('href',None)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    band+=1