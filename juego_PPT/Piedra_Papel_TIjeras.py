nombre_1 = input("Como se llamara el jugador 1?: ")
nombre_2 = input("Como se llamara el jugador 2?: ")


jugador_1 = input("Hola " + nombre_1 + "! Que eliges? piedra ,papel o tijeras?: ")
jugador_2 = input("Hola " + nombre_2 + "! Que eliges? piedra ,papel o tijeras?: ")

jugador_1.lower()
jugador_2.lower()

condicion_1 = jugador_1 == "piedra" and jugador_2 == "tijeras"
condicion_2 = jugador_1 == "papel" and jugador_2 == "papel"
condicion_3 = jugador_1 == "tijeras" and jugador_2 == "piedra"



if jugador_1 == jugador_2:
    print("Ha sido un empate entre ",nombre_1," y ",nombre_2)
elif condicion_1 or condicion_2 or condicion_3:
    print("Ha ganado",nombre_1)
else :
    print("Ha ganado", nombre_2)