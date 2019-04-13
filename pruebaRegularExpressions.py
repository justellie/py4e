import re
"""
hand=open('mbox-short.txt')
for line in hand:
    line=line.rstrip()
    if re.search('\S+@\S+',line):#Imprime toda la linea
        print(line)
"""
y=[]
hand=open('mbox-short.txt')
for line in hand:
    line=line.rstrip()
    line = re.findall('\S+@\S+', line)#imprime solo lo que cumple esta condicion
    if len(line)>0:
        y.append(line)
print(len(y))
y=[]
hand=open('mbox-short.txt')
for line in hand:
    line=line.rstrip()
    line = re.findall('From (\S+@\S+)', line)#los parentesis no son parte del match pero dicen donde iniciar y finalizar la extracion
    print(line)