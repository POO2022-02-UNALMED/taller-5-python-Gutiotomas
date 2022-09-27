class Zona:

    def __init__(self, nombre = "", zoo = None):
        self._nombre = nombre
        self._zoo = [zoo]
        self._animales = []
        
    def getNombre(self):
        return self._nombre
    
    def getZoo(self):
        return self._zoo[0]
    
    def getAnimales(self):
        return self._animales
        
    def setNombre(self, nombre):
        self._nombre = nombre
        
    def agregarAnimales(self, animal):
        self._animales.append(animal)
        animal.setZona(self)
    
    def cantidadAnimales(self):
        return len(self._animales)