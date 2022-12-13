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
def control_errores(num1, num2):
    if not isinstance(num1, float) or not isinstance(num1, int):
        a = input('Introduce un número ')
        control_errores(a, num2)
    elif not isinstance(num2, float) or not isinstance(num2, int):    
        a = input('Introduce un número ')
        control_errores(a, num2)
    else:
        return num1, num2


def sumar(a, b):
    a, b =control_errores(a, b)
    suma = a + b
    return suma

def resta(a, b):
    a, b =control_errores(a, b)
    if a > b:
        resta = a - b
    else:
        resta = b - a
    return resta

def producto(a, b):
    a, b =control_errores(a, b)
    multi = a * b
    return multi

def division(a, b):
    a, b =control_errores(a, b)
    div = a / b
    return div

numero1 = input('Introduce un número ')
numero2 = input('Introdice otro número')
s = sumar(numero1, numero2)