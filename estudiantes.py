#importamos la libreria
from logging import getLogRecordFactory
from msilib.schema import ComboBox
from tkinter import *
from turtle import width
from tkinter import ttk
import pymysql

#creamos la clase student
class Student:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Sistema Administrador de Estudiantes")  # Titulo
        self.ventana.geometry("1340x700+0+0")  # Tamanio de la ventana
        self.ventana.resizable(False, False)  # No permitir al usuario que modifique la ventana

        ##############################################################################################################

        title = Label(self.ventana, text="Sistema Administrador de Estudiantes", bd=10, relief=RAISED, font=("Arial", 40, "bold"), bg="green", fg="white")
        title.pack(side=TOP)
        
        ##=============== VARIABLES ==============##
        self.matricula_var = StringVar()
        self.nombre_var = StringVar()
        self.email_var = StringVar()
        self.genero_var = StringVar()
        self.telefono_var = StringVar()
        self.fdn_var = StringVar()



        Manage_Frame = Frame(self.ventana, bd=4, relief=RIDGE, bg="green")
        Manage_Frame.place(x=20, y=100, width=520, height=580)

        m_title = Label(Manage_Frame,text="Control de Estudiantes", bg='yellow', fg="red", font=("Arial", 30, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        ####### MATRICULA #######################################################################################################

        lbl_roll = Label(Manage_Frame, text="Matricula:", bg="yellow", fg="red", font=("Arial", 20, "bold"))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky='w')

        txt_Roll = Entry(Manage_Frame, textvariable=self.matricula_var, font=("Arial", 15, "bold"), bd=5,  relief=GROOVE)
        txt_Roll.grid(row=1, column=1, pady=10, padx=20, sticky='w')

        ####### NOMBRE #######################################################################################################

        lbl_name = Label(Manage_Frame, text="Nombre:", bg="yellow", fg="red", font=("Arial", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky='w')

        txt_name = Entry(Manage_Frame, textvariable=self.nombre_var, font=("Arial", 15, "bold"), bd=5,  relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky='w')

        ####### CORREO #######################################################################################################


        lbl_email = Label(Manage_Frame, text="Correo:", bg="yellow", fg="red", font=("Arial", 20, "bold"))
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky='w')

        txt_email = Entry(Manage_Frame, textvariable=self.email_var, font=("Arial", 15, "bold"), bd=5,  relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky='w')

        ####### GENERO #######################################################################################################

        lbl_gene = Label(Manage_Frame, text="Genero:", bg="yellow", fg="red", font=("Arial", 20, "bold"))
        lbl_gene.grid(row=4, column=0, pady=10, padx=20, sticky='w')

        combo_genero = ttk.Combobox(Manage_Frame, textvariable=self.genero_var, width=9, font=("Arial", 15, "bold"), state="readonly")
        combo_genero["values"] = ("Masculino", "Femenino", "otros")
        combo_genero.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        ####### TELEFONO #######################################################################################################

        lbl_tel = Label(Manage_Frame, text="Telefono:", bg="yellow", fg="red", font=("Arial", 20, "bold"))
        lbl_tel.grid(row=5, column=0, pady=10, padx=20, sticky='w')

        txt_tel = Entry(Manage_Frame, textvariable=self.telefono_var, font=("Arial", 15, "bold"), bd=5,  relief=GROOVE)
        txt_tel.grid(row=5, column=1, pady=10, padx=20, sticky='w')

        ####### FECHA DE NACIMIENTO #######################################################################################################

        lbl_fdn = Label(Manage_Frame, text="F.D.N :", bg="yellow", fg="red", font=("Arial", 20, "bold"))
        lbl_fdn.grid(row=6, column=0, pady=10, padx=20, sticky='w')

        txt_fdn = Entry(Manage_Frame, textvariable=self.fdn_var, font=("Arial", 15, "bold"), bd=5,  relief=GROOVE)
        txt_fdn.grid(row=6, column=1, pady=10, padx=20, sticky='w')

        ####### DOMICILIO #######################################################################################################

        lbl_domi = Label(Manage_Frame, text="Domicilio:", bg="yellow", fg="red", font=("Arial", 20, "bold"))
        lbl_domi.grid(row=7, column=0, pady=10, padx=20, sticky='w')

        self.txt_domi=Text(Manage_Frame, width = 30, height =4, font=("Arial", 10 , "bold"))
        self.txt_domi.grid(row=7, column=1, pady=10, padx=20, sticky='w')

        ##############################################################################################################

        btn_Frame = Frame(self.ventana, bd=4, relief=RIDGE, bg="blue")
        btn_Frame.place(x=25, y=625, width=420)

        add_btn = Button(btn_Frame, text="Agregar", width=7, command=self.agregar_estudiantes)
        add_btn.grid(row=0, column=0, padx=10, pady=10)

        ##############################################################################################################

        add_btn = Button(btn_Frame, text="Actualizar", width=7)
        add_btn.grid(row=0, column=1, padx=10, pady=10)

        ##############################################################################################################

        add_btn = Button(btn_Frame, text="Borrar", width=7)
        add_btn.grid(row=0, column=2, padx=10, pady=10)

        ##############################################################################################################

        add_btn = Button(btn_Frame, text="Limpiar", width=7)
        add_btn.grid(row=0, column=3, padx=10, pady=10)

        ##############################################################################################################

        Detail_Frame = Frame(self.ventana, bd=4, relief=RIDGE, bg='green')
        Detail_Frame.place(x=550, y=110, width=810, height=580)

        lbl_search = Label(Detail_Frame, text="Buscar por: ", bg="yellow", fg="red", font=("Arial",20,"bold"))
        lbl_search.grid(row=0, column=0, pady=10, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame, width=10, font=("Arial", 15, "bold"), state='readonly')
        combo_search ['values'] = ("Matricula", "Nombre", "Telefono")
        combo_search.grid(row=0, column=2, padx=20, pady=10)

        ##############################################################################################################

        #PARCIAL

        txt_search = Entry(Detail_Frame, width=20, font=("Arial", 11, "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=3, pady=10, padx=20, sticky="w")

        ##############################################################################################################
        
        search_btm = Button(Detail_Frame, text="Buscar", width=7)
        search_btm.grid(row=0, column=4, padx=10, pady=10)

        ##############################################################################################################

        showall_btn= Button(Detail_Frame, text="Mostrar Todo", width=10)
        showall_btn.grid(row=0, column=5, padx=10, pady=10)

        ##############################################################################################################

        Table_Frame = Frame(Detail_Frame, bd=4, relief= RIDGE, bg="crimson")
        Table_Frame.place(x=10, y=70, width=760, height=500)

        ##############################################################################################################

        scroll_x = Scrollbar(Table_Frame, orient= HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient= VERTICAL)

        Student_table = ttk.Treeview(Table_Frame, column= ("matricula" , "nombre", "email", "genero", "telefono", "fdn", "domicilio"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        #Empacando Scrolls

        scroll_x.pack(side= BOTTOM, fill=X)
        scroll_y.pack(side= RIGHT, fill=Y)
        scroll_x.config(command=Student_table.xview)
        scroll_y.config(command=Student_table.yview)
        Student_table.heading("matricula", text="Matricula")
        Student_table.heading("nombre", text="Nombre")
        Student_table.heading("email", text="Correo E")
        Student_table.heading("genero", text="Genero")
        Student_table.heading("telefono", text="Telefono")
        Student_table.heading("fdn", text="F.D.N")
        Student_table.heading("domicilio", text="Domicilio")

        Student_table ["show"] = "headings"
        Student_table.column("matricula", width=100)
        Student_table.column("nombre", width=100)
        Student_table.column("email", width=100)
        Student_table.column("genero", width=100)
        Student_table.column("telefono", width=100)
        Student_table.column("fdn", width=100)
        Student_table.column("domicilio", width=160)

        Student_table.pack(fill=BOTH, expand=1)

        #Aqui termina el diseño estetico de la aplicacion, sigue la parte logica 

        ##############################################################################################################


    def agregar_estudiantes(self):
        con = pymysql.connect(host="localhost", user= "root", password="0524", database="studentm")
        cur=con.cursor()
        cur.execute("insert into students values (%s, %s, %s, %s, %s, %s, %s)",(
                                                  self.matricula_var.get(),
                                                  self.nombre_var.get(),
                                                  self.email_var.get(),
                                                  self.genero_var.get(),
                                                  self.telefono_var.get(),
                                                  self.fdn_var.get(),
                                                  self.txt_domi.get('1.0', END)))
        con.commit()
        con.close()

ventana = Tk()  #llamar la libreria tkinter
ob = Student(ventana)
ventana.mainloop()