from cryptography.fernet import Fernet

#guardar y escribir clave
def generar_clave():
    clave= Fernet.generate_key()
    with open("clave.key", "wb") as archivo_clave:
        archivo_clave.write(clave)


def cargar_clave():
    return open("clave.key", "rb").read()


#generamos la clave
generar_clave()

#guardamos la clave en una variable
clave= cargar_clave()

#confirmamos si tenemos la clave no valla a ser que no se guarde y yo encriptando sin ella
print(clave)

#encriptaremos un mensaje
mensaje= "oh no, i drop my password, contrasena123".encode()
print(mensaje)

#fernet permite que no se lea el mensaje sin la clave
fer= Fernet(clave)
#encriptamos
encriptado= fer.encrypt(mensaje)

#sigan viendo
print(encriptado)

#desencriptar
desencriptado= fer.decrypt(encriptado)

print(mensaje)