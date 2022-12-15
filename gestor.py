#Ejercici 3

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



