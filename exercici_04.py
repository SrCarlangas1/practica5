print "Escribe un numero"
prime=int(raw_input())
lista=[]
print "Escrive un numero major que" , prime
secu=int(raw_input())
lista=lista+[prime]+[secu]
while prime>secu:
    print secu , "no es mayor que" , prime
    print ""
    print "Vuelve a escrivir otro numero"
    secu=int(raw_input())
    lista=lista+[prime]+[secu]
print "Los numeros que has escritos son" , prime , "y" , secu
