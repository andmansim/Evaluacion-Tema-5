#Creamos archivo 
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
leer()

def aniadir(inc = False, dec = False):
    if inc:
        leer1 = open('contador.txt', 'r')
        n = int(leer1.read())
        suma = open('contador.txt', 'w')
        dato = n + 1
        suma.write(f'{dato}')
        suma.close()
        leer()
    elif dec:
        resta = open('contador.txt', 'w')
        resta.write('-1')
        resta.close()
        leer()
aniadir(True, False)