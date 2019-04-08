
lisNom=list()
lisScore=list()
for _ in range(int(input())):
    name = input()
    score = float(input())
    lisScore.append(score)
    lisNom.append((name,score))
lisNom.sort() 
n=min(lisScore)
   
while min(lisScore) == n:
    lisScore.remove(min(lisScore))
n=min(lisScore)
print(*[name for name,value in lisNom  if value==n],sep='\n')#Pasa como valores a los elementos de una lista que contiene los elementos que tengan el mismo valor ,siendo este valor la segunda menor nota

