##from clases.heroe import Heroe
##from clases.villano import Villano

##superman = Heroe("Superman", 100,"Volar")

##joker = Villano("Joker", 60,"Robar banco")

##superman.identificarse()
##superman.mostrar_poder()
##superman.mostrar_salud()

##joker.mostrar_salud()
##joker.mostrar_salud()

from clases_animales.perro import Perro
from clases_animales.gato import Vaca
from clases_animales.Vaca import Gato


def hacer_sonido_de_animal(animal):
    print(animal.hacer_sonido())

perro = Perro("Alaska")
vaca = Vaca("Lola")
Gato = Gato("Coco")

hacer_sonido_de_animal(perro)
hacer_sonido_de_animal(Gato)
hacer_sonido_de_animal(vaca)