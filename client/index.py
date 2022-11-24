from tkinter import * #Libreria para desarrollar interfaz grafica
from datetime import datetime
from helpers.controlView import changeView
from helpers.controlView import cleanGrid

def mainMenu( root ):
  root.title("MENÚ")
  root.geometry("650x350")
  root.config( bg = "#2d2d2d" ) 
  root.resizable(0,0)
  
  """ Titulo y Fecha """
  Label( 
    text = "Menú Pokemon", bg = "#2d2d2d", fg = "white", font = ('Arial', 13, 'bold')
  ).grid( pady = 10, row = 0, column = 0 )
  Label(
    text = f"Fecha: { datetime.today().strftime('%Y-%m-%d') }", bg = "#2d2d2d", fg = "white", font = ('Arial', 13, 'bold')
  ).grid( pady = 10, row = 0, column = 1 )
  
  
  """ Menu """
  Button(
    root,
    text = "Todos", cursor = "hand2", relief = "flat", width = "25", bg = "#2f4f4f", fg = "white", font = ('Arial', 13, 'bold'),
    command = lambda: changeView( root, "Todos" )
  ).grid( pady = 5, padx = 10,column = 0, row = 2 )
  
  Button(
    root,
    text = "Filtrar por codigo", cursor = "hand2", relief = "flat", width = "25", bg = "#2c5545", fg = "white", font = ('Arial', 13, 'bold'),
    command = lambda: changeView( root, "Filtrar por codigo" )
  ).grid( pady = 5,padx = 10, column = 1, row = 2 )
  
  Button(
    root,
    text = "Filtrar por tipo", cursor = "hand2",relief = "flat", width = "25", bg = "#008080", fg = "white", font = ('Arial', 13, 'bold'),
    command = lambda: changeView( root, "Filtrar por tipo" )
  ).grid( pady = 5,padx = 10, column = 0, row = 3 )
  
  Button(
    root,
    text = "Filtrar por habilidades", cursor = "hand2",relief = "flat", width = "25", bg = "#025669", fg = "white", font = ('Arial', 13, 'bold'),
    command = lambda: changeView( root, "Filtrar por habilidades" )
  ).grid( pady = 5,padx = 10, column = 1, row = 3 )
  
  Button(
    root,
    text = "Filtrar por Experiencia", cursor = "hand2",relief = "flat", width = "25", bg = "#1b5583", fg = "white", font = ('Arial', 13, 'bold'),
    command = lambda: changeView( root, "Filtrar por Experiencia" )
  ).grid( pady = 20, row = 4, column = 0, columnspan = 2 )

  
  root.mainloop()
  
if __name__ == "__main__":
  mainMenu( Tk() )
