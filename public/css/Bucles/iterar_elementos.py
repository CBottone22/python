animales = ["gato","perro","loro","cocodrilo"]
numeros = [52,16,32,14]

#recorriendo la lista animales
for animal in animales:
    print(f'ahora la variable animal es igual a: {animal}')
  
#recorriendo la lista numeros y multiplicando cada valor por 10    
for numero in numeros:
    resultado = numero * 10
    print(resultado)

#recorriendo dos listas del mismo tamaño al mismo tiempo   
for numero,animal in zip(animales,numeros):
    print(f'recorriendo lista 1: {numero}')
    print(f'recorriendo lista 2: {animal}')

#forma no optima de recorrer una lista  (no funciona en conjuntos)
for num in range (len (numeros)):
    print(numeros[num])
    
#forma correcta de rcorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es: {indice} y el valor es: {valor}')
    
#usando el for/else
for numero in numeros:
    print(f'ejecutando el ultimo bucle, valor actual: {numeros}')
else:
    print("el bucle termino")
    
#TODO LO ANTERIOR FUNCIONA EXACTAMENTRE IGUAL PARA LISTAS, TUPLAS Y CONJUNTOS