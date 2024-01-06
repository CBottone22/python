numeros = [1,2,3,4,5,6,7,8,9]

#creando una funcion lambda para multiplicar por dos
multiplicar_por_dos = lambda x: x*2

#Creando función común que diga si es par o no
#def es_par(num):
 #   if(num%2==1):
  #      return True

#usando filter con una función común
#numeros_impares = filter(es_par,numeros)

#Creando lo mismo con Lambda
numeros_pares = filter(lambda numero:numero%2==0,numeros)

print(list(numeros_pares))