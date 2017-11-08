print "Escribe un numero"
prime=int(raw_input())
lista=[]
print "Escrive un numero major que" , prime
secu=int(raw_input())
lista=lista+[prime]+[secu]
while prime<secu:
    lista=lista+[secu]
    print "Escrive un numero major que" , secu
    secu=int(raw_input())
print "Los numeros que has escritos son" , lista
