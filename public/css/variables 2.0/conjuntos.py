#creando un conjunto con set()
conjunto = set(["dato1","dato2"])

#metiendo un cojunto dentro de otro conjunto
conjunto1 = frozenset(["dato1","dato2"])
conjunto2 = {conjunto1,"dato3"}

print(conjunto2)

#Teoria de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#varificando si es un subconjunto
#resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

#varificando si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1

#verificar si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)