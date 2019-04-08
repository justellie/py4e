def computepay(h,r):#Esto es una funcion
    total=0
    if h<40:
        total=r*h
        
    elif h>40:
    	total=40*r+((h-40)*(1.5)*r)
    return(total)
#Aqui se cierra la funcion    

hrs = input("Enter Hours:")
hrs=float(hrs)
rate=input("Enter rate:")
rate=float(rate)
p = computepay(hrs,rate)
print(p)