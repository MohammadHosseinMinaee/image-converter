from .base_converter import BaseConverter

class TGAConverter(BaseConverter):
    def __init__(self, width, height, atlas, pages):
        super().__init__(width, height)
        if not isinstance(atlas, bool):
            raise ValueError("Atlas flag must be a boolean.")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Pages must be a positive integer.")
        self.atlas = atlas
        self.pages = pages

    def calculate_size(self):
        # Calculate the size of the TGA image based on atlas and number of pages
        return self.width * self.height * self.pages if self.atlas else self.width * self.height
