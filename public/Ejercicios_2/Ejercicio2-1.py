#Falto el profe y los chicos van a armar la clase

#Función para obtener el asistente y el profesor según la edad
def obtener_compañeros(cantidad_de_compañeros):
    
    #Creando la lista de compañeros
    compañeros = []
    
    #ejecutando un for para pedir informacion de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre = input("ingrese el nombre del compañero: ")
        edad = int(input("ingrese la edad del compañero: "))
        compañero = (nombre,edad)
        
        #agregando la informacion a la lista
        compañeros.append(compañero)
        
    #ordenando de menor a mayor su edad
    compañeros.sort(key=lambda x:x[1])
    
    #compañeros[x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre
    #para definir al asistente y al profesor
    asistente = compañeros[0][0]
    profesor = compañeros[-1]
    
    #retornamos la tupla
    return asistente,profesor

#desempaquetamos lo que nos retorna la función
asistente,profesor = obtener_compañeros(5)

#mostrando el resultado
print(f"El profesor es: {profesor} y su asistente es: {asistente}")