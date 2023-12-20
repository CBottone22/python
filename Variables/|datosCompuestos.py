#creando una lista (se puede modificar)
lista = ["Caro Bottone", "Genia", True, "Genia"]
 
#creando una tupla (no semificar)
tupla = ("Caro Bottone", "Genia", True, True)

#esto es valido
lista[2]= "Maquinola"

#esto no es valido
#tupla[2]= "Maquinola"

#creando un conjunto (set)[no se puede llamar datos por su indice, no muestra datos duplicados]
conjunto = {"Caro Bottone", "Genia", True, "Genia"}

#print (conjunto[2])#no puede acceder al elemento

#creando un diccionario(dict)[la estructura es llave y valor o key and value. y se separan por comas]
diccionario = {
    "nombre": "Caro",
    "Simplemente": "Genia",
    "es_la_mejor": True,
    "dato_duplicado": "Caro"
}
print(diccionario["nombre"])