print('Ingrese una palabra')
palabra_mayor= input()
print('Ingrese una segunda palabra')
palabra_menor=input()

band= palabra_menor in palabra_mayor #revisa si la palabra menor esta en la mayor

if band:
	print( palabra_menor, 'Esta contenida en ', palabra_mayor)
else:	
	print( palabra_menor, 'No esta contenida en ', palabra_mayor)