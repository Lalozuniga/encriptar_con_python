from cryptography.fernet import Fernet
from tkinter import *
from tkinter.filedialog import askopenfilename

# guardar y escribir clave
def generar_clave():
    clave = Fernet.generate_key()
    with open("clave.key", "wb") as archivo_clave:
        archivo_clave.write(clave)


def cargar_clave():
    return open("clave.key", "rb").read()


# generamos la clave
#generar_clave()
# guardamos la clave en una variable
clave = cargar_clave()

# fernet permite que no se lea el mensaje sin la clave
fer = Fernet(clave)

#encriptar el archivo
def encript(archivo,fer):
    try:
        with open(archivo, "rb") as file:
            archivo_info = file.read()
        encripted_data = fer.encrypt(archivo_info)
        with open(archivo, "wb") as file:
            file.write(encripted_data)
        print(f"Archivo '{archivo}' encriptado exitosamente.")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo}'.")
    except Exception as e:
        print(f"Error al encriptar el archivo: {e}")


def desencript(archivo,fer):
    try:
        with open(archivo, "rb") as file:
            archivo_info = file.read()
        decrypted_data = fer.decrypt(archivo_info)
        with open(archivo, "wb") as file:
            file.write(decrypted_data)
        print(f"Archivo '{archivo}' desencriptado exitosamente.")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo}'.")
    except Exception as e:
        print(f"Error al desencriptar el archivo: {e}")

def seleccionar_archivo():
    Tk().withdraw()  # Ocultar la ventana principal de tkinter
    archivo = askopenfilename(title="Selecciona un archivo")  # Abrir cuadro de diálogo
    return archivo


accion = input("selecciona 1 si quieres encriptar \nselecciona 2 si quieres desencriptar\nOpción:")

if accion == "1":
    archivo = seleccionar_archivo()
    if archivo:
        encript(archivo, fer)
    else:
        print("No se seleccionó ningún archivo. Saliendo del programa.")
elif accion == "2":
    archivo = seleccionar_archivo()
    if archivo:
        desencript(archivo, fer)
    else:
        print("No se seleccionó ningún archivo. Saliendo del programa.")
else:
    print("Opción no válida. Saliendo del programa.")