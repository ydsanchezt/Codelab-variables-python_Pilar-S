#Tipo de datos
#Entero (int)
año = 2023
print (año)
número_días = 7
print (número_días)
#float
peso = 45.6
print (peso)
estatura = 1.56
print (estatura)
#String 
nombre = "Pilar"
lugar = "Bogotá"
días_semana = "lunes, martes, miercoles, jueves, viernes, sabado y domingo"
print (nombre, lugar, días_semana, sep="-")
#booleanos
tengo_hambre = True
Estoy_llena = False

#concatenación
descripción = "Soy " + nombre + " y vivo en " + lugar + " mi altura y estatura es " + str ( peso ) + " y " + str ( estatura )
print (descripción)

"""
Los números enteros representan a los números naturales más el 0, estos pueden ser positivos o negativos y tienen las siguientes características:
Están en una base concreta (por defecto base 10).
Pueden ser negativos o positivos o cero (0).
Pueden realizarse operaciones entre ellos.
Son el tipo base, por lo que se pueden realizar operaciones con otros tipos fácilmente.
En Python no hay límite de tamaño de estos números.

El tipo numérico float permite representar un número positivo o negativo con decimales, es decir, números reales. 
Los números tipo float a diferencia de los int tienen unos valores mínimo y máximos que pueden representar.
Los números en punto flotante se componen de dos parte, la parte entera y la parte decimal. En Python tienen las siguientes características:

Pueden ser positivos, negativos ó 0.
El separador de las partes es el carácter punto ('.').
Se pueden representar como un punto y la parte decimal para decir 0.decimales.
Se pueden utilizar con otros tipos de números como los enteros.
La precisión máxima está limitada por 53 bits.
"""
#Sumar número pares consecutivos usando la formula : n*(n+1)
n=20
suma = n*(n+1)
print(suma)