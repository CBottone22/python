cadena1 = "hola gorda como estas"
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

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True
empieza_con = cadena1.startswith("h")

#verificamos si una cadena termina con otra cadena dada, si es asi devuelve True
termina_con = cadena1.endswith("s")

#si el valor 1 se encuentra en la cadena original, reemplaza el valor 1 de la misma x el valor 2
cadena_nueva = cadena1.replace("la", "lis")

#nos va a separar cadenas con una cadena que le pasemos
cadena_separada = cadena1.split(" ")

print(cadena_separada[3])