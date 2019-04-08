def diagonalDifference(arr):
    acumPrinDig=0
    acumSecDig=0
    colum=len(arr)
    for filas in range(0,len(arr)):
        acumPrinDig+=arr[filas][filas]
    for filas in range(0,len(arr)):
        acumSecDig+=arr[filas][colum-1]
        colum-=1
    total=acumPrinDig-acumSecDig
    if total<0:
        total=total*-1
    return(total)
