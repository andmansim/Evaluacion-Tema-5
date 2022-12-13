#Creamos archivo 
try:
    open('contador.txt')
except FileNotFoundError:     
    contador = open('contador.txt', 'w')
    contador.write('0')
    contador.close()