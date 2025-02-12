from modules.solid import Solid
from math import pi

class Cylinder(Solid):
    def __init__(self, radius: float, height: float) -> None:
        self.radius = radius
        self.height = height
        self.volume = self.get_volume()
        self.surface = self.get_surface()
    

    def get_volume(self):
        return pi * self.height * self.radius ** 2
    
    def get_surface(self):
        bases: float = 2 * pi * self.radius ** 2
        side: float = 2 * pi * self.radius * self.height
        return bases + side