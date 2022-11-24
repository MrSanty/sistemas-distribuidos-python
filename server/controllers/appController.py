import socket
import threading
from views.appView import appView
from models.appModel import appModel

class appController:
  def __init__( self ):
    self.appModel = appModel()
    self.appView = appView()
    self.appModel.updateEvery5Seconds()
  
  def server( self ):
    while True:
      with socket.socket( socket.AF_INET, socket.SOCK_STREAM ) as s:
        s.bind(( 'localhost', 8080 ))
        s.listen()
        conn, addr = s.accept()
        with conn:
          print( 'Connected by', addr )
          while True:
            data = conn.recv( 1024 )
            if not data:
              break
            self.readData( conn, data.decode('utf-8') )
            
  def hilo( self ):
    h = threading.Thread( target = self.server, args = () )
    h.daemon = True
    h.start()
    
  def readData( self, conn, data ):
    data = eval( data )
    print( data[0] )
    if data[0] == 'all':
      self.appView.sendData( conn, self.appModel.getAll() )
    elif data[0] == 'code':
      self.appView.sendData( conn, self.appModel.getByCode( data[1] ) )
    elif data[0] == 'type':
      self.appView.sendData( conn, self.appModel.getFilterByType( data[1] ) )
    elif data[0] == 'ability':
      self.appView.sendData( conn, self.appModel.getFilterByAbility( data[1] ) )
    elif data[0] == 'experience':
      self.appView.sendData( conn, self.appModel.getFilterByExperience( data[1], data[2] ) )