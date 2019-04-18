import xml.etree.ElementTree as ET
"""
data ='''<person>
    <name>Chuck</name>
    <phone type="intl">
    +1 734 303 4456
    </phone>
    <email hide="yes"/>
    </person>'''
#las tres comillas simpless fue para meter toda esa informacion en varias lineas Jaja salu2

tree=ET.fromstring(data)#Crea un arbol de el documento
print('Name: ', tree.find('name').text)#obtengo el contenido de name
print('Attr: ', tree.find('email').get('hide'))#Obtengo el valor de hide
"""

input ='''<stuff>
    <users>
            <user x="2">
                <id>001</id>
                <name>Chuck</name>    
            </user>
            <user x="7">
                <id>009</id>
                <name>Brent</name>    
            </user>    
        </users>
    </stuff>'''
stuff=ET.fromstring(input)#un arbol
lst=stuff.findall('users/user')#una lista de arboles
print('User count:',len(lst))
for iteam in lst:
    print('Name ', iteam.find('name').text)
    print('ID ', iteam.find('id').text)
    print('Attribute ', iteam.get('x'))
