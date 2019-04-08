import numpy as np 
np.set_printoptions(legacy='1.13')#ESTA MIERDA ES IMPORTANTE PARA HR
N, M = list(map(int, input().split()))
my_array = np.array([input().split() for i in range(0,N)], int)
print (np.mean(my_array, axis = 1))    
print (np.var(my_array, axis = 0))   
print (np.std(my_array))       
