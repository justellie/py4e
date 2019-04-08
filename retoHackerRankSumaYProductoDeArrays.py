import numpy as np
N, M = list(map(int, input().split()))

my_array = np.array([input().split() for i in range(0,N)], int)
print (np.prod(np.sum(my_array, axis = 0)))     
