name=input('Introduzca el nombre del archivo: ')
handle=open(name)

counts=dict()
for line in handle:#Lee cada linea del archivo
	words=line.split()#vuelve cada linea una lista
	for word in words:#lee cada elemento de esa lista
		counts[word]=counts.get(word,0)+1#Nos da la cantidad de veces que se repite una palabra
bigcount=None
bigword=None

for word,count in counts.items():
	if bigcount is None or count>bigcount:
		bigword=word
		bigcount=count
#print(counts)
print(bigword, bigcount)
