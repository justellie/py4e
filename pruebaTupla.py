name=input('Introduzca el nombre del archivo: ')
handle=open(name)

counts=dict()
for line in handle:#Lee cada linea del archivo
	words=line.split()#vuelve cada linea una lista
	for word in words:#lee cada elemento de esa lista
		counts[word]=counts.get(word,0)+1#Nos da la cantidad de veces que se repite una palabra
lst=list()
for key,val in counts.items():#Convierte el dicionario en una lista de tuplas
	newtup=(val,key)#organiza valor-keyword
	lst.append(newtup)#añade a nuestra lista auxiliar
lst=sorted(lst,reverse=True)#ordena por valor 

for val,key in lst[:10]:#llama a a los primero 10
	print(key,val)#imprime
