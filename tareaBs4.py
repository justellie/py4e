
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

suma=0
count=0
url=' http://py4e-data.dr-chuck.net/comments_191374.html'#Pedimos la direccion
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
spans=soup('span')#Busco los span del documento y me retorna una lista
#print(spans)
for span in spans:
    #print(span.contents[0])
    #print(int(span.contents[0]))
    suma+=int(span.contents[0])#Obtengo el contenido de la etiqueta span y lo sumo
    count+=1
print( count, suma, sep='\n')