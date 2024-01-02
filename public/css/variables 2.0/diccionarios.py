#creando diccionarios con dict()
diccionario = dict(nombre="Caro",apodo="gorda")

#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["caro","gorda"]):"jajaja"}

#creando diccionarios con fronkeys
diccionario = dict.fronkeys(["nombre","apodo"])

print(diccionario)