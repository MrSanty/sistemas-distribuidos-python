class appView:
  def sendData( self, conn, data ):
    return conn.sendall( bytes( str( data ), 'utf-8' ))
    