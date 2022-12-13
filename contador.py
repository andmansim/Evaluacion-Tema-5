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
    