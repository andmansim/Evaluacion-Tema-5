#Ejercicio 4

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