from cryptography.fernet import Fernet
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox

# Variable global para el objeto Fernet
fer = None

# Función para generar y guardar una clave
def generar_clave():
    nombre = nombre_clave.get().strip()
    if not nombre:
        messagebox.showerror("Error", "Por favor, ingresa un nombre para la clave.")
        return

    archivo_clave = f"{nombre}.key"
    clave = Fernet.generate_key()
    try:
        with open(archivo_clave, "wb") as archivo:
            archivo.write(clave)
        messagebox.showinfo("Éxito", f"Clave generada y guardada como '{archivo_clave}'.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar la clave: {e}")

# Función para cargar una clave desde un archivo
def cargar_clave():
    global fer
    archivo = askopenfilename(title="Selecciona un archivo de clave", filetypes=[("Archivos de clave", "*.key")])
    if archivo:
        try:
            with open(archivo, "rb") as file:
                clave = file.read()
            fer = Fernet(clave)
            messagebox.showinfo("Éxito", f"Clave '{archivo}' cargada exitosamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar la clave: {e}")
    else:
        messagebox.showwarning("Advertencia", "No seleccionaste un archivo de clave.")

# Función para encriptar un archivo
def encriptar():
    if not fer:
        messagebox.showerror("Error", "Cargue una clave antes de encriptar.")
        return

    archivo = askopenfilename(title="Selecciona un archivo para encriptar")
    if archivo:
        try:
            with open(archivo, "rb") as file:
                archivo_info = file.read()
            encripted_data = fer.encrypt(archivo_info)
            with open(archivo, "wb") as file:
                file.write(encripted_data)
            messagebox.showinfo("Éxito", f"Archivo '{archivo}' encriptado exitosamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo encriptar el archivo: {e}")
    else:
        messagebox.showwarning("Advertencia", "No seleccionaste un archivo para encriptar.")

# Función para desencriptar un archivo
def desencriptar():
    if not fer:
        messagebox.showerror("Error", "Cargue una clave antes de desencriptar.")
        return

    archivo = askopenfilename(title="Selecciona un archivo para desencriptar")
    if archivo:
        try:
            with open(archivo, "rb") as file:
                archivo_info = file.read()
            decrypted_data = fer.decrypt(archivo_info)
            with open(archivo, "wb") as file:
                file.write(decrypted_data)
            messagebox.showinfo("Éxito", f"Archivo '{archivo}' desencriptado exitosamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo desencriptar el archivo: {e}")
    else:
        messagebox.showwarning("Advertencia", "No seleccionaste un archivo para desencriptar.")

# Inicializar la ventana principal
root = Tk()
root.title("Encriptador/Desencriptador")

# Diseño de la interfaz
frame = Frame(root, padx=10, pady=10)
frame.pack()

Label(frame, text="Nombre de la clave:").grid(row=0, column=0, sticky=W)
nombre_clave = Entry(frame, width=30)
nombre_clave.grid(row=0, column=1, pady=5)

Button(frame, text="Generar Clave", command=generar_clave).grid(row=1, column=0, columnspan=2, pady=5)

Button(frame, text="Cargar Clave", command=cargar_clave).grid(row=2, column=0, columnspan=2, pady=5)

Button(frame, text="Encriptar Archivo", command=encriptar).grid(row=3, column=0, columnspan=2, pady=5)

Button(frame, text="Desencriptar Archivo", command=desencriptar).grid(row=4, column=0, columnspan=2, pady=5)

# Iniciar el bucle principal de la interfaz
root.mainloop()
