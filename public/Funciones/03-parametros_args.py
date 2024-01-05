#Forma no optima de sumar valores
#def suma(lista):
 #   numeros_sumados = 0
  #  for numero in lista:
   #     numeros_sumados = numeros_sumados + numero
   # return(numeros_sumados)

#resultado = suma([5,3,6,10,4])

#Utilizando el parametro * como argumento (*args)
def suma(nombre,*numeros):
    return f'{nombre}, la suma de tus numeros es: {sum(numeros)}'


resultado = suma("Caro",5,3,6,10,4)   
#print (resultado)

#Lo mismo que arriba pero usando el operador args como parametro
def suma_total(*numeros):
    return sum (*numeros)

resultado2 = suma_total([5,3,6,10,4])

print(resultado2)