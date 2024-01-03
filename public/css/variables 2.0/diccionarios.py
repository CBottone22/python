#creando diccionarios con dict()
diccionario = dict(nombre="Caro",apodo="gorda")

#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["caro","gorda"]):"jajaja"}

#creando diccionarios con fromkeys() valor por defecto none
diccionario = dict.fromkeys(["nombre","apodo"])

#creando diccionarios con fromkeys() cambiando el valor por defecto a "No se"
diccionario = dict.fromkeys(["nombre","apodo"],"No se")

print(diccionario)