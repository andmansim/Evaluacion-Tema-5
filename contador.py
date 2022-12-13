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
        suma = open('contador.txt', 'a')
        suma.write('+1')
        suma.close()
        leer()
    elif dec:
        resta = open('contador.txt', 'a')
        resta.write('-1')
        resta.close()
        leer()
aniadir(True, False)