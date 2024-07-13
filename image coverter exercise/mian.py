from ImageFactory import ImageFactory

def main():
    factory = ImageFactory()

    # Create and calculate size of BMP image
    bmp_image = factory.create_image('BMP', 640, 480, 0.5)
    print(f"BMP Image Size: {bmp_image.calculate_size()} bytes.")

    # Create and calculate size of PNG image
    png_image = factory.create_image('PNG', 800, 600, 80, False)
    print(f"PNG Image Size: {png_image.calculate_size()} bytes.")

    # Create and calculate size of TGA image
    tga_image = factory.create_image('TGA', 400, 300, True, 7)
    print(f"TGA Image Size: {tga_image.calculate_size()} bytes.")

    # Create and calculate size of TIFF image
    tiff_image = factory.create_image('TIFF', 1024, 768, 300, False, {'Author': 'Mohammad Hossein Minaee', 'Professor': 'Dr. Pourya Khanzadi'})
    print(f"TIFF Image Size: {tiff_image.calculate_size()} bytes.")

    # Convert TIFF image to BMP format and calculate size
    converted_image = factory.convert_image(tiff_image, 'BMP', 0.2)
    print(f"Converted TIFF to BMP Size: {converted_image.calculate_size()} bytes.")

if __name__ == "__main__":
    main()
