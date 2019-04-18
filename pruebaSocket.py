import socket
mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Creo el socket
mysock.connect(('data.pr4e.org',80))#Digo a donde me voy a conectar y por cual puerto
cmd='GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()#El comando que hace la peticion
mysock.send(cmd)#Envio de la peticion
while True:
    data=mysock.recv((512))#Cantidad de caracteres a recibir
    print(data)
    if (len(data)<1):
        break

    print(data.decode(), end='')
    #print(data)
mysock.close()


