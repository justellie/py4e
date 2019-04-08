#Prueba loops 
n=0
while True:
	line= input('> ')
	n+=1
	if line[0]=='#':
		continue #esta vaina se salta hasta la proxima interacion 
	if line=='done':
		break
	print(line)
	print(n)
print('DONE!')		