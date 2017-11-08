print "Escribe una palabra"
prime=raw_input()
lista=[]
while prime<>"":
    lista=lista+[prime]
    print "Escribe otra palabra"
    prime=raw_input()
print "Las palabras escritas son" , lista
