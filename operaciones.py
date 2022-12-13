#Ejercicio 1    
def suma(a, b):
    try:
        suma = a + b
    except TypeError:
        a = int(input('Escribe un número '))
        b = int(input('Escribe un número '))
        suma = a + b
    return a, b, suma

def resta(a, b):
    
    try:
        resta = a - b
    except TypeError:
        a = int(input('Escribe un número '))
        b = int(input('Escribe un número '))
        resta = a - b
    return a, b, resta

def producto(a, b):
    try:
        multi = a * b
    except TypeError:
            a = int(input('Escribe un número '))
            b = int(input('Escribe un número '))
            multi = a * b
    return a, b, multi

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
    
    return a, b, div
