import urllib.request, urllib.parse, urllib.error

fhand=urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')#obtine la informacion que hay en esa url como un archivo
for line in fhand:
    print(line.decode().strip())


""""
counts = dict()
for line in fhand:  # Lee cada linea del archivo
    words = line.decode().split()  # vuelve cada linea una lista
    for word in words:  # lee cada elemento de esa lista
        counts[word] = counts.get(word, 0) + 1
print(counts)
"""