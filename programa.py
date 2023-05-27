#Ejemplos 

#La clave es una cadena

num_mes = {"enero":1, "febrero":2, "marzo":3, "abril":4, "mayo":5,}

print(num_mes)

#la clave es un entero

nom_meses ={1:"enero", 2:"febrero", 3:"marzo", 4:"abril", 5:"mayo"}

print(nom_meses)

print("el tipo es: ", type(nom_meses))

#Creacion de diccionarios por el constructor "una lista de duplas"

dic1=dict([("la paz", 13), ("lima", 27), ("caracas", 30)])

print("con lista de tuplas: ", dic1)

#listas por comprension

dic_cubos= dict([(n, n**3)for n in range(1, 5)])

print(dic_cubos)

#usando un diccionario desarrollar una calculadora basica con Menu
from math import log
print("1 ---> suma(x+y)")
print("2 ---> resta(x-y)")
print("3 ---> multiplicacion(x*y)")
print("4 ---> division(x/y)")
print("5 ---> potencia(x^y)")
print("6 ---> Logaritmo(base =x, argumento=y)")

#input
x = float(input("ingrese el valor de X: "))
y = float(input("ingrese el valor de Y: "))
opcion=input("operacion que desea realizar: ") 

#processing
operaciones={"1":x+y, "2":x-y, "3":x*y, "4":x/y, "5":x**y, "6":log(x,y)}

#Salida
print(operaciones[opcion])