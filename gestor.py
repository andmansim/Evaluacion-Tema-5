'''
Utilizando como base el ejercicio de los personajes que hicimos, en este ejercicio tendrás que crear un gestor de personajes gestor.py para añadir y borrar la información de los siguientes personajes:


Deberás hacer uso del módulo pickle y todos los cambios que realices se irán guardando en un fichero binario personajes.pckl, por lo que aunque cerremos el programa los datos persistirán.

·        Crea dos clases, una Personaje y otra Gestor.

·        La clase Personaje deberá permitir crear un personaje con el nombre (que será la clase), y sus propiedades de vida, ataque, defensa y alcance (que deben ser números enteros mayor que cero obligatoriamente).

·        Por otro lado la clase Gestor deberá incorporar todos los métodos necesarios para añadir personajes, mostrarlos y borrarlos (a partir de su nombre por ejemplo, tendrás que pensar una forma de hacerlo), además de los métodos esenciales para guardar los cambios en el fichero personajes.pckl que se deberían ejecutar automáticamente.

·        En caso de que el personaje ya exista en el Gestor entonces no se creará.

Una vez lo tengas listo realiza las siguientes prueba en tu código:

·        Crea los tres personajes de la tabla anterior y añádelos al Gestor.

·        Muestra los personajes del Gestor.

·        Borra al Arquero.

·        Muestra de nuevo el Gestor.

Sugerencia

El ejemplo con pickle que realizamos anteriormente puede servirte como base.
'''

import pickle

class Personaje():
    def __init__(self, vida, ataque, defensa, alcance):
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance

        Personaje.control(self.vida)
        Personaje.control(self.ataque)
        Personaje.control(self.defensa)
        Personaje.control(self.alcance)
        
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
        
        
            
class Gestor():
    pass

a = Personaje(3, 0, 9, 'u')
print(a.defensa, a.alcance)