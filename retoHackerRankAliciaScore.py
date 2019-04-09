def climbingLeaderboard(scores, alice):#Esto es de orden N
    unique_scores = list(reversed(sorted(set(scores))))#Convierte en un set  eleminando todos los elementos respetidos y luego hago una lista y ordeno
    aux=unique_scores.copy()
    resultado=[]
    for i in range(0,len(alice)):
        aux.append(alice[i])
        aux.sort(reverse=True)
        #print(aux)
        resultado.append(aux.index(alice[i])+1)
        #print(aux.index(alice[i])+1)
        aux=unique_scores.copy()
    #print(resultado)
    return (resultado)





                





scores=[100,100,50,40,40,20,10]
alice=[5,25,50,120]
climbingLeaderboard(scores,alice)