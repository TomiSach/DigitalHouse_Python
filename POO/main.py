class Perro:
    def __init__(self,nombre , edad) :
        self.nombre = nombre
        self.edad = edad 
    
    def ladrar(self):
        return "Guau"
    
perro1 = Perro("Loki",4)

perro2 = Perro("Alaska",5)

print(f"{perro1.nombre} tiene {perro1.edad} y dice {perro1.ladrar()}")