#Falto el profe y los chicos van a armar la clase

#Pedir el nombre y la edad de los compañeros que vinieron hoy a clases
def obtener_compañeros(cantidad):
    compañeros = []
    for i in range(cantidad_de_compañeros):
        nombre = input("ingrese el nombre del compañero")
        edad = int(input("ingrese la edad del compañero"))
        compañero = (nombre,edad)
        compañeros = append(compañero)
    compañeros.sort(key=lambda x:x[1])
    asistente = compañeros[0][0]