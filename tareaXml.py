import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

#address = input('Enter location: ')
address='http://py4e-data.dr-chuck.net/comments_191376.xml'
uh = urllib.request.urlopen(address)
data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)
sum=0

counts = tree.findall('.//count')
print('User count:', len(counts))
for iteam in counts:
    sum+=int(iteam.text)
print(sum)

