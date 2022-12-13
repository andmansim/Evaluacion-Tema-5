from operaciones import*

a, b, c, d = (10, 5, 0, "Hola")

a, b, s = suma(a, b)
b, d, r = resta(a, b)
b, b, p = producto(b, b)
a, c, d = division(a, c)

print( "{} + {} = {}".format(a, b, s ) )

print( "{} - {} = {}".format(b, d, r ) )

print( "{} * {} = {}".format(b, b, p ) )

print( "{} / {} = {}".format(a, c, d ) )