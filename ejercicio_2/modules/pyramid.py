from modules.solid import Solid
from math import pi

class Pyramid(Solid):
    def __init__(self, base: float, height: float, apothem: float) -> None:
        self.base = base
        self.height = height
        self.apothem = apothem
        self.volume = self.get_volume()
        self.surface = self.get_surface()
    

    def get_volume(self):
        return (self.height * self.base ** 2) / 3
    
    def get_surface(self):
        base_area: float = self.base ** 2
        sides_area: float = 2 * self.base * self.apothem
        return base_area + sides_area