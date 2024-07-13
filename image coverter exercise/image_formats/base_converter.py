from abc import ABC, abstractmethod

class BaseConverter(ABC):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive values.")
        self.width = width
        self.height = height

    @abstractmethod
    def calculate_size(self):
        # Abstract method to calculate file size, to be implemented by subclasses
        pass
