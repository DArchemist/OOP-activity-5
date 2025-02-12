from modules.solid import Solid
from math import pi

class Sphere(Solid):
    def __init__(self, radius: float) -> None:
        self.radius = radius
        self.volume = self.get_volume()
        self.surface = self.get_surface()
    

    def get_volume(self):
        return 4 / 3 * pi * self.radius ** 3
    
    def get_surface(self):
        return 4 * pi * self.radius ** 2