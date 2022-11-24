from views.allView import all
from views.filterByCodeView import filterByCode
from views.filterByTypeView import filterByType
from views.filterByAbilityView import filterByAbility
from views.filterByExperienceView import filterByExperience



def cleanGrid( root ):
  list = root.grid_slaves()
  for l in list:
    l.destroy()
    
def changeView( root, view ):
  cleanGrid( root )
  if view == "Todos":
    all( root )
  elif view == "Filtrar por codigo":
    filterByCode( root )
  elif view == "Filtrar por tipo":
    filterByType( root )
  elif view == "Filtrar por habilidades":
    filterByAbility( root )
  elif view == "Filtrar por Experiencia":
    filterByExperience( root )