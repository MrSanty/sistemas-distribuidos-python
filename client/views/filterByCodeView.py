from tkinter import * #Libreria para desarrollar interfaz grafica
from tkinter import ttk
from tkinter import messagebox
from helpers.restart import comeBack
import socket

def filterByCode( root ):
  def delete():
    for i in treev.get_children():
      treev.delete(i)

  def search():
    if cod.get() == '':
      messagebox.showinfo(
        message = "No se ha ingresado un codigo",
        title = "Error"
      )
      return
    elif int(cod.get()) < 1 or int(cod.get()) > 150:
      messagebox.showinfo(
        message = "El codigo debe estar entre 1 y 150",
        title = "Error"
      )
      return
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.connect(( 'localhost', 8080 ))
      array = [ 'code', cod.get(), '' ]
      s.sendall( bytes( str( array ), 'utf-8' ))
      data = s.recv(15000)
      db = eval( data.decode( 'utf-8' ))
      delete()
      treev.insert("", 'end', text ="L1", values =(db['code'], db['name'], db['type'], db['ability'], db['experience']))
  
  container = ttk.Frame( root, style = "Container.TFrame" )
  ttk.Style().configure( "Container.TFrame", background = "#2d2d2d", foreground = "white", font = ('Arial', 13, 'bold'), marginx = 10 )
  Label( text = "Buscar por codigo", bg = "#2d2d2d", width = '15', fg = "white", font = ('Arial', 13, 'bold') ).pack( in_ = container, side = LEFT, anchor = NW, pady = 10, padx = 10 )
  Button( root, text = "Regresar", cursor = "hand2", relief = "flat", width = "10", bg = "#2f4f4f", fg = "white", font = ('Arial', 13, 'bold'), command=lambda: comeBack( root )).pack( in_ = container, side = RIGHT, pady = 10, padx = 10 )
  
  container.pack( side = TOP, fill = 'x' )
  
  container2 = ttk.Frame( root, style="Container.TFrame" )
  cod = StringVar()
  Entry( root, textvariable = cod, width = 10, font = ('Arial', 13, 'bold') ).pack( in_ = container2, side = LEFT, pady = 10, padx = 10 )
  Button( root, text = "Buscar", cursor = "hand2", relief = "flat", width = "10", bg = "#2f4f4f", fg = "white", font = ('Arial', 13, 'bold'), command = lambda: search() ).pack( in_ = container2, side = LEFT, pady = 10, padx = 10 )
  container2.pack( side = TOP, fill = 'x' )

  container3 = ttk.Frame( root, style = "Container.TFrame" )
  treev = ttk.Treeview( root, selectmode = 'browse', style = "Container.TFrame" )
  treev.pack( in_ = container3, side = LEFT, fill = 'x', expand = True, pady = 10, padx = 10 )

  verscrlbar = ttk.Scrollbar( root, orient = "vertical", command = treev.yview )
  verscrlbar.pack( in_ = container3, side = RIGHT, fill = 'y' )

  # Configuring treeview
  treev.configure(xscrollcommand = verscrlbar.set)
  treev["columns"] = ("1", "2", "3", "4", "5")
  treev['show'] = 'headings'

  treev.column("1", width = 40, anchor ='c')
  treev.column("2", width = 40, anchor ='c')
  treev.column("3", width = 40, anchor ='c')
  treev.column("4", width = 40, anchor ='c')
  treev.column("5", width = 40, anchor ='c')

  treev.heading("1", text = "Codigo")
  treev.heading("2", text = "Nombre")
  treev.heading("3", text = "Tipo")
  treev.heading("4", text = "Habilidad")
  treev.heading("5", text = "Experiencia")
  container3.pack( side = TOP, fill = 'x' )