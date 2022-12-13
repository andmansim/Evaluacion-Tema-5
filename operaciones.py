'''
Crea el siguiente módulo:

·        El módulo se denominará operaciones.py y contendrá 4 funciones para realizar una suma, una resta, un producto y una división entres dos números. Todas ellas devolverán el resultado.

·        En las funciones del módulo deberá de haber tratamiento e invocación manual de errores para evitar que se quede bloqueada una funcionalidad, eso incluye:

·        TypeError: En caso de que se envíen valores a las funciones que no sean números. Además deberá aparecer un mensaje que informe Error: Tipo de dato no válido.

·        ZeroDivisionError: En caso de realizar una división por cero. Además deberá aparecer un mensaje que informe Error: No es posible dividir entre cero.

Una vez creado el módulo, crea un script calculos.py en el mismo directorio en el que deberás importar el módulo y realizar las siguientes instrucciones. Observa si el comportamiento es el esperado:

from operaciones import *

 

a, b, c, d = (10, 5, 0, "Hola")

 

print( "{} + {} = {}".format(a, b, suma(a, b) ) )

print( "{} - {} = {}".format(b, d, resta(b, d) ) )

print( "{} * {} = {}".format(b, b, producto(b, b) ) )

print( "{} / {} = {}".format(a, c, division(a, c) ) )
'''
def control_num1(num1):
    a = isinstance(num1, int)
    try :
        a == True   
    except:
        num1 = int(input('Introduce un número '))
        return num1
    
def control_num2(num2):
    b = isinstance(num2, int)
    try: 
        b == True
    except:
        num2 = int(input('Introduce un número '))
        return num2
    

    
def suma(a, b):
    try:
        suma = a + b
    except TypeError:
        a = int(input('Escribe un número '))
        b = int(input('Escribe un número '))
        suma = a + b
    return suma

def resta(a, b):
    
    try:
        resta = a - b
    except TypeError:
        a = int(input('Escribe un número '))
        b = int(input('Escribe un número '))
        resta = a - b


def producto(a, b):
    try:
        multi = a * b
    except TypeError:
            a = int(input('Escribe un número '))
            b = int(input('Escribe un número '))
            multi = a * b
    return multi

def division(a, b):
    try:
        div = a / b
    except TypeError:
        a = int(input('Escribe un número '))
        b = int(input('Escribe un número '))
        div = a / b
    except ZeroDivisionError:
        b = int(input('Escribe un número '))
        div = a / b
    
    return div
