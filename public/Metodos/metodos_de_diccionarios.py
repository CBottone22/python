#keys() devuelve las claves y tb sirve para iterar
diccionario = {
    "nombre": 'Caro',
    "apodo": 'gorda',
    "subs": '10000000'
}

#nos dewvuelve un objeto dict_item
claves = diccionario.keys()

#obteniendo un elemento con get() (si no encuentra nada el programa contrinua)
claves = diccionario.get("nombre")

#eliminando todo el diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
#diccionario.pop("nombre","subs")

#obteniendo una dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)