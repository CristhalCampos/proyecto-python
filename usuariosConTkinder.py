from tkinter import Tk, Frame, Button, Label, Entry
import re
import os

class Usuarios(Frame):
  def __init__(self, master=None):
    super().__init__(master, width=1000, height=720)
    self.master = master
    self.pack()
    self.crearButton()
    self.crearLabel()
    self.crearEntry()
    self.nombre = ""
    self.apellido = ""
    self.correo = ""
    self.telefono = ""
    self.id = 1

  def crearButton(self):
    self.button1 = Button(self, text="Registrar", bg="blue", fg="white", command=self.registrarUsuario)
    self.button1.place(x=450, y=230, width=100, height=30)
    self.button2 = Button(self, text="Eliminar", bg="blue", fg="white", command=self.eliminarUsuario)
    self.button2.place(x=80, y=490, width=100, height=30)
    self.button3 = Button(self, text="Actualizar", bg="blue", fg="white", command=self.actualizarUsuario)
    self.button3.place(x=230, y=490, width=100, height=30)
    self.button4 = Button(self, text="Ver", bg="blue", fg="white", command=self.verUsuarios)
    self.button4.place(x=630, y=380, width=80, height=30)

  def crearLabel(self):
    self.label1 = Label(self, text="Registra un usuario", font="Times 20")
    self.label1.place(x=350, y=30, width=300, height=30)
    self.label2 = Label(self, text="Elimina o actualiza\n un usuario", font="Times 20")
    self.label2.place(x=55, y=330, width=300, height=50)
    self.label3 = Label(self, text="ID del usuario")
    self.label3.place(x=155, y=400, width=100, height=20)
    self.label3 = Label(self, text="Si vas a actualizar,\n escribe los nuevos datos\n antes de darle al botón", fg="red")
    self.label3.place(x=200, y=530, width=160, height=40)
    self.label4 = Label(self, text="Ver usuarios", font="Times 20")
    self.label4.place(x=570, y=330, width=200, height=30)
    self.nombreValido = Label(self, text="Solo se permiten letras\n (mínimo 2)", fg="red")
    self.nombreValido.place(x=60, y=175, width=200, height=40)
    self.apellidoValido = Label(self, text="Solo se permiten letras\n (mínimo 2)", fg="red")
    self.apellidoValido.place(x=285, y=175, width=200, height=40)
    self.correoValido = Label(self, text="El correo debe tener (@.)\n un formato correcto", fg="red")
    self.correoValido.place(x=510, y=175, width=200, height=40)
    self.telefonoValido = Label(self, text="Solo se permiten números, + y -\n (mínimo 10, máximo 15)", fg="red")
    self.telefonoValido.place(x=735, y=175, width=200, height=40)
    self.mostrarMensaje1 = Label(self, text="", fg="red")
    self.mostrarMensaje1.place(x=350, y=270, width=300, height=20)
    self.mostrarMensaje2 = Label(self, text="", fg="red")
    self.mostrarMensaje2.place(x=60, y=530, width=130, height=40)
    self.mostrarMensaje3 = Label(self, text="", fg="red")
    self.mostrarMensaje3.place(x=190, y=580, width=180, height=20)
    self.mostrarMensaje4 = Label(self, text="", fg="red")
    self.mostrarMensaje4.place(x=595, y=420, width=150, height=20)
    self.mostrarUsuarios = Label(self, text="", justify="left")  #Label para mostrar usuarios
    self.mostrarUsuarios.place(x=470, y=450, width=400, height=200)
    self.nombre = Label(self, text="Datos del usuario", font="Times 16")
    self.nombre.place(x=425, y=80, width=150, height=20)
    self.nombre = Label(self, text="Nombre")
    self.nombre.place(x=110, y=110, width=100, height=20)
    self.apellido = Label(self, text="Apellido")
    self.apellido.place(x=335, y=110, width=100, height=20)
    self.correo = Label(self, text="Correo")
    self.correo.place(x=560, y=110, width=100, height=20)
    self.telefono = Label(self, text="Telefono")
    self.telefono.place(x=785, y=110, width=100, height=20)
    
  def crearEntry(self):
    self.entry1 = Entry(self, bg="gray")
    self.entry1.place(x=85, y=140, width=150, height=30)
    self.entry2 = Entry(self, bg="gray")
    self.entry2.place(x=310, y=140, width=150, height=30)
    self.entry3 = Entry(self, bg="gray")
    self.entry3.place(x=535, y=140, width=150, height=30)
    self.entry4 = Entry(self, bg="gray")
    self.entry4.place(x=760, y=140, width=150, height=30)
    self.entry5 = Entry(self, bg="gray")
    self.entry5.place(x=155, y=430, width=100, height=30)

  def ingresarDatos(self):
    patron1 = r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ]{2,}$'  
    patron2 = r'^[a-zA-Z0-9_.-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]+$' 
    patron3 = r'^[\+\s-]?\d{10,15}$'
    intentos = 3
    datosValidos = False
    #Valida nombre
    for intento in range(intentos):
      self.nombre = self.entry1.get().strip()
      if re.search(patron1, self.nombre):
        #Valida apellido
        for intento in range(intentos):
          self.apellido = self.entry2.get().strip()
          if re.search(patron1, self.apellido):
            #Valida correo
            for intento in range(intentos):
              self.correo = self.entry3.get().strip()
              if re.search(patron2, self.correo):
                #Valida telefono
                for intento in range(intentos):
                  self.telefono = self.entry4.get().strip()
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

  def registrarUsuario(self):
    try:
      if self.ingresarDatos():
        if os.path.exists("archivoUsuarios.txt"):
          with open("archivoUsuarios.txt", "r") as archivo:
            lineas = archivo.readlines()
          if lineas:
            self.id = len(lineas) + 1
          else:
            self.id = 1
        else:
          self.id = 1
          with open("archivoUsuarios.txt", "a") as archivo:
            archivo.write(f"id:{self.id} {self.nombre} {self.apellido} {self.correo} {self.telefono}\n")
          self.mostrarMensaje1.config(text="El usuario se ha registrado con éxito")
          self.mostrarMensaje4.config(text="")
          self.entry1.delete(0, "end")
          self.entry2.delete(0, "end")
          self.entry3.delete(0, "end")
          self.entry4.delete(0, "end")
      else:
        self.mostrarMensaje1.config(text="Datos no válidos. Vuelve a intentarlo")
    except Exception as e:
      self.mostrarMensaje1.config(text=f"Error inesperado: {e}")

  def eliminarUsuario(self):
    try:
      if os.path.exists("archivoUsuarios.txt"):
        with open("archivoUsuarios.txt", "r") as archivo:
          lineas = archivo.readlines()
        if lineas:
          id = int(self.entry5.get().strip())
          if 0 < id <= len(lineas):
            lineas.pop(id - 1)
            #Cambia el resto de los id
            for i in range(len(lineas)):
              if i >= id-1:
                lineas[i] = lineas[i].replace(f"{i+2}", f"{i+1}", 1)
            #Actualiza el texto del Label
            usuarios = "".join(lineas)
            self.mostrarUsuarios.config(text=usuarios)  
            #Actualiza el archivo
            with open("archivoUsuarios.txt", "w") as archivo:
              archivo.writelines(lineas)
            self.mostrarMensaje2.config(text="Usuario eliminado\n correctamente")
            self.entry5.delete(0, "end")
          else:
            self.mostrarMensaje2.config(text="id no válido")
        else:
          self.mostrarMensaje2.config(text="No hay usuarios\n registrados")
      else:
        self.mostrarMensaje2.config(text="No hay usuarios\n registrados")
    except Exception as e:
      self.mostrarMensaje2.config(text=f"Error inesperado: {e}")

  def actualizarUsuario(self):
    try:
      if os.path.exists("archivoUsuarios.txt"):
        with open("archivoUsuarios.txt", "r") as archivo:
          lineas = archivo.readlines()
        if lineas:
          id = int(self.entry5.get().strip())
          if 0 < id <= len(lineas):
            datosValidos = self.ingresarDatos()
            if datosValidos:
              lineas[id - 1] = f"id:{id} {self.nombre} {self.apellido} {self.correo} {self.telefono}\n"
              #Actualiza el texto del Label
              usuarios = "".join(lineas) 
              self.mostrarUsuarios.config(text=usuarios)  
              #Actualiza el archivo
              with open("archivoUsuarios.txt", "w") as archivo:
                archivo.writelines(lineas)
              self.mostrarMensaje3.config(text="Usuario actualizado correctamente")
              self.entry1.delete(0, "end")
              self.entry2.delete(0, "end")
              self.entry3.delete(0, "end")
              self.entry4.delete(0, "end")
              self.entry5.delete(0, "end")
            else:
              self.mostrarMensaje3.config(text="Vuelve a intentarlo")
          else:
            self.mostrarMensaje3.config(text="id no válido")
        else:
          self.mostrarMensaje3.config(text="No hay usuarios registrados")
      else:
        self.mostrarMensaje3.config(text="No hay usuarios registrados")
    except Exception as e:
      self.mostrarMensaje3.config(text=f"Error inesperado: {e}")
  
  def verUsuarios(self):
    try:
      if os.path.exists("archivoUsuarios.txt"):
        with open("archivoUsuarios.txt", "r") as archivo:
          lineas = archivo.readlines()
        if lineas:
          self.mostrarMensaje1.config(text="")
          self.mostrarMensaje4.config(text="")
          usuarios = "".join(lineas)  #Combina todas las líneas en una sola cadena
          self.mostrarUsuarios.config(text=usuarios)  #Actualiza el texto del Label
        else:
          self.mostrarMensaje4.config(text="No hay usuarios registrados")
      else:
        self.mostrarMensaje4.config(text="No hay usuarios registrados")
    except Exception as e:
      self.mostrarMensaje4.config(text=f"Error inesperado: {e}")

ventana = Tk()
ventana.wm_title("Usuarios")
app = Usuarios(ventana)
app.mainloop()