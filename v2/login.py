from tkinter import *
from tkinter import ttk
from conexion import BaseDatos
import hashlib

# Crear la ventana de inicio de sesión
def login_window():
    login = Tk()
    login.title("Inicio de Sesión")
    login.geometry("300x200")

    # Variables de entrada
    username = StringVar()
    password = StringVar()

    # Etiquetas y campos de entrada
    Label(login, text="Nombre de Usuario:").grid(row=0, column=0, padx=10, pady=10)
    Entry(login, textvariable=username).grid(row=0, column=1, padx=10, pady=10)

    Label(login, text="Contraseña:").grid(row=1, column=0, padx=10, pady=10)
    Entry(login, textvariable=password, show="*").grid(row=1, column=1, padx=10, pady=10)

    # Función de inicio de sesión
    def login_user():
        db = BaseDatos()
        username_input = username.get()
        password_input = hashlib.sha256(password.get().encode()).hexdigest()

        sql = "SELECT * FROM usuarios WHERE nombreusuario = %s AND contrasena = %s"
        db.cursor.execute(sql, (username_input, password_input))
        result = db.cursor.fetchone()

        if result:
            login.destroy()
            main_window()
        else:
            Label(login, text="Credenciales inválidas", fg="red").grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    # Botón de inicio de sesión
    Button(login, text="Iniciar Sesión", command=login_user).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    login.mainloop()

# Abrir la ventana principal de la aplicación
def main_window():
    # Código de la ventana principal de la aplicación
    db = BaseDatos()
    win = Tk()
    win.title("Listado de Trabajadores")
    win.geometry("1200x700")

        # creamos marco para el formulario
    marco = LabelFrame(win, text="Gestión de Trabajadores")
    marco.place(x=50, y=50, width=1100, height=500)

    # variables de texto para las cajas de diálogo
    rut = StringVar()
    nombres = StringVar()
    apellidos = StringVar()
    sexo = StringVar()
    cargoid = IntVar()
    direccion = StringVar()
    telefono = StringVar()
    fechaingreso = StringVar()
    contactoemergenciarut = StringVar()
    usuarioid = IntVar()

    # labels y cajas de diálogo
    lblRut = Label(marco, text="RUT")
    lblRut.grid(row=0, column=0)
    txtRut = Entry(marco, textvariable=rut)
    txtRut.grid(row=0, column=1)

    lblNom = Label(marco, text="Nombres")
    lblNom.grid(row=0, column=2)
    txtNom = Entry(marco, textvariable=nombres)
    txtNom.grid(row=0, column=3)

    lblApe = Label(marco, text="Apellidos")
    lblApe.grid(row=1, column=0, padx=5, pady=5)
    txtApe = Entry(marco, textvariable=apellidos)
    txtApe.grid(row=1, column=1)

    lblSex = Label(marco, text="Sexo")
    lblSex.grid(row=1, column=2, padx=5, pady=5)
    txtSex = Entry(marco, textvariable=sexo)
    txtSex.grid(row=1, column=3)

    lblCar = Label(marco, text="Cargo ID")
    lblCar.grid(row=2, column=0, padx=5, pady=5)
    txtCar = Entry(marco, textvariable=cargoid)
    txtCar.grid(row=2, column=1)

    lblDir = Label(marco, text="Dirección")
    lblDir.grid(row=2, column=2, padx=5, pady=5)
    txtDir = Entry(marco, textvariable=direccion)
    txtDir.grid(row=2, column=3)

    lblTel = Label(marco, text="Teléfono")
    lblTel.grid(row=3, column=0, padx=5, pady=5)
    txtTel = Entry(marco, textvariable=telefono)
    txtTel.grid(row=3, column=1)

    lblFec = Label(marco, text="Fecha Ingreso")
    lblFec.grid(row=3, column=2, padx=5, pady=5)
    txtFec = Entry(marco, textvariable=fechaingreso)
    txtFec.grid(row=3, column=3)

    lblCon = Label(marco, text="Contacto Emergencia RUT")
    lblCon.grid(row=4, column=0, padx=5, pady=5)
    txtCon = Entry(marco, textvariable=contactoemergenciarut)
    txtCon.grid(row=4, column=1)

    lblUsu = Label(marco, text="Usuario ID")
    lblUsu.grid(row=4, column=2, padx=5, pady=5)
    txtUsu = Entry(marco, textvariable=usuarioid)
    txtUsu.grid(row=4, column=3)

    # mensaje de salida
    lblMensaje = Label(marco, text="Gestión de Trabajadores", fg="black")
    lblMensaje.grid(row=5, column=0, columnspan=4)

    # creamos la tabla que contendrá los datos = grilla => TreeView
    tvTrabajadores = ttk.Treeview(marco)
    tvTrabajadores.grid(row=6, column=0, columnspan=4)
    # creamos columnas lógicas
    tvTrabajadores["columns"] = ("Rut", "Nombres", "Apellidos", "Sexo", "Cargo ID", "Dirección", "Teléfono", "Fecha Ingreso", "Contacto Emergencia RUT", "Usuario ID")
    # fijamos el ancho de las columnas lógicas
    tvTrabajadores.column("#0", width=0, stretch=0)
    tvTrabajadores.column("Rut", width=100, anchor=CENTER)
    tvTrabajadores.column("Nombres", width=100, anchor=CENTER)
    tvTrabajadores.column("Apellidos", width=100, anchor=CENTER)
    tvTrabajadores.column("Sexo", width=50, anchor=CENTER)
    tvTrabajadores.column("Cargo ID", width=100, anchor=CENTER)
    tvTrabajadores.column("Dirección", width=150, anchor=CENTER)
    tvTrabajadores.column("Teléfono", width=100, anchor=CENTER)
    tvTrabajadores.column("Fecha Ingreso", width=100, anchor=CENTER)
    tvTrabajadores.column("Contacto Emergencia RUT", width=150, anchor=CENTER)
    tvTrabajadores.column("Usuario ID", width=100, anchor=CENTER)
    # creamos los títulos de las columnas
    tvTrabajadores.heading("#0", text="")
    tvTrabajadores.heading("Rut", text="RUT", anchor=CENTER)
    tvTrabajadores.heading("Nombres", text="NOMBRES", anchor=CENTER)
    tvTrabajadores.heading("Apellidos", text="APELLIDOS", anchor=CENTER)
    tvTrabajadores.heading("Sexo", text="SEXO", anchor=CENTER)
    tvTrabajadores.heading("Cargo ID", text="CARGO ID", anchor=CENTER)
    tvTrabajadores.heading("Dirección", text="DIRECCIÓN", anchor=CENTER)
    tvTrabajadores.heading("Teléfono", text="TELÉFONO", anchor=CENTER)
    tvTrabajadores.heading("Fecha Ingreso", text="FECHA INGRESO", anchor=CENTER)
    tvTrabajadores.heading("Contacto Emergencia RUT", text="CONTACTO EMERGENCIA RUT", anchor=CENTER)
    tvTrabajadores.heading("Usuario ID", text="USUARIO ID", anchor=CENTER)

    # funciones
    def validar():
        r = len(rut.get())
        n = len(nombres.get())
        a = len(apellidos.get())
        s = len(sexo.get())
        c = len(str(cargoid.get())) 
        d = len(direccion.get())
        t = len(telefono.get())
        f = len(fechaingreso.get())
        ce = len(contactoemergenciarut.get())
        u = len(str(usuarioid.get()))
        return r * n * a * s * c * d * t * f * ce * u

    def limpiarForm():
        rut.set("")
        nombres.set("")
        apellidos.set("")
        sexo.set("")
        cargoid.set(0)
        direccion.set("")
        telefono.set("")
        fechaingreso.set("")
        contactoemergenciarut.set("")
        usuarioid.set(0)

    def eliminar():
        try:
            item = tvTrabajadores.selection()[0]
            rut_seleccionado = tvTrabajadores.item(item)["values"][0]
        except IndexError:
            lblMensaje.config(text="No hay registro seleccionado", fg="red")
        else:
            sql = "DELETE FROM trabajadores WHERE rut = %s"
            db.cursor.execute(sql, (rut_seleccionado,))
            db.conn.commit()
            tvTrabajadores.delete(item)
            lblMensaje.config(text="Se ha eliminado correctamente", fg="green")

    def nuevo():
        if validar():
            valores = (
                rut.get(),
                nombres.get(),
                apellidos.get(),
                sexo.get(),
                cargoid.get(),
                direccion.get(),
                telefono.get(),
                fechaingreso.get(),
                contactoemergenciarut.get(),
                usuarioid.get()
            )
            sql = "INSERT INTO trabajadores (rut, nombres, apellidos, sexo, cargoid, direccion, telefono, fechaingreso, contactoemergenciarut, usuarioid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            db.cursor.execute(sql, valores)
            db.conn.commit()
            limpiarForm()
            cargarDatos()
            lblMensaje.config(text="Trabajador insertado", fg="green")
        else:
            lblMensaje.config(text="No debe haber registros vacíos", fg="red")

    def modificar():
        if validar():
            item = tvTrabajadores.selection()[0]
            rut_seleccionado = tvTrabajadores.item(item)["values"][0]
            valores = (
                nombres.get(),
                apellidos.get(),
                sexo.get(),
                cargoid.get(),
                direccion.get(),
                telefono.get(),
                fechaingreso.get(),
                contactoemergenciarut.get(),
                usuarioid.get(),
                rut_seleccionado
            )
            sql = "UPDATE trabajadores SET nombres=%s, apellidos=%s, sexo=%s, cargoid=%s, direccion=%s, telefono=%s, fechaingreso=%s, contactoemergenciarut=%s, usuarioid=%s WHERE rut=%s"
            db.cursor.execute(sql, valores)
            db.conn.commit()
            tvTrabajadores.item(item, values=valores)
            limpiarForm()
            lblMensaje.config(text="Trabajador actualizado", fg="green")
        else:
            lblMensaje.config(text="No debe haber registros vacíos", fg="red")

    def limpiarGrilla():
        filas = tvTrabajadores.get_children()
        for fila in filas:
            tvTrabajadores.delete(fila)

    def cargarDatos():
        limpiarGrilla()
        sql = "SELECT * FROM trabajadores"
        db.cursor.execute(sql)
        filas = db.cursor.fetchall()
        for fila in filas:
            tvTrabajadores.insert("", END, values=fila)

    # botones de acción
    btnEliminar = Button(marco, text="Eliminar", command=eliminar)
    btnEliminar.grid(row=7, column=0)

    btnNuevo = Button(marco, text="Nuevo", command=nuevo)
    btnNuevo.grid(row=7, column=1)

    btnModificar = Button(marco, text="Modificar", command=modificar)
    btnModificar.grid(row=7, column=2)


    def abrirVentanaCargos():
        ventanaCargos = Toplevel(win)
        ventanaCargos.title("Gestión de Cargos")
        ventanaCargos.geometry("600x400")

        # Variables para el formulario de Cargos
        cargo = StringVar()

        # Labels y cajas de diálogo para el formulario
        lblCargo = Label(ventanaCargos, text="Cargo")
        lblCargo.grid(row=0, column=0)
        txtCargo = Entry(ventanaCargos, textvariable=cargo)
        txtCargo.grid(row=0, column=1)

        # Función para guardar un nuevo cargo
        def guardarCargo():
            valores = (cargo.get(),)
            sql = "INSERT INTO cargos (cargo) VALUES (%s)"
            db.cursor.execute(sql, valores)
            db.conn.commit()
            limpiarFormCargos()
            cargarDatosCargos()
            lblMensajeCargos.config(text="Cargo insertado", fg="green")

        # Función para limpiar el formulario de Cargos
        def limpiarFormCargos():
            cargo.set("")

        # Función para cargar los datos de la tabla Cargos en un TreeView
        def cargarDatosCargos():
            tvCargos = ttk.Treeview(ventanaCargos)
            tvCargos.grid(row=1, column=0, columnspan=2)
            tvCargos["columns"] = ("Cargo ID", "Cargo")
            tvCargos.column("#0", width=0, stretch=0)
            tvCargos.column("Cargo ID", width=100, anchor=CENTER)
            tvCargos.column("Cargo", width=400, anchor=CENTER)
            tvCargos.heading("#0", text="")
            tvCargos.heading("Cargo ID", text="CARGO ID", anchor=CENTER)
            tvCargos.heading("Cargo", text="CARGO", anchor=CENTER)
            sql = "SELECT * FROM cargos"
            db.cursor.execute(sql)
            filas = db.cursor.fetchall()
            for fila in filas:
                tvCargos.insert("", END, values=fila)

        # Botón para guardar un nuevo cargo
        btnGuardarCargo = Button(ventanaCargos, text="Guardar", command=guardarCargo)
        btnGuardarCargo.grid(row=2, column=0)

        # Mensaje de salida
        lblMensajeCargos = Label(ventanaCargos, text="Gestión de Cargos", fg="black")
        lblMensajeCargos.grid(row=2, column=1)

        cargarDatosCargos()

    def abrirVentanaContactosEmergencia():
        ventanaContactosEmergencia = Toplevel(win)
        ventanaContactosEmergencia.title("Gestión de Contactos de Emergencia")
        ventanaContactosEmergencia.geometry("600x400")

        # Variables para el formulario de Contactos de Emergencia
        rut = StringVar()
        nombre = StringVar()
        relacioncontrabajador = StringVar()
        contacto = StringVar()

        # Labels y cajas de diálogo para el formulario
        lblRut = Label(ventanaContactosEmergencia, text="RUT")
        lblRut.grid(row=0, column=0)
        txtRut = Entry(ventanaContactosEmergencia, textvariable=rut)
        txtRut.grid(row=0, column=1)

        lblNombre = Label(ventanaContactosEmergencia, text="Nombre")
        lblNombre.grid(row=1, column=0)
        txtNombre = Entry(ventanaContactosEmergencia, textvariable=nombre)
        txtNombre.grid(row=1, column=1)

        lblRelacion = Label(ventanaContactosEmergencia, text="Relación con el Trabajador")
        lblRelacion.grid(row=2, column=0)
        txtRelacion = Entry(ventanaContactosEmergencia, textvariable=relacioncontrabajador)
        txtRelacion.grid(row=2, column=1)

        lblContacto = Label(ventanaContactosEmergencia, text="Contacto")
        lblContacto.grid(row=3, column=0)
        txtContacto = Entry(ventanaContactosEmergencia, textvariable=contacto)
        txtContacto.grid(row=3, column=1)

        # Función para guardar un nuevo contacto de emergencia
        def guardarContactoEmergencia():
            valores = (rut.get(), nombre.get(), relacioncontrabajador.get(), contacto.get())
            sql = "INSERT INTO contactosemergencia (rut, nombre, relacioncontrabajador, contacto) VALUES (%s, %s, %s, %s)"
            db.cursor.execute(sql, valores)
            db.conn.commit()
            limpiarFormContactosEmergencia()
            cargarDatosContactosEmergencia()
            lblMensajeContactosEmergencia.config(text="Contacto de Emergencia insertado", fg="green")

        # Función para limpiar el formulario de Contactos de Emergencia
        def limpiarFormContactosEmergencia():
            rut.set("")
            nombre.set("")
            relacioncontrabajador.set("")
            contacto.set("")

        # Función para cargar los datos de la tabla ContactosEmergencia en un TreeView
        def cargarDatosContactosEmergencia():
            tvContactosEmergencia = ttk.Treeview(ventanaContactosEmergencia)
            tvContactosEmergencia.grid(row=4, column=0, columnspan=2)
            tvContactosEmergencia["columns"] = ("RUT", "Nombre", "Relación con el Trabajador", "Contacto")
            tvContactosEmergencia.column("#0", width=0, stretch=0)
            tvContactosEmergencia.column("RUT", width=100, anchor=CENTER)
            tvContactosEmergencia.column("Nombre", width=150, anchor=CENTER)
            tvContactosEmergencia.column("Relación con el Trabajador", width=200, anchor=CENTER)
            tvContactosEmergencia.column("Contacto", width=100, anchor=CENTER)
            tvContactosEmergencia.heading("#0", text="")
            tvContactosEmergencia.heading("RUT", text="RUT", anchor=CENTER)
            tvContactosEmergencia.heading("Nombre", text="NOMBRE", anchor=CENTER)
            tvContactosEmergencia.heading("Relación con el Trabajador", text="RELACIÓN CON EL TRABAJADOR", anchor=CENTER)
            tvContactosEmergencia.heading("Contacto", text="CONTACTO", anchor=CENTER)
            sql = "SELECT * FROM contactosemergencia"
            db.cursor.execute(sql)
            filas = db.cursor.fetchall()
            for fila in filas:
                tvContactosEmergencia.insert("", END, values=fila)

        # Botón para guardar un nuevo contacto de emergencia
        btnGuardarContactoEmergencia = Button(ventanaContactosEmergencia, text="Guardar", command=guardarContactoEmergencia)
        btnGuardarContactoEmergencia.grid(row=5, column=0)

        # Mensaje de salida
        lblMensajeContactosEmergencia = Label(ventanaContactosEmergencia, text="Gestión de Contactos de Emergencia", fg="black")
        lblMensajeContactosEmergencia.grid(row=5, column=1)

        cargarDatosContactosEmergencia()

    def abrirVentanaCargasFamiliares():
        ventanaCargasFamiliares = Toplevel(win)
        ventanaCargasFamiliares.title("Gestión de Cargas Familiares")
        ventanaCargasFamiliares.geometry("600x400")

        # Variables para el formulario de Cargas Familiares
        rut = StringVar()
        nombre = StringVar()
        sexo = StringVar()
        parentescoid = IntVar()

        # Labels y cajas de diálogo para el formulario
        lblRut = Label(ventanaCargasFamiliares, text="RUT")
        lblRut.grid(row=0, column=0)
        txtRut = Entry(ventanaCargasFamiliares, textvariable=rut)
        txtRut.grid(row=0, column=1)

        lblNombre = Label(ventanaCargasFamiliares, text="Nombre")
        lblNombre.grid(row=1, column=0)
        txtNombre = Entry(ventanaCargasFamiliares, textvariable=nombre)
        txtNombre.grid(row=1, column=1)

        lblSexo = Label(ventanaCargasFamiliares, text="Sexo")
        lblSexo.grid(row=2, column=0)
        txtSexo = Entry(ventanaCargasFamiliares, textvariable=sexo)
        txtSexo.grid(row=2, column=1)

        lblParentesco = Label(ventanaCargasFamiliares, text="Parentesco ID")
        lblParentesco.grid(row=3, column=0)
        txtParentesco = Entry(ventanaCargasFamiliares, textvariable=parentescoid)
        txtParentesco.grid(row=3, column=1)

        # Función para guardar una nueva carga familiar
        def guardarCargaFamiliar():
            valores = (rut.get(), nombre.get(), sexo.get(), parentescoid.get())
            sql = "INSERT INTO cargasfamiliares (rut, nombre, sexo, parentescoid) VALUES (%s, %s, %s, %s)"
            db.cursor.execute(sql, valores)
            db.conn.commit()
            limpiarFormCargasFamiliares()
            cargarDatosCargasFamiliares()
            lblMensajeCargasFamiliares.config(text="Carga Familiar insertada", fg="green")

        # Función para limpiar el formulario de Cargas Familiares
        def limpiarFormCargasFamiliares():
            rut.set("")
            nombre.set("")
            sexo.set("")
            parentescoid.set(0)

        # Función para cargar los datos de la tabla CargasFamiliares en un TreeView
        def cargarDatosCargasFamiliares():
            tvCargasFamiliares = ttk.Treeview(ventanaCargasFamiliares)
            tvCargasFamiliares.grid(row=4, column=0, columnspan=2)
            tvCargasFamiliares["columns"] = ("RUT", "Nombre", "Sexo", "Parentesco ID")
            tvCargasFamiliares.column("#0", width=0, stretch=0)
            tvCargasFamiliares.column("RUT", width=100, anchor=CENTER)
            tvCargasFamiliares.column("Nombre", width=200, anchor=CENTER)
            tvCargasFamiliares.column("Sexo", width=50, anchor=CENTER)
            tvCargasFamiliares.column("Parentesco ID", width=100, anchor=CENTER)
            tvCargasFamiliares.heading("#0", text="")
            tvCargasFamiliares.heading("RUT", text="RUT", anchor=CENTER)
            tvCargasFamiliares.heading("Nombre", text="NOMBRE", anchor=CENTER)
            tvCargasFamiliares.heading("Sexo", text="SEXO", anchor=CENTER)
            tvCargasFamiliares.heading("Parentesco ID", text="PARENTESCO ID", anchor=CENTER)
            sql = "SELECT * FROM cargasfamiliares"
            db.cursor.execute(sql)
            filas = db.cursor.fetchall()
            for fila in filas:
                tvCargasFamiliares.insert("", END, values=fila)

        # Botón para guardar una nueva carga familiar
        btnGuardarCargaFamiliar = Button(ventanaCargasFamiliares, text="Guardar", command=guardarCargaFamiliar)
        btnGuardarCargaFamiliar.grid(row=5, column=0)

        # Mensaje de salida
        lblMensajeCargasFamiliares = Label(ventanaCargasFamiliares, text="Gestión de Cargas Familiares", fg="black")
        lblMensajeCargasFamiliares.grid(row=5, column=1)

        cargarDatosCargasFamiliares()

    def abrirVentanaParentezcos():
        ventanaParentezcos = Toplevel(win)
        ventanaParentezcos.title("Gestión de Parentescos")
        ventanaParentezcos.geometry("600x400")

        # Variables para el formulario de Parentescos
        parentesco = StringVar()

        # Labels y cajas de diálogo para el formulario
        lblParentesco = Label(ventanaParentezcos, text="Parentesco")
        lblParentesco.grid(row=0, column=0)
        txtParentesco = Entry(ventanaParentezcos, textvariable=parentesco)
        txtParentesco.grid(row=0, column=1)

        # Función para guardar un nuevo parentesco
        def guardarParentesco():
            valores = (parentesco.get(),)
            sql = "INSERT INTO parentezcos (parentesco) VALUES (%s)"
            db.cursor.execute(sql, valores)
            db.conn.commit()
            limpiarFormParentezcos()
            cargarDatosParentezcos()

        # Función para limpiar el formulario de Parentescos
        def limpiarFormParentezcos():
            parentesco.set("")

        # Función para cargar los datos de la tabla Parentezcos en un TreeView
        def cargarDatosParentezcos():
            # Variables para el formulario de Parentescos
            parentesco = StringVar()

            # Labels y cajas de diálogo para el formulario
            lblParentesco = Label(ventanaParentezcos, text="Parentesco")
            lblParentesco.grid(row=0, column=0)
            txtParentesco = Entry(ventanaParentezcos, textvariable=parentesco)
            txtParentesco.grid(row=0, column=1)

            # Función para guardar un nuevo parentesco
        def guardarParentesco():
            valores = (parentesco.get(),)
            sql = "INSERT INTO parentezcos (parentesco) VALUES (%s)"
            db.cursor.execute(sql, valores)
            db.conn.commit()
            limpiarFormParentezcos()
            cargarDatosParentezcos()
            lblMensajeParentezcos.config(text="Parentesco insertado", fg="green")
            
        # Función para limpiar el formulario de Parentescos
        def limpiarFormParentezcos():
            parentesco.set("")

        # Función para cargar los datos de la tabla Parentezcos en un TreeView
        def cargarDatosParentezcos():
            tvParentezcos = ttk.Treeview(ventanaParentezcos)
            tvParentezcos.grid(row=1, column=0, columnspan=2)
            tvParentezcos["columns"] = ("ID", "Parentesco")
            tvParentezcos.column("#0", width=0, stretch=0)
            tvParentezcos.column("ID", width=50, anchor=CENTER)
            tvParentezcos.column("Parentesco", width=450, anchor=CENTER)
            tvParentezcos.heading("#0", text="")
            tvParentezcos.heading("ID", text="ID", anchor=CENTER)
            tvParentezcos.heading("Parentesco", text="PARENTESCO", anchor=CENTER)
            sql = "SELECT * FROM parentezcos"
            db.cursor.execute(sql)
            filas = db.cursor.fetchall()
            for fila in filas:
                tvParentezcos.insert("", END, values=fila)
            
        # Botón para guardar un nuevo parentesco
        btnGuardarParentesco = Button(ventanaParentezcos, text="Guardar", command=guardarParentesco)
        btnGuardarParentesco.grid(row=2, column=0)
        
        # Mensaje de salida
        lblMensajeParentezcos = Label(ventanaParentezcos, text="Gestión de Parentescos", fg="black")
        lblMensajeParentezcos.grid(row=2, column=1)
        
        cargarDatosParentezcos()

    def abrirVentanaTrabajadoresCargas():
        ventanaTrabajadoresCargas = Toplevel(win)
        ventanaTrabajadoresCargas.title("Gestión de Trabajadores y Cargas")
        ventanaTrabajadoresCargas.geometry("600x400")

        # Variables para el formulario de Trabajadores y Cargas
        ruttrabajador = StringVar()
        rutcarga = StringVar()

        # Labels y cajas de diálogo para el formulario
        lblRutTrabajador = Label(ventanaTrabajadoresCargas, text="RUT Trabajador")
        lblRutTrabajador.grid(row=0, column=0)
        txtRutTrabajador = Entry(ventanaTrabajadoresCargas, textvariable=ruttrabajador)
        txtRutTrabajador.grid(row=0, column=1)

        lblRutCarga = Label(ventanaTrabajadoresCargas, text="RUT Carga")
        lblRutCarga.grid(row=1, column=0)
        txtRutCarga = Entry(ventanaTrabajadoresCargas, textvariable=rutcarga)
        txtRutCarga.grid(row=1, column=1)

        # Función para guardar una nueva relación Trabajador-Carga
        def guardarRelacionTrabajadorCarga():
            valores = (ruttrabajador.get(), rutcarga.get())
            sql = "INSERT INTO trabajadorescargas (ruttrabajador, rutcarga) VALUES (%s, %s)"
            db.cursor.execute(sql, valores)
            db.conn.commit()
            limpiarFormTrabajadoresCargas()
            cargarDatosTrabajadoresCargas()
            lblMensajeTrabajadoresCargas.config(text="Relación guardada", fg="green")

        # Función para limpiar el formulario de Trabajadores y Cargas
        def limpiarFormTrabajadoresCargas():
            ruttrabajador.set("")
            rutcarga.set("")

        # Función para cargar los datos de la tabla trabajadorescargas en un TreeView
        def cargarDatosTrabajadoresCargas():
            tvTrabajadoresCargas = ttk.Treeview(ventanaTrabajadoresCargas)
            tvTrabajadoresCargas.grid(row=2, column=0, columnspan=2)
            tvTrabajadoresCargas["columns"] = ("ID", "RUT Trabajador", "RUT Carga")
            tvTrabajadoresCargas.column("#0", width=0, stretch=0)
            tvTrabajadoresCargas.column("ID", width=50, anchor=CENTER)
            tvTrabajadoresCargas.column("RUT Trabajador", width=150, anchor=CENTER)
            tvTrabajadoresCargas.column("RUT Carga", width=150, anchor=CENTER)
            tvTrabajadoresCargas.heading("#0", text="")
            tvTrabajadoresCargas.heading("ID", text="ID", anchor=CENTER)
            tvTrabajadoresCargas.heading("RUT Trabajador", text="RUT TRABAJADOR", anchor=CENTER)
            tvTrabajadoresCargas.heading("RUT Carga", text="RUT CARGA", anchor=CENTER)
            sql = "SELECT * FROM trabajadorescargas"
            db.cursor.execute(sql)
            filas = db.cursor.fetchall()
            for fila in filas:
                tvTrabajadoresCargas.insert("", END, values=fila)

        # Botón para guardar una nueva relación Trabajador-Carga
        btnGuardarRelacion = Button(ventanaTrabajadoresCargas, text="Guardar", command=guardarRelacionTrabajadorCarga)
        btnGuardarRelacion.grid(row=3, column=0)

        # Mensaje de salida
        lblMensajeTrabajadoresCargas = Label(ventanaTrabajadoresCargas, text="Gestión de Trabajadores y Cargas", fg="black")
        lblMensajeTrabajadoresCargas.grid(row=3, column=1)

        cargarDatosTrabajadoresCargas()

    def abrirVentanaUsuarios():
        ventanaUsuarios = Toplevel(win)
        ventanaUsuarios.title("Gestión de Usuarios")
        ventanaUsuarios.geometry("600x400")

        rut = StringVar()
        nombreusuario = StringVar()
        contrasena = StringVar()
        cargo = StringVar()

        # Labels y cajas de diálogo para el formulario
        lblRut = Label(ventanaUsuarios, text="RUT")
        lblRut.grid(row=0, column=0)
        txtRut = Entry(ventanaUsuarios, textvariable=rut)
        txtRut.grid(row=0, column=1)

        lblRut = Label(ventanaUsuarios, text="RUT")
        lblRut.grid(row=0, column=0)
        txtRut = Entry(ventanaUsuarios, textvariable=rut)
        txtRut.grid(row=0, column=1)

        lblNombre = Label(ventanaUsuarios, text="Nombre de Usuario")
        lblNombre.grid(row=1, column=0)
        txtNombre = Entry(ventanaUsuarios, textvariable=nombreusuario)
        txtNombre.grid(row=1, column=1)

        lblContrasena = Label(ventanaUsuarios, text="Contraseña")
        lblContrasena.grid(row=2, column=0)
        txtContrasena = Entry(ventanaUsuarios, textvariable=contrasena, show="*")
        txtContrasena.grid(row=2, column=1)

        lblCargo = Label(ventanaUsuarios, text="Cargo")
        lblCargo.grid(row=3, column=0)
        txtCargo = Entry(ventanaUsuarios, textvariable=cargo)
        txtCargo.grid(row=3, column=1)

        def guardarUsuario():
            valoresUsuario = (rut.get(), nombreusuario.get(), hashlib.sha256(contrasena.get().encode()).hexdigest(), cargo.get())
            sql = "INSERT INTO usuarios (ruttrabajador, nombreusuario, contrasena, cargo) VALUES (%s, %s, %s, %s)"
            db.cursor.execute(sql, valoresUsuario)
            db.conn.commit()
            limpiarFormUsuarios()
            cargarDatosUsuarios()
            lblMensaje.config(text="Usuario insertado", fg="green")

        def limpiarFormUsuarios():
            rut.set("")
            nombreusuario.set("")
            contrasena.set("")
            cargo.set("")

        def cargarDatosUsuarios():
            tvUsuarios = ttk.Treeview(ventanaUsuarios)
            tvUsuarios.grid(row=4, column=0, columnspan=2)
            tvUsuarios["columns"] = ("RUT", "Nombre de Usuario", "Cargo")
            tvUsuarios.column("#0", width=0, stretch=0)
            tvUsuarios.column("RUT", width=100, anchor=CENTER)
            tvUsuarios.column("Nombre de Usuario", width=150, anchor=CENTER)
            tvUsuarios.column("Cargo", width=100, anchor=CENTER)
            tvUsuarios.heading("#0", text="")
            tvUsuarios.heading("RUT", text="RUT", anchor=CENTER)
            tvUsuarios.heading("Nombre de Usuario", text="NOMBRE DE USUARIO", anchor=CENTER)
            tvUsuarios.heading("Cargo", text="CARGO", anchor=CENTER)
            sql = "SELECT * FROM usuarios"
            db.cursor.execute(sql)
            filas = db.cursor.fetchall()

            for fila in filas:
                tvUsuarios.insert("", END, values=fila)

        btnGuardarUsuario = Button(ventanaUsuarios, text="Guardar", command=guardarUsuario)
        btnGuardarUsuario.grid(row=5, column=0)

        # Mensaje de salida
        lblMensaje = Label(ventanaUsuarios, text="Gestión de Usuarios", fg="black")
        lblMensaje.grid(row=5, column=1)

        cargarDatosUsuarios()

    # Botones para acceder a otras ventanas
    btnCargos = Button(win, text="Cargos", command=abrirVentanaCargos)
    btnCargos.place(x=50, y=550)

    btnContactosEmergencia = Button(win, text="Contactos de Emergencia", command=abrirVentanaContactosEmergencia)
    btnContactosEmergencia.place(x=250, y=550)

    btnCargasFamiliares = Button(win, text="Cargas Familiares", command=abrirVentanaCargasFamiliares)
    btnCargasFamiliares.place(x=500, y=550)

    btnParentezcos = Button(win, text="Parentescos", command=abrirVentanaParentezcos)
    btnParentezcos.place(x=650, y=550)

    btnTrabajadoresCargas = Button(win, text="Trabajadores y Cargas", command=abrirVentanaTrabajadoresCargas)
    btnTrabajadoresCargas.place(x=800, y=550)

    btnUsuarios = Button(win, text="Usuarios", command=abrirVentanaUsuarios)
    btnUsuarios.place(x=1035, y=550)

    cargarDatos()
    win.mainloop()

login_window()