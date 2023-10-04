# Importamos la libreria
from tkinter import * 
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3
import sys
from subprocess import call


class Login:
	db_name = '/home/andrev/Escritorio/tienda/base_datos_proyecto2503319.db'
	def __init__(self, ventana_loguin):
		# Atributos de la ventana
		self.window = ventana_loguin
		# Titulo
		self.window.title("Ingreso al sistema")
		# Tamaño
		self.window.geometry("380x420")
		# Icono
		self.window.iconbitmap("")
		# Permisos de acondicionar el tamaño
		self.window.resizable(0,0)
		# Color de la ventana
		self.window.config(bd=10)


		# titulo de la ventana
		# titulo = Label(ventana_loguin, text="Ingreso al sistema", fg= 'black', font=("Arial", 10, "bold"),pady=10).pack()
		# # Logo del loguin
		# imagen_loguin = Image.open("C:/Users/Aprendiz/Desktop/tienda/entrada.png")
		# # Tamaño 
		# nueva_imagen = imagen_loguin.resize((40,40))
		# # Renderizar
		# render = ImageTk.PhotoImage(nueva_imagen)
		# # Label para cargar la imagen
		# label_imagen = Label(ventana_loguin, image=render)
		# # Renderizar el label
		# label_imagen.image = render
		# # Ubicamos el label
		# label_imagen.pack(pady=5)
		# # Marco del loguin
		marco = LabelFrame(ventana_loguin, text="Ingrese sus datos ",  font=("Arial", 10, "bold"),pady=18)
		marco.pack()
		# Formulario_loguin
		label_usuario = Label(marco, text= "Usuario: ",font=("Arial", 10, "bold")).grid(row=0,column=0,sticky='s',padx=5,pady=10)
		self.usuario = Entry(marco,width=25)
		self.usuario.focus()
		self.usuario.grid(row=0,column=1,padx=5,pady=10)
		"""Label contraseña"""
		label_password = Label(marco, text="Password", font=("Arial", 10, "bold")).grid(row=1,column=0,sticky='s',pady=5)
		self.password = Entry(marco,width=25,  show="*")
		self.password.grid(row=1,column=1,padx=5,pady=10)
		"""Frame de los bototenes loguin"""
		frame_botones = Frame(ventana_loguin)
		frame_botones.pack()
		"""Botones de loguin"""
		boton_ingreso = Button(frame_botones, text="Ingresar",command=self.login, height=2,width=12, bg="green", fg="white", font=("Arial", 10, "bold")).grid(row=0,column=1,sticky='s',padx=10,pady=15)
		boton_registro = Button(frame_botones, text="Registrar",command=self.llamar_registro, height=2,width=12, bg="blue", fg="white", font=("Arial", 10, "bold")).grid(row=0,column=2,sticky='s',padx=10,pady=15)

		label_olvido = Label(frame_botones, text="Olvido su contraseña", font=("Arial", 10, "bold")).grid(row=1,column=1,columnspan=2,sticky='s')
		boton_ingreso = Button(frame_botones, text="Recuperar contraseña",command=self.llamar_recuperacion,height=2,width=24, bg="pink", fg="white", font=("Arial", 10, "bold")).grid(row=2,column=1,columnspan=2,sticky='s',padx=10,pady=15)

	def llamar_registro(self):
		ventana_loguin.destroy()
		call([sys.executable, '/home/andrev/Escritorio/tienda/registro.py'])


	def llamar_recuperacion(self):
		ventana_loguin.destroy()
		call([sys.executable, '/home/andrev/Escritorio/tienda/recuperar.py'])

	def login(self):
		if (self.validar_formulario_completo()):
			usuario = self.usuario.get()
			password = self.password.get()
			dato = self.validar_login(usuario,password)
			if (dato != []):
				messagebox.showinfo("BIENVENIDO","Datos ingresados Correctamente")
				ventana_loguin.destroy()
				call([sys.executable, '/home/andrev/Escritorio/tienda/producto.py'])
			else:
				messagebox.showerror("Error de ingreso","Usuario o Password incorrectos")
	
	
	def validar_formulario_completo(self):
		if len(self.usuario.get()) !=0 and len(self.password.get()) != 0:
			return True
		else:
			messagebox.showerror('Error de ingreso','Ingrese los datos correctamente')

	def validar_login(self,usuario,password):
		with sqlite3.connect(self.db_name) as conexion:
			cursor = conexion.cursor()
			sql = f'SELECT * FROM usuarios WHERE usuario={usuario} AND password={password}'
			cursor.execute(sql)
			validacion = cursor.fetchall()
			cursor.close()
			return validacion

	
if __name__ == '__main__':
	ventana_loguin = Tk()
	application = Login(ventana_loguin)
	ventana_loguin.mainloop()


