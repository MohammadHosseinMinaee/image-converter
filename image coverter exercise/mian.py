from ImageFactory import ImageFactory

def main():
    factory = ImageFactory()

    # ایجاد و محاسبه اندازه تصویر BMP
    bmp_image = factory.create_image('BMP', 'path/to/your/image.bmp', 800, 600, 0.7)
    print(f"BMP Image Size: {bmp_image.calculate_size()} bytes.")

    # ایجاد و محاسبه اندازه تصویر PNG
    png_image = factory.create_image('PNG', 'path/to/your/image.png', 1024, 768, 100, True)
    print(f"PNG Image Size: {png_image.calculate_size()} bytes.")

    # ایجاد و محاسبه اندازه تصویر TGA
    tga_image = factory.create_image('TGA', 'path/to/your/image.tga', 1280, 720, True, 5)
    print(f"TGA Image Size: {tga_image.calculate_size()} bytes.")

    # ایجاد و محاسبه اندازه تصویر TIFF با لایه‌ها
    tiff_image_true = factory.create_image('TIFF', 'path/to/your/image.tiff', 1920, 1080, 300, True, {'Author': 'Mohammad Hossein Minaee', 'Professor': 'Dr. Pourya Khanzadi'})
    print(f"TIFF Image Size with Layers Saved: {tiff_image_true.calculate_size()} bytes.")

    # ایجاد و محاسبه اندازه تصویر TIFF بدون لایه‌ها
    tiff_image_false = factory.create_image('TIFF', 'path/to/your/image.tiff', 1920, 1080, 300, False, {'Author': 'Mohammad Hossein Minaee', 'Professor': 'Dr. Pourya Khanzadi'})
    print(f"TIFF Image Size without Layers Saved: {tiff_image_false.calculate_size()} bytes.")

    # تبدیل تصویر TIFF به فرمت BMP و محاسبه اندازه
    converted_image = factory.convert_image(tiff_image_true, 'BMP', 'path/to/your/converted_image.bmp', 0.3)
    print(f"Converted TIFF to BMP Size: {converted_image.calculate_size()} bytes.")

if __name__ == "__main__":
    main()
