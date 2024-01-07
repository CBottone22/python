#importando un modulo y asignandole un nombre "m_saludar"
#import modulo_saludar as m_saludar 

#desde ese modulo importamos dos funciones y les cambiamos el nombre
from public.Modulos.modulo_saludar import saludar as saludar_normal,saludar_motivando as saludar_como_la_mejor
import modulo_saludar as m_saludar

#creamos las variables con los saludos
saludo = saludar_normal("Gorda")
saludar_motivando = saludar_como_la_mejor("Reyna")

#mostramos los resultados
print(saludo)
print (saludar_motivando)

#para ver todas las propiedades y metidos de namespsce
#print(dir(m_saludar))

#para acceder al nombre de este modulo
print(__name__)

#accedemos al nombre del modulo llamado
print(m_saludar.__name__)