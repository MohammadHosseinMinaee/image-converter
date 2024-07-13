from ImageFactory import ImageFactory

def main():
    factory = ImageFactory()

    # Create and calculate the size of BMP image
    bmp_image = factory.create_image('BMP', 'image.bmp', 800, 600, 0.7)
    print(f"BMP Image Size: {bmp_image.calculate_size()} bytes.")

    # Create and calculate the size of PNG image
    png_image = factory.create_image('PNG', 'image.png', 1024, 768, 100, True)
    print(f"PNG Image Size: {png_image.calculate_size()} bytes.")

    # Create and calculate the size of TGA image
    tga_image = factory.create_image('TGA', 'image.tga', 1280, 720, True, 5)
    print(f"TGA Image Size: {tga_image.calculate_size()} bytes.")

    # Create and calculate the size of TIFF image with layers saved
    tiff_image_true = factory.create_image('TIFF', 'image.tiff', 1920, 1080, 300, True, {'Author': 'John Doe', 'Professor': 'Dr. Smith'})
    print(f"TIFF Image Size with Layers Saved: {tiff_image_true.calculate_size()} bytes.")

    # Create and calculate the size of TIFF image without layers saved
    tiff_image_false = factory.create_image('TIFF', 'image.tiff', 1920, 1080, 300, False, {'Author': 'John Doe', 'Professor': 'Dr. Smith'})
    print(f"TIFF Image Size without Layers Saved: {tiff_image_false.calculate_size()} bytes.")

    # Convert TIFF image to BMP format and calculate the size
    converted_image = factory.convert_image(tiff_image_true, 'BMP', 'converted_image.bmp', 0.3)
    print(f"Converted TIFF to BMP Size: {converted_image.calculate_size()} bytes.")

if __name__ == "__main__":
    main()
