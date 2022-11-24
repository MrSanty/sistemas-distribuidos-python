import requests
import threading

class appModel:
  db = {}
  
  def updateData( self ):
    for i in range( 1, 151 ):
      req = requests.get( f'https://pokeapi.co/api/v2/pokemon/{i}/' )
      data = req.json()
      dataTemp = {
        'code': data['id'],
        'name': data['name'],
        'type': data['types'][0]['type']['name'],
        'ability': data['abilities'][0]['ability']['name'],
        'experience': data['base_experience']
      }
      self.db[ data['id'] ] = dataTemp
    print('Updated db')
  
  def updateEvery5Seconds( self ):
    threading.Timer( 5, self.updateEvery5Seconds ).start()
    self.updateData()
    
  def getAll( self ):
    return self.db
  
  def getByCode( self, code ):
    return self.db[ int(code) ]
  
  def getFilterByType( self, type ):
    return [ item for item in self.db.items() if item[1]['type'] == type ]

  def getFilterByAbility( self, ability ):
    return [ item for item in self.db.values() if item['ability'] == ability ]
  
  def getFilterByExperience( self, experience, operator ):
    return [ item for item in self.db.values() if eval( f'{item["experience"]} {operator} {experience}' ) ]