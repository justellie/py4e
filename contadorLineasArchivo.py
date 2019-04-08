fhand= open('mbox-short.txt')
cont=0
for i in fhand:
	cont+=1
print('la cantidad de lineas es', cont)	

fhand= open('mbox-short.txt')
for i in fhand:
	i=i.rstrip()
	if i.startswith('From: '):#Imprime la linea que comience por 'Received'
		print(i)
	