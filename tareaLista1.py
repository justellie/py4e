#Lista de palabras que estan en un archivo excluyendo cuando se repiten
fname = input('Nombre de archivo: ')
fh = open(fname)
lst = list()
for line in fh:
    line.rstrip
    aux=line
    aux=aux.split()

    for word in aux:
        band=word in aux
        if word in lst: continue
        lst.append(word) 
        
       
lst.sort()        
print(lst)