import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url=' http://py4e-data.dr-chuck.net/known_by_Fikret.html'#Pedimos la direccion
html=urllib.request.urlopen(url).read()#abrimos la pagina read lee todo el archivo
soup=BeautifulSoup(html,'html.parser')#Convierte todos esos bits en un objeto manejable por python

tags=soup('a')
#print(tags)
for tag in tags:
    print(tag.get('href',None))