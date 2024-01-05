#Creando una funcion simple
#def saludar():
    #print("Hola Gorda ¿como andas?")

#Ejecutando la funcion simple   
#saludar()

#Crear una funcion que tenga parametros
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "rey"
    else:
        adjetivo = "amor"
    print(f"Hola {nombre}, mi {adjetivo} ¿Como andas?")
    
saludar("Maca","mujer")
saludar("Alvaro","hombre")
saludar("Fran","no binario")

#Crear una funcion que nos retorne valores
def crear_contraseña_random(num):
    chars = "abcdfghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f'{chars[c1]}{chars[c2]}{chars[c3]}{num*2}'
    num = 2
    #print(contraseña)
    #para que nos quede oculta a nosotrosque sea algo de nuestro sistema debe ser
    return contraseña

password = crear_contraseña_random(2)
frase = f"Tu contraseña nueva es: {password}"
#print(frase)

#Crear una funcion que nos retorne multiples valores
def crear_contraseña_random(num):
    chars = "abcdfghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f'{chars[c1]}{chars[c2]}{chars[c3]}{num*2}'
    num = 2
    #print(contraseña)
    #para que nos quede oculta a nosotrosque sea algo de nuestro sistema debe ser
    return contraseña,num

#Desempaquetando la funcion
password, primer_numero = crear_contraseña_random(298)

#Mostrando los resultados obtenidos y los datos utilizados para obtenerlo
print(f"Tu contraseña nueva es: {password}")
print(f"El numero para crearla es: {primer_numero}")
