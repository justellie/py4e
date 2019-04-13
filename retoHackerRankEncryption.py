import math

def encryption(s):
    l=s.split()
    l = ''.join(l)
    longitud=len(l)
    rows=math.floor(math.sqrt(longitud))
    columns=math.ceil(math.sqrt(longitud))
    resultado=[]
    inicio=0
    #print(l)
    #print(rows)
    #print(columns)
    #print(len(l))
    fin=columns
    auxMatriz=[]
    codigoFinal=[]

    for i in range(0, rows):
        anadir=[l[inicio:fin]]
        #print(inicio, fin)
        #print(l[inicio:fin])


        #print(anadir)
        resultado.append(anadir)
        inicio+=columns
        fin+=columns
        #print(i)
    print(resultado)
    inicio=0
    fin=1
    for j in range(0, columns):
        for i in range(0, rows):
            #print(resultado[i])
            aux=' '.join(resultado[i])
            #print(aux[inicio:fin])
            auxMatriz.append(aux[inicio:fin])
        codigoFinal.append(''.join(auxMatriz))
        auxMatriz=[]
        inicio+=1
        fin+=1
    print(codigoFinal)
    print (' '.join(codigoFinal))
encryption('chillout')