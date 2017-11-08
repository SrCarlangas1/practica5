print "Escribe un numero"
prime=raw_input()
lista=[]
while prime<>"":
    lista=lista+[int(prime)]
    print "Escribe otro numero"
    prime=raw_input()
print "Los numeros escritos son" , lista
