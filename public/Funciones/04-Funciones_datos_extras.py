#creando una funcion de tres parametros

#def frase(nombre,apodo,adjetivo):
 #   return f'Hola {nombre}, {apodo} sos muy {adjetivo}'

#utilizando keyword arguments
#frase_resultante = frase(adjetivo = "genia",nombre = "Caro",apodo = "gorda")
#print(frase_resultante)

#creando la misma función con un parametrto opcional y un valor por defecto
def frase(nombre,apodo,adjetivo = "tonta"):
    return f'Hola {nombre}, {apodo} sos muy {adjetivo}'

frase_resultante = frase("Caro","gorda","genia")
print(frase_resultante)