import sys
from .base_converter import BaseConverter

class TIFFConverter(BaseConverter):
    def __init__(self, width, height, dpi, save_layers, metadata):
        super().__init__(width, height)
        if dpi <= 0:
            raise ValueError("DPI must be a positive value.")
        if not isinstance(metadata, dict):
            raise ValueError("Metadata must be a dictionary.")
        self.dpi = dpi
        self.save_layers = save_layers
        self.metadata = metadata

    def calculate_size(self):
        # Calculate the base size of the TIFF image based on DPI and metadata size
        base_size = self.width * self.height * self.dpi * sys.getsizeof(self.metadata)
        # Add additional size if layers are saved
        layer_size = 10000 if self.save_layers else 0
        return base_size + layer_size
