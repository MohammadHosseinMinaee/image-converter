from .base_converter import BaseConverter

class PNGConverter(BaseConverter):
    def __init__(self, width, height, dpi, interlaced):
        super().__init__(width, height)
        if dpi <= 0:
            raise ValueError("DPI must be a positive value.")
        if not isinstance(interlaced, bool):
            raise ValueError("Interlaced flag must be a boolean.")
        self.dpi = dpi
        self.interlaced = interlaced

    def calculate_size(self):
        # Calculate the size of the PNG image based on DPI and interlacing
        size = self.width * self.height * self.dpi
        return int(size / 2) if self.interlaced else int(size)
