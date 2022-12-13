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
aniadir(True, False)
aniadir(False, True)