fhand= open('mbox-short.txt')
aux=fhand.read()
aux=aux.split()
aux.sort()
print(aux)
#Lee un archivo , lo convierte en una lista y ordenas los elementos en esa lista