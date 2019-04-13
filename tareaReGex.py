import re
#Suma todos los valores numericos en un archivo

hand=open('regex_sum_191372.txt')
suma=0
for line in hand:
    line=line.rstrip()
    line=re.findall('[0-9]',line)
    if len(line)>0:
        line=map(int,line)
        suma+=(sum(line))
print(suma)
