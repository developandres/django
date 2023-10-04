from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import sys
from subprocess import call

class Registro:

	db_name = '/home/andrev/Escritorio/tienda/base_datos_proyecto2503319.db'
	def __init__(self,ventana_registro):
		#Titulo de la ventana
		self.window = ventana_registro
		self.window.title("Formulario de registro: ")
		self.window.geometry("520x830")
		#self.window.iconbitmap("C:/Users/Aprendiz/Deskto	p/tienda/form_icon_142679.ico")
		self.window.resizable(0,0)
		self.window.config(bd=10)
		"""Titulo de la ventana"""
		titulo = Label(ventana_registro, text="Registro de usuario", fg="black", font=("Arial", 10, "bold")).pack()
		# """Imagen registro"""
		# imagen_registro = Image.open('C:/Users/Aprendiz/Desktop/tienda/anadir.png')
		# nueva_imagen = imagen_registro.resize((40,40))
		# render = ImageTk.PhotoImage(nueva_imagen)
		# label_imagen = Label(ventana_registro, image=render)
		# label_imagen.image = render
		# label_imagen.pack(pady=5)
		"""Marco del registro"""
		marco = LabelFrame(ventana_registro, text="Datos personales", font=("Arial", 10, "bold"))
		marco.config(bd=2, pady=5)
		marco.pack()
		""""Fomrulario de regstro """
		label_usuario = Label(marco, text="Usuario" ,font=("Arial", 10, "bold")).grid(row=0,column=0,sticky='s',padx=5,pady=0)
		self.usuario= Entry(marco, width=25)
		self.usuario.focus()
		self.usuario.grid(row=0,column=1,padx=5,pady=5)

		#label nombre
		label_nombre = Label(marco, text="Nombres: " ,font=("Arial", 10, "bold")).grid(row=1,column=0,sticky='s',padx=5,pady=0)
		self.nombre= Entry(marco, width=25)
		self.nombre.grid(row=1,column=1,padx=5,pady=5)

		#label apellidos
		label_apellido = Label(marco, text="Apellidos: " ,font=("Arial", 10, "bold")).grid(row=2,column=0,sticky='s',padx=5,pady=0)
		self.apellido= Entry(marco, width=25)
		self.apellido.grid(row=2,column=1,padx=5,pady=5)
		#label Sexo
		label_genero = Label(marco, text="Sexo: ",font=("Arial", 10, "bold")).grid(row=3, column=0,sticky='s',padx=5,pady=0)
		self.combo_genero = ttk.Combobox(marco, values=["Masculino", "Femenino"], width=22, state="readonly")
		self.combo_genero.current(0)
		self.combo_genero.grid(row=3,column=1,padx=5,pady=5)

		#label correo
		label_correo = Label(marco, text="Correo: " ,font=("Arial", 10, "bold")).grid(row=4,column=0,sticky='s',padx=5,pady=0)
		self.correo= Entry(marco, width=25)
		self.correo.grid(row=4,column=1,padx=5,pady=5)
		#label edad
		label_edad = Label(marco, text="Edad: " ,font=("Arial", 10, "bold")).grid(row=5,column=0,sticky='s',padx=5,pady=0)
		self.edad= Entry(marco, width=25)
		self.edad.grid(row=5,column=1,padx=5,pady=5)
		#label password
		label_password = Label(marco, text="Password: " ,font=("Arial", 10, "bold")).grid(row=6,column=0,sticky='s',padx=5,pady=0)
		self.password= Entry(marco, width=25, show="*")
		self.password.grid(row=6,column=1,padx=5,pady=5)
		#label validate_password
		label_validate_password = Label(marco, text="Validate Password: " ,font=("Arial", 10, "bold")).grid(row=7,column=0,sticky='s',padx=5,pady=0)
		self.validate_password= Entry(marco, width=25, show="*")
		self.validate_password.grid(row=7,column=1,padx=5,pady=5)

		# Marco preguntas de recurso
		marco_pregunta = LabelFrame(ventana_registro, text="Preguntas de seguridad",font=("Arial", 10, "bold"),pady=10)
		marco_pregunta.config(bd=2, pady=5)
		marco_pregunta.pack()

		#Preguntas del registro
		label_pregunta = Label(marco_pregunta, text="Pregunta",font=("Arial", 10, "bold")).grid(row=0,column=0,sticky='s',padx=10,pady=8)
		self.combo_pregunta = ttk.Combobox(marco_pregunta, values=["Nombre de su primera mascota", "Nombre de su deporte favorito"],width="30", state="readonly")
		self.combo_pregunta.current(0)
		self.combo_pregunta.grid(row=0,column=1,padx=10,pady=8)

		label_respuesta = Label(marco_pregunta, text="Respuesta: " ,font=("Arial", 10, "bold")).grid(row=1,column=0,sticky='s',padx=5,pady=0)
		self.respuesta= Entry(marco_pregunta, width=25)
		self.respuesta.grid(row=1,column=1,padx=5,pady=5)

		label_nota = Label(marco_pregunta, text="Respuesta para recuperar contraseña").grid(row=2,column=0,sticky='s')

		"""Frame de registro"""
		frame_botones = Frame(ventana_registro)
		frame_botones.pack()


		boton_registo = Button(frame_botones, text="Registrar",command=self.registrar_usuario, height=2, width=9, bg="green", fg="white", font=("Comic Sans MS",8,"bold")).grid(row=1, column=1, padx=10, pady=10)
		boton_login = Button(frame_botones, text="loguin",command=self.llamar_login, height=2, width=9, bg="blue", fg="white", font=("Comic Sans MS",8,"bold")).grid(row=1, column=2, padx=10, pady=10)
		boton_limpiar = Button(frame_botones, text="Limpiar",command=self.limpiar_formulario, height=2, width=9, bg="yellow", fg="white", font=("Comic Sans MS",8,"bold")).grid(row=1, column=3, padx=10, pady=10)
		boton_cancelar= Button(frame_botones, text="Cancelar",command=ventana_registro.quit, height=2, width=9, bg="red", fg="white", font=("Comic Sans MS",8,"bold")).grid(row=1, column=4, padx=10, pady=10)

	def registrar_usuario(self):
		if self.validar_formulario() and self.validar_password() and self.validar_usuario():
			query = 'INSERT INTO  usuarios VALUES(NULL, ? , ?, ?, ?, ?, ?, ?, ?)'
			parametros= (self.usuario.get(),self.nombre.get(),self.apellido.get(),self.combo_genero.get(),self.correo.get(),self.edad.get(),self.password.get(),self.respuesta.get())
			self.ejecutar_consulta(query, parametros)
			messagebox.showinfo('REGISTRO EXITOSO'f'Bienvenid@ {self.nombre.get()} {self.apellido.get()}')
			self.limpiar_formulario()

	def validar_formulario(self):
		if len(self.usuario.get())!=0 and len(self.nombre.get())!=0 and len(self.apellido.get())!=0 and len(self.combo_genero.get())!=0 and len(self.correo.get())!=0 and len(self.edad.get())!=0 and len(self.password.get())!=0 and len(self.respuesta.get())!=0:
			return True
		else:
			messagebox.showerror("Error en el registro. ","Diligencie todos los campos del Formulario")
	
	def validar_password(self):
		if (str(self.password.get()) == str(self.validate_password.get())):
			return True
		else:
			messagebox.showerror("Error en el registro. ","Password incorrecto")

	
	
	def	validar_usuario(self):
		usuario = self.usuario.get()
		dato = self.buscar_usuario(usuario)
		if (dato == []):
			return True
		else:
			messagebox.showerror("Error en el registro. ", "El usuario ya existe")

	def buscar_usuario(self, usuario):
		with sqlite3.connect(self.db_name) as conexion:
			cursor = conexion.cursor()
			sql = "SELECT * FROM Usuarios WHERE usuario = {}".format(usuario)
			cursor.execute(sql)
			usuario_consulta = cursor.fetchall()
			cursor.close()
			return usuario_consulta
		

	def ejecutar_consulta(self, query, parametros=()):
		with sqlite3.connect(self.db_name) as conexion:
			cursor = conexion.cursor()
			result = cursor.execute(query,parametros)
			conexion.commit()
			return result
		
	def limpiar_formulario(self):
		self.usuario.delete(0,END)
		self.nombre.delete(0,END)
		self.apellido.delete(0,END)
		self.combo_genero.delete(0,END)
		self.correo.delete(0,END)
		self.edad.delete(0,END)
		self.password.delete(0,END)
		self.validate_password.delete(0,END)
		self.combo_pregunta.delete(0,END)
		self.respuesta.delete(0,END)
		 	
	def llamar_login(self):
		ventana_registro.destroy()
		call([sys.executable,'/home/andrev/Escritorio/tienda/loguin.py'])


if __name__ == '__main__':
	ventana_registro = Tk()
	application = 	Registro(ventana_registro)
	ventana_registro.mainloop()
	
	