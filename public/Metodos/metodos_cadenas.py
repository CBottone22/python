cadena1 = "holaGordaComoEstas"
cadena2 = "Bienvenida Gorda"

#convcierte a mayusculas
resultado = cadena1.upper()

#convierte a minusculas
resultado = cadena1.lower()

#primera letra en mayuscula
resultado = cadena1.capitalize()

#buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1    
busqueda_find = cadena1.find("g")

#buscamos una cadena en otra cadena, si no haya coincidencias, lanza una excepción
busqueda_index = cadena1.index("a")

#si es numerico devolvemos True, sino devolvemos False
es_numerico = cadena1.isnumeric()

#es alfanumerico devolvemos true, sino devolvemos false
es_alfanumerico = cadena1.isalpha()

#contamos las coincidenciaS de una cadena, dentro de otra cadena, devuelve la cantidad de coincidencias 
contar_coincidencias = cadena1.count("p")

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

print(contar_caracteres)