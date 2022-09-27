from zooAnimales.animal import Animal

class Zona: 
    
    def __init__(self, nombre=None, zoo=None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = []
     
    def getNombre(self):
        return self._nombre 
    
    def setNombre(self, nombre):
        self._nombre = nombre
        
    def getZoo(self):
        return self._zoo
    
    def setZoo(self, zoo):
        self._zoo = zoo
        
    def getAnimaels(self):
        return self._animales
    
    def setAnimaels(self, animales):
        self._animales = animales
         
    def agregarAnimales(self, animal):
        if isinstance(animal, Animal):
            self._animales.append(animal)
    
    def cantidadAnimales(self):
        return len(self._animales)
    
    def cantidadTotalAnimales(self):
        return len(self._animales)