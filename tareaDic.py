name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
correos=list()
counts=dict()
for line in handle:
   line=line.strip()
   if line.startswith('From: '):
   		aux=line.split()
   		correos.append(aux[1])
for correo in correos:
	counts[correo]=counts.get(correo,0)+1     

bigcorreo=None
bigcount=None

for correo,count in counts.items():
    if bigcount is None or count>bigcount:
        bigcorreo=correo
        bigcount=count
print(bigcorreo,bigcount)        
    