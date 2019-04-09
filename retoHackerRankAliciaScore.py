def climbingLeaderboard(scores, alice):#Esto es de orden N
    unique_scores = list(reversed(sorted(set(scores))))#Convierte en un set  eleminando todos los elementos respetidos y luego hago una lista y ordeno
    i = len(unique_scores) - 1#Obtengo la longitud de la lista ordenada para interarla
    resultado = []

    for j in range(0, len(alice)):#Interare sobre cada elemento de Alice
        while (i >= 0):#Recorro de la menor puntuacion hasta la mayor
            if alice[j] >= unique_scores[i]:#Si la putuacion de alice es mayor o igual a la putuacioi que esta en el score
                i -= 1#Avanzo en el score
                #print(i)

            else:#Cuando encuentro un valor que es mayor al score de alice entonces me encuento en la mitad de el score menor al de alice y el mayor que en ese caso el menor se desplaza una posicion hacia abajo y el score de alice toma esa posicion y por esa razon al añadir se suma uno al interador 1
                resultado.append(i + 2)#Y como se inicia en 1 y no en 0 se suma otro
                break
        if i==-1:#En el caso de que No haya ningun valor que sea mayor a de alice entonces alice tiene el primer lugar y lo añado. Esto se hace fuera del while pòrque la posicion -1 no existe en ninguna lista jamas y entonces se ignora
            resultado.append(i + 2)

    return (resultado)











scores=[100,100,50,40,40,20,10]
alice=[5,25,50,120]
climbingLeaderboard(scores,alice)