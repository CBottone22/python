numeros = [4,7,1,42,15]

#encontrando el numero mayor de una lista
numero_mas_alto = max(numeros)
#print(numero_mas_alto)

#encontrando el numero menor de una lista
numero_mas_bajo = min(numeros)
#print(numero_mas_bajo)

#redondeando a 6 decimales
numero = round(12.345678,2)

#retorna false -> 0, false, vacio, none // True -> distinto a 0, cadena, True, datos no vacios
resultado_bool = bool(12354)

#retorna True, si todos los valores son verdaderos
resultado_all = all([0,True,[314,23]])

#suma todos los valores de un iterable
suma_total = sum(numeros)

print(suma_total)
