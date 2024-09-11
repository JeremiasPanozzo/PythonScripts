import pyttsx3
from tkinter import Tk, filedialog
import threading

# Inicializar pyttsx3
engine = pyttsx3.init()
engine_running = False

def leer_texto_en_voz_alta(texto):
    """Lee el texto proporcionado en voz alta."""
    global engine_running
    engine_running = True
    engine.say(texto)
    engine.runAndWait()
    engine_running = False

def seleccionar_archivo():
    """Abre un cuadro de diálogo para seleccionar un archivo de texto."""
    Tk().withdraw()  # Ocultar la ventana principal de Tkinter
    archivo = filedialog.askopenfilename(
        title="Selecciona un archivo de texto",
        filetypes=[("Archivos de texto", "*.txt")]
    )
    return archivo

def leer_archivo(archivo):
    """Lee el contenido de un archivo de texto."""
    with open(archivo, 'r', encoding='utf-8') as f:
        return f.read()

def configurar_voz():
    """Permite al usuario configurar la velocidad y el volumen de la voz."""
    velocidad = input("Ingrese la velocidad de la voz (por defecto es 200): ")
    volumen = input("Ingrese el volumen de la voz (0.0 a 1.0, por defecto es 1.0): ")

    if velocidad.isdigit():
        engine.setProperty('rate', int(velocidad))
    if volumen.replace('.', '', 1).isdigit():
        engine.setProperty('volume', float(volumen))
        
def detener_lectura():
    """Detiene la lectura en curso."""
    global engine_running
    if engine_running:
        engine.stop()
        engine_running = False
        print("Lectura detenida.")
        
def main():
    """Función principal del programa."""
    print("Bienvenido al lector de texto en voz alta.")
    
    # Configurar voz
    configurar_voz()

    # Seleccionar archivo
    archivo = seleccionar_archivo()
    if archivo:
        print(f"Archivo seleccionado: {archivo}")
        texto = leer_archivo(archivo)
        
        # Crear un hilo para la lectura en voz alta
        hilo_lectura = threading.Thread(target=leer_texto_en_voz_alta, args=(texto,))
        hilo_lectura.start()
        
        # Permitir que el usuario detenga la lectura
        while hilo_lectura.is_alive():
            comando = input("Escribe 'stop' para detener la lectura: ")
            if comando.lower() == 'stop':
                detener_lectura()
                break
    else:
        print("No se seleccionó ningún archivo.")

if __name__ == "__main__":
    main()