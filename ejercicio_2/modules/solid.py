from abc import ABC, abstractmethod

class Solid(ABC):
    volume: float
    surface: float

    @abstractmethod
    def get_volume(self) -> float:
        pass

    @abstractmethod
    def get_surface(self) -> float:
        pass
        
