counts=dict()
names=['csev','cwen','csev','zquian','cwen']
for name in names:
	counts[name]=counts.get(name,0)+1
	"""
	Si esta el nombre añade uno Si no esta el nombre lo añade con el valor de 0 por default
	"""
print(counts)