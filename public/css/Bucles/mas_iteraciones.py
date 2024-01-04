#creando las listas
cadena ="Hola Gorda"
frutas = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]
numeros = [2,5,8,10]

#evitando que se coma un granada con la sentencia continue
for fruta in frutas:
    if fruta == "granada":
        continue
    print(f'Me voy a comer una {fruta}')
    
#evitar que el bucle se siga ejecutando (el else no se ejecuta tampoco)
    if fruta == "pera":
        break
    print(f'Me voy a comer una {fruta}')
else:
    print("terminado")

#recorrer(recorrer es igual a iterar) una cadena de texto
for letra in cadena:
    print(letra)
     
#for en una sola linea de codigo (duplicamos los numeros)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)