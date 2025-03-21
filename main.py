from clases.heroe import Heroe
from clases.villano import Villano

superman = Heroe("Superman", 100,"Volar")

joker = Villano("Joker", 60,"Robar banco")

superman.identificarse()
superman.mostrar_poder()
superman.mostrar_salud()

joker.mostrar_salud()
joker.mostrar_salud()