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
      print("Menú\n 1. Registrar usuario\n 2. Eliminar usuario por id\n 3. Actualizar usuario por id\n 4. Ver usuarios\n 5. Salir")
      opcion = input("Ingresa una opción")
      if opcion == '1':
        if os.path.exists("archivo.txt"):
          archivo = open("archivo.txt", "r")
          lineas = archivo.readlines()
          archivo.close()
          if lineas:
            self.id += 1
            self.registrarUsuario()
          else:
            self.id = 1
            self.registrarUsuario()
        else:
          archivo = open("archivo.txt", "x")
          self.registrarUsuario()
      elif opcion == '2':
        self.id -= 1
        self.eliminarUsuario()
      elif opcion == '3':
        self.actualizarUsuario()
      elif opcion == '4':
        self.verUsuarios()
      elif opcion == '5':
        print("Saliste del programa")
        break
      else:
        print("Opción inválida. Vuelve a intentarlo")

  def registrarUsuario(self):
    datosValidos = self.ingresarDatos()
    if datosValidos == True:
      archivo = open("archivo.txt", "a")
      archivo.write(f"{self.id} {self.nombre} {self.apellido} {self.correo} {self.telefono}\n")
      archivo.close()
      print("El usuario se ha registrado con éxito")
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
    else:
      print("Vuelve a intentarlo")

  def eliminarUsuario(self):
    try:
      if os.path.exists("archivo.txt"):
        archivo = open("archivo.txt", "r")
        lineas = archivo.readlines()
        archivo.close()
        if lineas:
          id = int(input("Ingresa el id del usuario"))
          if 0 < id <= len(lineas):
            archivo = open("archivo.txt", "r")
            lineas.pop(id - 1)
            archivo.close()
            print("Usuario eliminado correctamente")
            #Cambia el resto de los id
            i = 0
            while i < len(lineas):
              if i >= id-1:
               lineas[i] = lineas[i].replace(f"{i+2}", f"{i+1}", 1)
               i += 1
            #Actualiza el archivo
            archivo = open("archivo.txt", "w")
            archivo.writelines(lineas)
            archivo.close()
          else:
            print("id no válido")
            archivo.close()
        else:
          print("No hay usuarios registrados")
      else:
        print("No existe el archivo. Registra un usuario para crearlo")
    except Exception as e:
      print(f"Error inesperado: {e}")

  def actualizarUsuario(self):
    try:
      if os.path.exists("archivo.txt"):
        archivo = open("archivo.txt", "r")
        lineas = archivo.readlines()
        archivo.close()
        if lineas:
          id = int(input("Ingresa el id del usuario"))
          if 0 < id <= len(lineas):
            print("Ingresa los nuevos datos del usuario")
            datosValidos = self.ingresarDatos()
            if datosValidos == True:
              archivo = open("archivo.txt", "r")
              lineas[id - 1] = f"{id} {self.nombre} {self.apellido} {self.correo} {self.telefono}\n"
              archivo.close()
              print("Usuario actualizado correctamente")
              #Actualiza el archivo
              archivo = open("archivo.txt", "w")
              archivo.writelines(lineas)
              archivo.close()
            else:
              print("Vuelve a intentarlo")
          else:
            print("id no válido")
            archivo.close()
        else:
          print("No hay usuarios registrados")
      else:
        print("No existe el archivo. Registra un usuario para crearlo")
    except Exception as e:
      print(f"Error inesperado: {e}")
    
  def verUsuarios(self):
    if os.path.exists("archivo.txt"):
      archivo = open("archivo.txt", "r")
      lineas = archivo.readlines()
      archivo.close()
      if lineas:
        archivo = open("archivo.txt", "r")
        print(archivo.read())
        archivo.close()
      else:
        print("No hay usuarios registrados")
    else:
      print("No existe el archivo. Registra un usuario para crearlo")
    
  def ingresarDatos(self):
    patron1 = r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ]{2,}$'  
    patron2 = r'^[a-zA-Z0-9_.-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]+$' 
    patron3 = r'^[\+\s-]?\d{10,15}$'
    self.nombre = input("Ingresa el nombre del usuario").strip()
    self.apellido = input("Ingresa el apellido del usuario").strip()
    if re.search(patron1, self.nombre) and re.search(patron1, self.apellido):
      self.correo = input("Ingresa el correo del usuario").strip()
      if re.search(patron2, self.correo):
        self.telefono = input("Ingresa el telefono del usuario").strip()
        if re.search(patron3, self.telefono):
          print("Los datos se han validado")
          return True
        else:
          print("Telefono no válido. Solo se permiten números, espacios, + y -")
          return False
      else:
        print("Correo no válido. Debe tener un formato correcto")
        return False
    else:
      print("Nombre y apellido no válidos. Solo se permiten letras, mínimo 2")
      return False

ejecutar = Programa()
ejecutar.mostrarMenu()