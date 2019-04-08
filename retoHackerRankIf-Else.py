N = int(input())
even=(N%2)
print(even)

if (N%2)!=0:
    print('Weird')
else:
	if N==0:
		print('Not Weird')
	else:	
	    if N>=2 and N<=5:
	        print('Not Weird')
	    else:
	        if N>=6 and N<=20:
	            print('Weird')
	        else:
	            if N>20:
	                print('Not Weird') 