import random

numero_secreto =  random.randint(0,100)
adivinado = False 
cant_max_intentos = 5
cant_intentos = 0



print("Bienvenido al juego de adivinar el numero secreto!")

while not adivinado and cant_intentos < cant_max_intentos:

    numero = int(input("Intorduce un numero del 1 al 99: ")) 

    if numero == numero_secreto:
        print("Felicitaciones has adivinado el numero ")
    elif numero < numero_secreto:
        print("El numero es mayor al ingresado")
    else :
        print("EL numero es menor al numero ingresado")

    cant_intentos += 1
if not cant_intentos < cant_max_intentos:
    print("Game Over!, No has podido adivinar el numero dentro de los 5 intentos")

    
