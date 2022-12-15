# Evaluacion-Tema-5
Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/andmansim/Evaluacion-Tema-5.git)
https://github.com/andmansim/Evaluacion-Tema-5.git

He realizado 4 ejercicios: calculos, ficheros y relojes.
Mi código es el siguiente:

# Ejercicio 1
```
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



a, b, c, d = (10, 5, 0, "Hola")

a1, b1, s = suma(a, b)
print( "{} + {} = {}".format(a1, b1, s ) )
b1, d1, r = resta(a, b)
print( "{} - {} = {}".format(b1, d1, r ) )
b2, b2, p = producto(b, b)
print( "{} * {} = {}".format(b2, b2, p ) )
a2, c2, d = division(a, c)
print( "{} / {} = {}".format(a2, c2, d ) )
```

# Ejercicio 2
```
def leer():
    try:
        open('contador.txt')  
    except FileNotFoundError:     
        contador = open('contador.txt', 'w')
        contador.write('0')
        contador.close()

    #Leemos el archivo 
    leer = open('contador.txt', 'r') 
    contenido = leer.read()
    print(contenido)
    leer.close()

#Añadir o quitar datos
def aniadir(inc = False, dec = False):
    leer1 = open('contador.txt', 'r')
    n = int(leer1.read())
    if inc:
        suma = open('contador.txt', 'w')
        dato = n + 1
        suma.write(f'{dato}')
        suma.close()
        leer()
    elif dec:
        resta = open('contador.txt', 'w')
        dato = n - 1
        resta.write(f'{dato}')
        resta.close()
        leer()
    else:
        leer()

print('Dato actual')
leer()
print('\nAñadimos uno')
aniadir(True, False)
print('\nQuitamos uno')
aniadir(False, True)
print('\nNo hacemos nada')
aniadir(False, False)
```

# Ejercicio 3
```
import pickle

class Personaje():
    def __init__(self, vida, ataque, defensa, alcance):
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance

        self.vida = Personaje.control(self.vida)
        self.ataque = Personaje.control(self.ataque)
        self.defensa = Personaje.control(self.defensa)
        self.alcance = Personaje.control(self.alcance)
        
    def control(dato):
        if isinstance(dato, int):
            if dato > 0:
                pass
            else:
                print('El valor es menor que cero')
                dato = int(input('Introduce un número mayor que cero '))
        else:
            print('El dato tiene que ser numérico')
            dato = int(input('Introduce un número mayor que cero '))
        return dato
    def datos(self):
        v = f'Vida: {self.vida} '
        at = f'Ataque: {self.ataque} '
        d = f'Defensa: {self.defensa} '
        al = f'Alcance: {self.alcance} '
        return v + at +  d + al
        
            
class Gestor():
    
    def __init__(self):
        self.datos= []
    def añadir(self, d):
        self.d = d
        fichero = open('personajes.pckl', 'wb')
        self.datos.append(self.d)
        pickle.dump(self.datos, fichero)
        fichero.close()
    def leer(self):
        fichero = open('personajes.pckl', 'rb')
        print(pickle.load(fichero))
        fichero.close()
    def borrar(self, dato):
        fichero = open('personajes.pckl', 'wb')
        for i in self.datos:
            if dato in i:
                self.datos.remove(i)
        pickle.dump(self.datos, fichero)
        fichero.close()
        
        
caballero = Personaje(4, 2, 4, 2)
c = 'Caballero ' + caballero.datos()
guerrero = Personaje(2, 4, 2, 4)
g = 'Guerero ' + guerrero.datos()
arquero = Personaje(2, 4, 1, 8)
a = 'Arquero ' + arquero.datos()
gest = Gestor()
gest.añadir(c)
gest.añadir(g)
gest.añadir(a)
print('Leemos fichero')
gest.leer()
gest.borrar('Arquero')
print('\nBorramos Arquero')
gest.leer()
```

# Ejercicio 4
```
import time
import os 

def hora_ac():
    tiempo = time.strftime("%H:%M:%S")
    os.system('cls')
    print('Hora actual:', tiempo)
    
hora_ac()
while True: 
    hora_ac()
    time.sleep(1)
```
