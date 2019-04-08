#Me dice que cantidad de mensajes fueron recibidos en una fecha dada
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
fechas=list()
counts=dict()
for line in handle:
	line=line.strip()
	if line.startswith('From') and line.find(':')>5:
		pos=line.find(':')
		fechas.append(line[pos-2:pos])		
for fecha in fechas:
    counts[fecha]=counts.get(fecha,0)+1
    
lst=list()
for key,val in counts.items():
    newtup=(key,val)
    lst.append(newtup)
lst=sorted(lst)

for key,val in lst:
    print(key,val)
#LO HICEEEEEEE!!!!!!!!!!!!!!!