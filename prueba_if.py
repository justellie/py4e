#Prueba de if
print("ingrese numero:")

inp=input()
try:
	inp=int(inp)
except :
	print("ingrese un valor numerico")	
	inp=input()
	inp=int(inp)


if inp>5:
	print("Mayor a 5")
elif inp<5:
		print("Menor a 5")
else:
    print("Es 5")

	
