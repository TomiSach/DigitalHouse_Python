########      POO
##from clases.heroe import Heroe
##from clases.villano import Villano

##superman = Heroe("Superman", 100,"Volar")

##joker = Villano("Joker", 60,"Robar banco")

##superman.identificarse()
##superman.mostrar_poder()
##superman.mostrar_salud()

##joker.mostrar_salud()
##joker.mostrar_salud()



###########     POLIMORFISMO
#from clases_animales.perro import Perro
#from clases_animales.gato import Vaca
#from clases_animales.Vaca import Gato


#def hacer_sonido_de_animal(animal):
#    print(animal.hacer_sonido())

#perro = Perro("Alaska")
#vaca = Vaca("Lola")
#Gato = Gato("Coco")

#hacer_sonido_de_animal(perro)
#hacer_sonido_de_animal(Gato)
#hacer_sonido_de_animal(vaca)


## Encapsulamiento

from Encapsulamiento.cuenta_bancaria import CuentaBancaria

##creamos instancia con dinero
cuenta = CuentaBancaria("Sergie Code",1000)

##obtener saldo inicial
print(cuenta.obtener_saldo())

##agregamos 5000 y volver a obtener saldo
cuenta.depositar(500)
print(cuenta.obtener_saldo())

##retirar 1000 y volver a obtener saldo
cuenta.retirar(1000)
print(cuenta.obtener_saldo)