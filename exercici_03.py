print "Escribe un numero"
prime=float(raw_input())
lista=[]
while prime>0 and prime<10:
    lista=lista+[prime]
    print "Escribe otro numero"
    prime=float(raw_input())
print "Los numeros escritos son" , lista
