from image_formats.Png_converter import PNGConverter
from image_formats.Bmp_converter import BMPConverter
from image_formats.Tga_converter import TGAConverter
from image_formats.Tiff_converter import TIFFConverter

class ImageFactory:
    def __init__(self):
        # Dictionary to map format names to their corresponding converter classes
        self.converters = {
            'BMP': BMPConverter,
            'PNG': PNGConverter,
            'TGA': TGAConverter,
            'TIFF': TIFFConverter
        }

    def create_image(self, format_name, width, height, *params):
        # Get the converter class based on the format name
        converter_class = self.converters.get(format_name)
        if not converter_class:
            raise ValueError(f"Unsupported image format: {format_name}")
        # Return an instance of the converter class
        return converter_class(width, height, *params)

    def convert_image(self, image, new_format, *params):
        # Get the converter class for the new format
        if new_format not in self.converters:
            raise ValueError(f"Unsupported destination format: {new_format}")
        new_converter_class = self.converters[new_format]
        # Create a new image using the new converter class
        return new_converter_class(image.width, image.height, *params)
