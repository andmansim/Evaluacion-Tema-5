#Ejercicio 1
from operaciones import*

a, b, c, d = (10, 5, 0, "Hola")

a1, b1, s = suma(a, b)
print( "{} + {} = {}".format(a1, b1, s ) )
b1, d1, r = resta(a, b)
print( "{} - {} = {}".format(b1, d1, r ) )
b2, b2, p = producto(b, b)
print( "{} * {} = {}".format(b2, b2, p ) )
a2, c2, d = division(a, c)
print( "{} / {} = {}".format(a2, c2, d ) )