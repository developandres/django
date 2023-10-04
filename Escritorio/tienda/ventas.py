from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import sys
from subprocess import call


class Ventas():
	db_name = "/home/andrev/Escritorio/tienda/base_datos_proyecto2503319.db"
	def __init__(self,ventana_ventas):
		menubar = Menu(ventana_ventas)
		self.ventana_ventas = ventana_ventas
		self.ventana_ventas.title("Ventas")
		self.ventana_ventas.geometry("1080x920")
		self.ventana_ventas.resizable(0,0)
		self.ventana_ventas.config(bd=10, menu=menubar)
		#--------------Menu de la ventana----------------------

		#--------------Opciones----------------------
		Productos = Menu(menubar, tearoff=0)
		Clientes = Menu(menubar, tearoff=0)
		Ventas = Menu(menubar, tearoff=0)
		Informacion = Menu(menubar, tearoff=0)

		#--------------Menu cascada----------------------
		menubar.add_cascade(label="Productos",menu=Productos)
		menubar.add_cascade(label="Clientes",menu=Clientes)
		menubar.add_cascade(label="Ventas",menu=Ventas)
		menubar.add_cascade(label="Informacion",menu=Informacion)
		

		#self.img_registrar =PhotoImage(file="")
		#self.img_buscar =PhotoImage(file="")
		#self.img_registrar =PhotoImage(file="")
		#--------------Menu cascada de Productos----------------------
		self.boton_registrar = Productos.add_command(label="Registrar",command=self.llamar_productos, compound=LEFT)
		#Arriba va una imagen
		#--------------Menu cascada de Clientes----------------------
		self.boton_registrar = Clientes.add_command(label="Registrar",command=self.llamar_clientes, compound=LEFT)
		#Arriba va una imagen
        #--------------Menu cascada de Ventas----------------------
		self.boton_registrar = Ventas.add_command(label="Registrar",command=self.widgets_crud, compound=LEFT)
		#Arriba va una imagen
		self.boton_buscar = Ventas.add_command(label="Buscar",command=self.widgets_buscador, compound=LEFT)
		#Arriba va una imagen
		#--------------Menu cascada de Informacion----------------------
		self.boton_informacion = Informacion.add_command(label="Informacion del sistema",command=self.widgets_informacion, compound=LEFT)
		

		#----------------------------------------WIDGETS DEL MENU-----------------------
		self.label_titulo_crud = LabelFrame(ventana_ventas)
		self.frame_logo_ventas = LabelFrame(ventana_ventas)
		self.frame_registro = LabelFrame(ventana_ventas, text= "Informacion de la venta", font=("comic sans", 10, "bold"),pady=5)
		self.frame_botones_registro = LabelFrame(ventana_ventas)
		self.frame_tabla_crud = LabelFrame(ventana_ventas )

		self.label_titulo_buscador = LabelFrame(ventana_ventas)
		self.frame_buscar_venta = LabelFrame(ventana_ventas, text= "Buscar ventas", font=("comic sans", 10, "bold"),pady=10)
		self.frame_boton_buscar = LabelFrame(ventana_ventas)

		self.label_informacion = LabelFrame(ventana_ventas)

		self.widgets_crud()
		#------------------------------------------------------------------------------


		# titulo = Label(ventana_registro, text="Registro de usuario", fg="black", font=("Arial", 10, "bold")).pack()
		# """Imagen registro"""
		# imagen_registro = Image.open('C:/Users/Aprendiz/Desktop/tienda/anadir.png')
		# nueva_imagen = imagen_registro.resize((40,40))
		# render = ImageTk.PhotoImage(nueva_imagen)
		# label_imagen = Label(ventana_registro, image=render)
		# label_imagen.image = render
		# label_imagen.pack(pady=5)
		# """Marco del registro"""
		titulo = Label(ventana_ventas, text="Registro de ventas", fg="black", font=("Arial", 10, "bold"))
		frame_registro = LabelFrame(ventana_ventas, text="Datos de la venta", font=("Arial", 10, "bold"))
		frame_registro.config(bd=2, pady=5)
		# marco.pack()

		# Nombre
		label_codigo = Label(self.frame_registro, text="Usuario" ,font=("Arial", 10, "bold")).grid(row=0,column=0,sticky='s',padx=5,pady=10)
		self.codigo= Entry(self.frame_registro, width=25)
		self.codigo.focus()
		self.codigo.grid(row=0,column=1,padx=5,pady=5)
		
		label_producto = Label(self.frame_registro, text="Producto" ,font=("Arial", 10, "bold")).grid(row=1,column=0,sticky='s',padx=5,pady=10)
		self.producto= Entry(self.frame_registro, width=25)
		self.producto.focus()
		self.producto.grid(row=1,column=1,padx=5,pady=5)

		label_proveedor= Label(self.frame_registro, text="Proveedor" ,font=("Arial", 10, "bold")).grid(row=2,column=0,sticky='s',padx=5,pady=10)
		self.proveedor= Entry(self.frame_registro, width=25)
		self.proveedor.focus()
		self.proveedor.grid(row=2,column=1,padx=5,pady=10)

		label_cantidad	= Label(self.frame_registro, text="Cantidad" ,font=("Arial", 10, "bold")).grid(row=0,column=2,sticky='s',padx=5,pady=10)
		self.cantidad= Entry(self.frame_registro, width=25)
		self.cantidad.focus()
		self.cantidad.grid(row=0,column=3,padx=5,pady=10)

		label_fecha = Label(self.frame_registro, text= "Ingrese se la fecha: ",font=("Arial", 10, "bold")).grid(row=1,column=2,sticky='s',padx=5,pady=10)
		self.fecha = Entry(self.frame_registro,width=25)
		self.fecha.focus()
		self.fecha.grid(row=1,column=3,padx=5,pady=10)

		label_combo_pago = Label(self.frame_registro, text="Tipo de pago: ",font=("Arial", 10, "bold")).grid(row=2, column=2,sticky='s',padx=5,pady=10)
		self.combo_pago = ttk.Combobox(self.frame_registro, values=["Credito", "Contado"], width=20, state="readonly")
		self.combo_pago.current(1)
		self.combo_pago.grid(row=2,column=3,padx=5,pady=10)

		"""Frame de registro"""
		
		#  frame  botones
		frame_botones_registro = Frame(ventana_ventas)
		self.frame_botones_registro.config(bd=0)
		self.frame_botones_registro.grid(row=3,column=0,padx=5,pady=5)
	


		boton_registo = Button(self.frame_botones_registro, text="Registrar",command=self.registrar_ventas, height=2, width=9, bg="green", fg="white", font=("Comic Sans MS",8,"bold")).grid(row=1, column=1, padx=10, pady=10)
		boton_editar = Button(self.frame_botones_registro, text="Editar",command=self.editar_venta, height=2, width=9, bg="blue", fg="white", font=("Comic Sans MS",8,"bold")).grid(row=1, column=2, padx=10, pady=10)
		boton_limpiar = Button(self.frame_botones_registro, text="Limpiar",command=self.limpiar_formulario, height=2, width=9, bg="yellow", fg="white", font=("Comic Sans MS",8,"bold")).grid(row=1, column=3, padx=10, pady=10)
		boton_cancelar= Button(self.frame_botones_registro, text="Cancelar",command=ventana_ventas.quit ,height=2, width=9, bg="red", fg="white", font=("Comic Sans MS",8,"bold")).grid(row=1, column=4, padx=10, pady=10)
		boton_eliminar= Button(self.frame_botones_registro, text="Eliminar",command=self.eliminar_ventas,height=2, width=9, bg="pink", fg="white", font=("Comic Sans MS",8,"bold")).grid(row=1, column=5, padx=10, pady=10)
		
		"""Registo de Ventas"""
	def registrar_ventas(self):
		if self.validar_formulario() and  self.validar_registrar():
			query = "INSERT INTO Ventas VALUES(NULL,?,?,?,?,?,?)"
			parametros = (self.codigo.get(),self.producto.get(),self.proveedor.get(),self.cantidad.get(),self.fecha.get(),self.combo_pago.get())
			self.ejecutar_consulta(query, parametros)
			messagebox.showinfo("Registro exitoso",f"Venta registrado exitosamente")
			self.limpiar_formulario()
			self.listar_ventas()


		"""validar formulario"""
	def validar_formulario(self):
		if len(self.codigo.get())!=0 and len(self.producto.get())!=0 and len(self.proveedor.get())!=0 and len(self.cantidad.get())!=0 and len(self.fecha.get())!=0 and len(self.combo_pago.get())!=0:
			return True
		else:
			messagebox.showerror("Error en el registro. ",f"Diligencie todos los campos del Formulario")
	"""Ejecutar consulta"""


	def ejecutar_consulta(self,query,parametros =()):
		with sqlite3.connect(self.db_name) as conexion:
			cursor = conexion.cursor()
			result = cursor.execute(query, parametros)
			conexion.commit()
			return result
	"""Limpiar formularios"""


	def limpiar_formulario(self):
		self.codigo.delete(0,END)
		self.producto.delete(0,END)
		self.proveedor.delete(0,END)
		self.cantidad.delete(0,END)
		self.fecha.delete(0,END)
		self.combo_pago.delete(0,END)
		
	"""Listar Ventas"""
	def listar_ventas(self):
		records = self.tree.get_children()
		for venta in records:
			self.tree.delete(venta)
		query = 'SELECT * FROM	Ventas ORDER BY  proveedor  DESC'
		db_rows = self.ejecutar_consulta(query)
		for	row in db_rows:
			self.tree.insert("",0, text=row[1], values=(row[2],row[3],row[4],row[5], row[6]))

	"""Editar ventas"""
	def editar_venta(self):
		try:
			self.tree.item(self.tree.selection())['values'][0]
		except IndexError as e:
			messagebox.showerror("ERROR",f"Debe seleccionar una venta de la tabla")

		codigo = self.tree.item(self.tree.selection())['text']
		producto = self.tree.item(self.tree.selection())['values'][0]
		proveedor = self.tree.item(self.tree.selection())['values'][1]
		cantidad = self.tree.item(self.tree.selection())['values'][2]
		fecha = self.tree.item(self.tree.selection())['values'][3]
		combo_pago = self.tree.item(self.tree.selection())['values'][4]

		self.ventana_editar = Toplevel()
		self.ventana_editar.title("EDITAR VENTA")
		self.ventana_editar.resizable(0,0)


		label_codigo = Label(self.ventana_editar, text="Código de la venta:", font=("Comic Sans", 10, "bold")).grid(row=0, column=0, sticky='s', padx=5, pady=8)
		nuevo_codigo = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=codigo), width=25)
		nuevo_codigo.grid(row=0, column=1, padx=5, pady=8)


		label_producto = Label(self.ventana_editar, text="Producto de la venta:", font=("Comic Sans", 10, "bold")).grid(row=1, column=0, sticky='s', padx=5, pady=8)
		nuevo_producto = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=producto), width=25)
		nuevo_producto.grid(row=1, column=1, padx=5, pady=0)

		label_proveedor = Label(self.ventana_editar, text="Proveedor:", font=("Comic Sans", 10, "bold")).grid(row=1, column=2, sticky='s', padx=5, pady=8)
		nueva_proveedor = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=proveedor), width=25)
		nueva_proveedor.grid(row=1, column=3, padx=5, pady=0)

		label_cantidad = Label(self.ventana_editar, text="cantidad:", font=("Comic Sans", 10, "bold")).grid(row=2, column=0, sticky='s', padx=5, pady=8)
		nueva_cantidad = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=cantidad), width=25)
		nueva_cantidad.grid(row=2, column=1, padx=5, pady=0)
		
		label_fecha = Label(self.ventana_editar, text="fecha:", font=("Comic Sans", 10, "bold")).grid(row=0, column=2, sticky='s', padx=5, pady=8)
		nuevo_fecha = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=fecha), width=25)
		nuevo_fecha.grid(row=0, column=3, padx=5, pady=0)

		label_combo_pago = Label(self.ventana_editar, text="Tipo de pago:", font=("Comic Sans", 10, "bold")).grid(row=2, column=2, sticky='s', padx=5, pady=8)
		nuevo_combo_pago = ttk.Combobox(self.ventana_editar, values=["Credito", "Contado"], width=22, state="readonly")
		nuevo_combo_pago.set(combo_pago)
		nuevo_combo_pago.grid(row=2, column=3, padx=5, pady=0)

		boton_actualizar = Button(self.ventana_editar, text="ACTUALIZAR", command=lambda:self.actualizar(nuevo_codigo.get(), nuevo_producto.get(), nueva_proveedor.get(), nueva_cantidad.get(), nuevo_fecha.get(), nuevo_combo_pago.get(), codigo), height=2, width=20, bg="blue", fg="white", font=("Comic Sans MS", 9, "bold"))
		boton_actualizar.grid(row=3, column=1, columnspan=2, padx=10, pady=15)

		self.ventana_editar.mainloop()

	#---------------------------------------------------- Actulizar venta-----------------------------------------------------------------------------------------

	def actualizar(self, nuevo_codigo, nuevo_producto, nueva_proveedor, nueva_cantidad, nuevo_combo_pago, nuevo_fecha, codigo):
		query = 'UPDATE Ventas SET codigo = ?, producto = ?, proveedor = ?, cantidad = ?, tipo_pago = ?, fecha = ? WHERE codigo = ?'
		parameters = (nuevo_codigo, nuevo_producto, nueva_proveedor, nueva_cantidad, nuevo_fecha, nuevo_combo_pago, codigo)
		self.ejecutar_consulta(query, parameters)
		messagebox.showinfo('EXITO',f'Venta Actualizado:{nuevo_producto}')
		self.ventana_editar.destroy()
		self.listar_ventas()


	def eliminar_ventas(self):
		try:
			self.tree.item(self.tree.selection())['values'][0]
		except IndexError as e:
			messagebox.showerror('Error',f'Debe seleccionar una venta de la tabla')
		dato = self.tree.item(self.tree.selection())['text']
		nombre = self.tree.item(self.tree.selection())['values'][0]
		query = "DELETE FROM Ventas WHERE codigo = ?"
		respuesta = messagebox.askquestion("ADVERTENCIA",f"¿Està seguro que desea eliminar la venta: {nombre}?")
		if respuesta == "yes":
			self.ejecutar_consulta(query,(dato,))
			self.listar_ventas()
			messagebox.showinfo('Exito',f'Venta eliminado: {nombre}')
		else:
			messagebox.showerror('ERROR',F'error al eliminar la venta: {nombre}')
		
	#----------------------------------------------- Widgets Crud ------------------------------------------------------------------------------------
	def widgets_crud(self):
		#------------------------------------- Configuracion de la ventana --------------------------------------------------------------------------		
		self.label_titulo_crud.config(bd=10)
		self.label_titulo_crud.grid(row=0, column=0, padx=5, pady=5)
		#-------------------------------------------------- Titulo --------------------------------------------------------------------------		
		self.titulo_crud = Label(self.label_titulo_crud, text="LISTA DE VENTAS",fg="aquamarine",bg="black",font=("Comic Sans", 17, "bold"),pady=10)
		self.titulo_crud.grid(row=0, column=0, padx=5, pady=5)
		#---------------------------------------------------Frame logo --------------------------------------------------------------------------		
		self.frame_logo_ventas.config(bd=2)
		self.frame_logo_ventas.grid(row=2, column=0, padx=5, pady=5)
		#------------------ Marco de la ventana ----------------------
		self.frame_registro.config(bd=2)
		self.frame_registro.grid(row=2, column=0, padx=5, pady=5)
		#------------------ Tabla de ventas ----------------------

		self.frame_tabla_crud.config(bd=2)
		self.frame_tabla_crud.grid(row=4,column=0,padx=5,pady=5)
		self.tree = ttk.Treeview(self.frame_tabla_crud,height=13, columns=("columna1", "columna2", "columna3", "columna4", "columna5"))

		self.tree.heading("#0", text="Codigo ", anchor=CENTER)
		self.tree.column("#0", width=90 ,minwidth=50, stretch=False)

		self.tree.heading("columna1", text="Codigo ", anchor=CENTER)
		self.tree.column("columna1", width=150 ,minwidth=50, stretch=False)

		self.tree.heading("columna1", text="productos ", anchor=CENTER)
		self.tree.column("columna1", width=150 ,minwidth=75, stretch=False)

		self.tree.heading("columna2", text="proveedor ", anchor=CENTER)
		self.tree.column("columna2", width=150 ,minwidth=75, stretch=False)

		self.tree.heading("columna3", text="cantidad ", anchor=CENTER)
		self.tree.column("columna3", width=150 ,minwidth=75, stretch=False)

		self.tree.heading("columna4", text="fecha: ", anchor=CENTER)
		self.tree.column("columna4", width=150 ,minwidth=75, stretch=False)

		self.tree.heading("columna5", text="tipo_pago: ", anchor=CENTER)
		self.tree.column("columna5", width=150 ,minwidth=75, stretch=False)

		self.tree.grid(row=0,column=0,sticky=E)
		self.listar_ventas()
		
		self.widgets_buscador_remove()
		self.label_informacion.grid_remove()

		#----------------------------------------------- Widgets buscador ------------------------------------------------------------------------------------
	def widgets_buscador(self):
		self.label_titulo_buscador.config(bd=0)
		self.label_titulo_buscador.grid(row=0, column=0, padx=5, pady=5)

		self.titulo_buscador = Label(self.label_titulo_buscador, text="BUSCADOR DE VENTAS",fg="black",font=("Comic Sans", 17, "bold"))
		self.titulo_buscador.grid(row=0, column=0)

		self.frame_buscar_venta.config(bd=2)
		self.frame_buscar_venta.grid(row=2, column=0, padx=5, pady=5)

		self.label_buscar = Label(self.frame_buscar_venta, text="Buscar por: ",font=("Arial", 10, "bold")).grid(row=0, column=0,sticky='s',padx=5,pady=5)
		self.combo_buscar= ttk.Combobox(self.frame_buscar_venta, values=["Codigo","provedor"], width=22, state="readonly")
		self.combo_buscar.current()
		self.combo_buscar.grid(row=0,column=1,padx=5,pady=5)

		self.label_proveedor = Label(self.frame_buscar_venta, text= "Codigo / Nombre del proveedor	 : ",font=("comic sans", 10, "bold")).grid(row=0,column=2,sticky='s',padx=5,pady=5)
		self.codigo_proveedor = Entry(self.frame_buscar_venta,width=25)
		self.codigo_proveedor.focus()
		self.codigo_proveedor.grid(row=0,column=3,padx=5,pady=5)

		self.frame_boton_buscar.config(bd=0)
		self.frame_boton_buscar.grid(row=3, column=0, padx=5, pady=5)

		self.boton_buscar = Button(self.frame_boton_buscar, text="BUSCAR", command=self.buscar_ventas, height=2, width=20, bg="black", fg="white",font=("comic sans", 10, "bold"))
		self.boton_buscar.grid(row=0,column=0,padx=5,pady=5)

		self.tree.delete(*self.tree.get_children())

		self.widgets_crud_remove()
		self.label_informacion.grid_remove()


	def widgets_crud_remove(self):
		self.label_titulo_crud.grid_remove()
		self.frame_registro.grid_remove()
		self.frame_botones_registro.grid_remove()
	

	def widgets_buscador_remove(self):
		self.label_titulo_buscador.grid_remove()
		self.frame_buscar_venta.grid_remove()
		self.frame_boton_buscar.grid_remove()
	
	def widgets_informacion(self):
		self.frame_logo_ventas.grid_forget()
		self.frame_tabla_crud.grid_forget()
		self.label_informacion.config(bd=0)
		self.label_informacion.grid(row=0, column=0)
		#self.imagen_soporte.config(row=0,column=0)

		self.label_titulo = Label(self.label_informacion, text= "APLICACION DE ESCRITORIO", fg="aquamarine", bg="black",font=("comic sans", 25, "bold"),padx=137, pady=20)
		self.label_titulo.grid(row=0, column=0)

		#imagen_soporte = Image()
		#nueva_imagen = imagen_soporte.resize((170,170))
		#render = ImageTK.PhotoImage(nueva_imagen)
		#label_imagen = Label(self.imagen_soporte, image=render)
		#label_imagen.image = render
		#label_imagen.grid(row=1,column=0,padx=10,pady=15)

		self.label_titulo = Label(self.label_informacion, text="> Codigo de tienda de Tecnologìa", fg="black", font=("comic sans", 18, "bold"))
		self.label_titulo.grid(row=2,column=0,sticky="W",padx=30,pady=10)

		self.label_titulo = Label(self.label_informacion, text="> En esta tienda encuentra productos de Tecnologìa", fg="black", font=("comic sans", 18, "bold"))
		self.label_titulo.grid(row=3,column=0,sticky="W",padx=30,pady=10)

		self.label_titulo = Label(self.label_informacion, text="> Instructora: Yuli Sàenz", fg="black", font=("comic sans", 18, "bold"))
		self.label_titulo.grid(row=4,column=0,sticky="W",padx=30,pady=10)


		self.label_titulo = Label(self.label_informacion, text="> Creado por Yuli Sàenz - Ficha 25003319 Tgo.ADSO. - 2023 ", fg="black", font=("comic sans", 10, "bold"))
		self.label_titulo.grid(row=7,column=0,pady=60)

		self.widgets_buscador_remove()
		self.widgets_crud_remove()

		
	def buscar_ventas(self):
		if(self.validar_busqueda()):
			records = self.tree.get_children()
			for element in records:
				self.tree.delete(element)

			if (self.combo_buscar.get() == "codigo"):
				query= ("SELECT * FROM Ventas WHERE codigo LIKE ?")
				parametros = (self.codigo_proveedor.get()+"%")
				db_rows = self.ejecutar_consulta(query,(parametros, ))
				for row in db_rows :
					self.tree.insert("",0,text=row[1],values=(row[2],row[3],row[4],row[5],row[6]))
				
				if(list(self.tree_get_children()) ==[]):
					messagebox.showerror("Error",f"Cliente no encontrado")
			else: 
				query = ("SELECT * FROM Ventas WHERE proveedor LIKE ?")
				parametros = ("%"+self.codigo_proveedor.get()+"%")
				db_rows = self.ejecutar_consulta(query,(parametros, ))
				for row in db_rows :
					self.tree.insert("",0,text=row[1],values=(row[2],row[3],row[4],row[5],row[6]))
				if(list(self.tree.get_children()) ==[]):
					messagebox.showerror("Error",f"Cliente no encontrado") 
	
	def validar_busqueda(self):
		if len(self.codigo_proveedor.get()) !=0:
			return True
		else:
			self.tree.delete(*self.tree.get_children())
			messagebox.showerror("ERROR",f"Complete todos los campos")
	
	def validar_registrar(self):
		parametros = self.codigo.get()
		query = "SELECT * FROM Ventas WHERE codigo = ?"
		dato = self.ejecutar_consulta(query, (parametros, ))
		if (dato.fetchall() == []):
			return True
		else:
			messagebox.showerror("ERROR EN EL REGISTRO",f"Codigo no registrado anteriormente")
	
	def llamar_productos(self):
		ventana_ventas.destroy()
		call([sys.executable, '/home/andrev/Escritorio/tienda/producto.py'])
	
	def llamar_clientes(self):
		ventana_ventas.destroy()
		call([sys.executable, '/home/andrev/Escritorio/tienda/clientes.py'])





if __name__ == '__main__':
	ventana_ventas = Tk()
	application = Ventas(ventana_ventas)
	ventana_ventas.mainloop()
