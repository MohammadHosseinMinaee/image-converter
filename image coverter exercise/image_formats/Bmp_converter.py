from .base_converter import BaseConverter

class BMPConverter(BaseConverter):
    def __init__(self, width, height, quality):
        super().__init__(width, height)
        if not (0.0 <= quality <= 1.0):
            raise ValueError("Quality must be between 0.0 and 1.0.")
        self.quality = quality

    def calculate_size(self):
        # Calculate the size of the BMP image based on quality
        return int(self.width * self.height * self.quality)
