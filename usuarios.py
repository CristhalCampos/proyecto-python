import re
import os
import pywhatkit as kit
import time
import ssl
import smtplib
from email.message import EmailMessage

class Programa:
  def __init__(self):
    self.nombre = ""
    self.apellido = ""
    self.correo = ""
    self.telefono = ""
    self.id = 1

  def mostrarMenu(self):
    while True:
      print("Menú\n 1. Registrar un usuario\n 2. Eliminar un usuario por su id\n 3. Actualizar un usuario por su id\n 4. Ver todos los usuarios\n 5. Eliminar todos los usuarios\n 6. Salir\n")
      opcion = input("Ingresa una opción\n").strip()
      if opcion == '1':
        self.registrarUsuario()
      elif opcion == '2':
        self.eliminarUsuario()
      elif opcion == '3':
        self.actualizarUsuario()
      elif opcion == '4':
        self.verUsuarios()
      elif opcion == '5':
        self.eliminarUsuarios()
      elif opcion == '6':
        print("Saliste del programa")
        break
      else:
        print("Opción inválida. Vuelve a intentarlo")

  def registrarUsuario(self):
    try:
      if self.ingresarDatos():
        if os.path.exists("archivo.txt"):
          with open("archivo.txt", "r") as archivo:
            lineas = archivo.readlines()
          if lineas:
            self.id = len(lineas) + 1
          else:
            self.id = 1
        else:
          self.id = 1
        with open("archivo.txt", "a") as archivo:
          archivo.write(f"{self.id} {self.nombre} {self.apellido} {self.correo} {self.telefono}\n")
        print("El usuario se ha registrado con éxito") 
      else:
        print("Datos no válidos. Vuelve a intentarlo")
    except Exception as e:
      print(f"Error inesperado: {e}")    

  def eliminarUsuario(self):
    try:
      if os.path.exists("archivo.txt"):
        with open("archivo.txt", "r") as archivo:
          lineas = archivo.readlines()
        if lineas:
          id = int(input("Ingresa el id del usuario\n").strip())
          if 0 < id <= len(lineas):
            lineas.pop(id - 1)
            print("Usuario eliminado correctamente")
            #Cambia el resto de los id
            for i in range(len(lineas)):
              if i >= id-1:
                lineas[i] = lineas[i].replace(f"{i+2}", f"{i+1}", 1)
            #Actualiza el archivo
            with open("archivo.txt", "w") as archivo:
              archivo.writelines(lineas)
          else:
            print("id no válido")
        else:
          print("No hay usuarios registrados")
      else:
        print("No existe el archivo de usuarios. Registra un usuario para crearlo")
    except Exception as e:
      print(f"Error inesperado: {e}")

  def actualizarUsuario(self):
    try:
      if os.path.exists("archivo.txt"):
        with open("archivo.txt", "r") as archivo:
          lineas = archivo.readlines()
        if lineas:
          id = int(input("Ingresa el id del usuario\n").strip())
          if 0 < id <= len(lineas):
            print("Ingresa los nuevos datos del usuario")
            datosValidos = self.ingresarDatos()
            if datosValidos:
              lineas[id - 1] = f"{id} {self.nombre} {self.apellido} {self.correo} {self.telefono}\n"
              print("Usuario actualizado correctamente")
              #Actualiza el archivo
              with open("archivo.txt", "w") as archivo:
                archivo.writelines(lineas)
            else:
              print("Vuelve a intentarlo")
          else:
            print("id no válido")
        else:
          print("No hay usuarios registrados")
      else:
        print("No existe el archivo de usuarios. Registra un usuario para crearlo")
    except Exception as e:
      print(f"Error inesperado: {e}")
    
  def verUsuarios(self):
    try:
      if os.path.exists("archivo.txt"):
        with open("archivo.txt", "r") as archivo:
          lineas = archivo.readlines()
        if lineas:
          for linea in lineas:
            print(linea.strip())
        else:
          print("No hay usuarios registrados")
      else:
        print("No existe el archivo de usuarios. Registra un usuario para crearlo")
    except Exception as e:
        print(f"Error inesperado: {e}")

  def eliminarUsuarios(self):
    try:
      if os.path.exists("archivo.txt"):
        archivo = open("archivo.txt", "r")
        lineas = archivo.readlines()
        archivo.close()
        if lineas:
          os.remove("archivo.txt")
          print("Todos los usuarios han sido eliminados")
          self.id = 1
        else:
          print("No hay usuarios registrados que eliminar")
      else:
        print("No existe el archivo de usuarios que eliminar")
    except Exception as e:
        print(f"Error inesperado: {e}")
    
  def ingresarDatos(self):
    patron1 = r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ]{2,}$'  
    patron2 = r'^[a-zA-Z0-9_.-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]+$' 
    patron3 = r'^[\+\s-]?\d{10,15}$'
    intentos = 3
    datosValidos = False
    #Valida nombre
    for intento in range(intentos):
      self.nombre = input("Ingresa el nombre del usuario\n").strip()
      if re.search(patron1, self.nombre):
        #Valida apellido
        for intento in range(intentos):
          self.apellido = input("Ingresa el apellido del usuario\n").strip()
          if re.search(patron1, self.apellido):
            #Valida correo
            for intento in range(intentos):
              self.correo = input("Ingresa el correo del usuario\n").strip()
              if re.search(patron2, self.correo):
                #Valida telefono
                for intento in range(intentos):
                  self.telefono = input("Ingresa el telefono del usuario\n").strip()
                  if re.search(patron3, self.telefono):
                    datosValidos = True
                    break
                  else:
                    datosValidos = False
                    print(f"Telefono no válido. Solo se permiten números (mínimo 10, máximo 15). Opcional: espacios, + y -\n Intento: {intento+1}/{intentos}")
                break
              else:
                print(f"Correo no válido. El correo debe tener un formato correcto\n Intento: {intento+1}/{intentos}")
            break
          else:
            print(f"Apellido no válido. Solo se permiten letras (mínimo 2)\n Intento: {intento+1}/{intentos}")
        break
      else:
        print(f"Nombre no válido. Solo se permiten letras (mínimo 2)\n Intento: {intento+1}/{intentos}")
    
    if datosValidos:
      return True
    else:
      return False
  
  def enviarBienvenida():
    """
      #Crea email
      email = EmailMessage()
      email['From'] = "camposcristhal@gmail.com"
      email['To'] = self.correo
      email['Subject'] = "Bienvenida"
      email.set_content("Este es un correo de bienvenida")
      #Inicia sesión e envía email
      with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context()) as smtp:
        smtp.login("camposcristhal@gmail.com", "upcb bsze witr zoec")
        smtp.sendmail("camposcristhal@gmail.com", self.correo, email.as_string())
      #Envía whatsapp
      mensaje = "Este es un mensaje de bienvenida"
      kit.sendwhatmsg_instantly(self.telefono, mensaje, 20, True)
      time.sleep(10)
    """

ejecutar = Programa()
ejecutar.mostrarMenu()