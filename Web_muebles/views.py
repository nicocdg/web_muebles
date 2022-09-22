from django.http import HttpResponse
from django.template import loader
from DBweb_muebles.models import *



def addMuebles(self): 

    sillon1 = Sillones(modelo="Mertcio", material="Cuero", cuerpos="1")
    sillon2 = Sillones(modelo="Sombra", material="Hierro", cuerpos="2")   
    mesa1 = Mesas(modelo="Chiqui", material="Madera", capacidadPersonas="4")
    mesa2 = Mesas(modelo="Wanda", material="Vidrio", capacidadPersonas="8")
    armario1 = Armarios(modelo="Flaco", material="Madera", puertas="2")
    armario2 = Armarios(modelo="Ronco", material="Hierro", puertas="4")
    myList = [sillon1, sillon2, mesa1, mesa2, armario1, armario2]

    for n in myList:
        n.save()

    return HttpResponse("Se agregaron los muebles a la base de datos")

def sillonesFromDB(self): #shows data but not from DB, sadly D:
    sillones = Sillones.objects.all() #get data from DBsqlite
  
    data = {'dataListDB': sillones}

    template = loader.get_template('sillonesFromDB.html')
    document = template.render(data)    
    return HttpResponse(document)

def mesasFromDB(self): #shows data but not from DB, sadly D:
    mesas = Mesas.objects.all() #get data from DBsqlite
  
    data = {'dataListDB': mesas}

    template = loader.get_template('mesasFromDB.html')
    document = template.render(data)    
    return HttpResponse(document)

def armariosFromDB(self): #shows data but not from DB, sadly D:
    armarios = Armarios.objects.all() #get data from DBsqlite
  
    data = {'dataListDB': armarios}

    template = loader.get_template('armariosFromDB.html')
    document = template.render(data)    
    return HttpResponse(document)
