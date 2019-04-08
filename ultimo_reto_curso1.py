#TIENES QUE ESTAR PENDIENTE DE LOS ESPACIOS PORQUE ESA VAINA SI IMPORTA COÑO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
acum=0
mayor=None
menor=None
while True:
    print("ingrese numero o done para salir:")
    inp=input()
    if inp=='done':
        break	
    try:
        inp=int(inp)
    except :
        print('Invalid input')	
        inp=input()
        inp=int(inp)
    if mayor==None:
        mayor=inp
    elif inp>mayor:
        mayor=inp
    if menor==None:
        menor=inp 
    elif menor>inp: 
        menor=inp 
    acum+=inp	
	
print('acumulado', acum)
print('mayor',mayor)
print('menor', menor)