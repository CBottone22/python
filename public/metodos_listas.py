#creando una lista con list
lista = list([25,44,34])

#devuelve la cantidad de elementos de la lista
#resultado = len(lista)

#agregando un elemento a la lista
lista.append(40)

#agregando un elemento a la lista en un indice especifico
#lista.insert(56)

#agregando varios elementos a la lista
lista.extend([False,2030,True,False])

#elimina un elemento de la lista (por su indice)
#lista.pop(-2)#-1 para eliminar el ultimo, -2 elimina el anteultimo y asi sucesivamente

#removiendo un elemento de la lista x su valor
#lista.remove("21")

#ordenando la lista en forma ascendente(si usamos el parametro reverse=True lo ordena en reversa)
lista.sort()

#invirtiendo los elementos en una lista
lista.clear()

print(lista)