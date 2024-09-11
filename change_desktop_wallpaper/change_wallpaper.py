import ctypes
import os
import random
import time

IMAGES_DIR = "C:\\Users\\..."
INTERVAL_DAYS = 2

def change_wallpaper(image_path):
    """Cambiar el fondo de pantalla usando la API de Windows"""
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
    
def get_image_files(directory):
    """Obtener una lista de todos los archivos de imagen en el directorio"""
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp'))]

def main():
    image_files = get_image_files(IMAGES_DIR)
    if not image_files:
        print("No se encontraron imágenes en el directorio especificado.")
        return

    while True:
        image_path = random.choice(image_files)
        change_wallpaper(image_path)
        print(f"Fondo de pantalla cambiado a: {image_path}")
        time.sleep(INTERVAL_DAYS * 86400)  # Convertir días a segundos

if __name__ == '__main__':
    main()
    