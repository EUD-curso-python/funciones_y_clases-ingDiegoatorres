global1 = 34

def cambiar_global(arg1):
    '''Cambiar una variable global

    Esta función debe asignarle a la variable global `global1` el valor que se
    le pasa como único argumento posicional.
    '''
    global global1
    global1 = arg1    
    

def anio_bisiesto(valor):
    '''Responder si el entero pasado como argumento es un año bisiesto
    
    Para determinar si un año es bisiesto, se deben tener en cuenta las 
    siguientes condiciones:

    - Si el año es divisible por 4 es bisiesto, a menos que:
        - Si el año es divisible por 100 no es bisiesto a menos que:
            - Si el año es divisible por 400 es bisiesto.

    Retorna True o False
    '''
    result = False;
    if valor % 4 == 0:
      result = True;
    if valor % 100 == 0:
      result = False
    if valor % 400 == 0:
      result = True
    return result;
    



def contar_valles(pasos):
    '''Contar el número de valles

    Esta función debe recibir como argumento una lista de -1's, 0's y 1's, y lo 
    que representan son las subidas y las bajadas en una ruta de caminata. -1
    representa un paso hacia abajo, el 0 representa un paso hacia adelante y el 
    1 representa un paso hacia arriba, entonces por ejemplo, para la lista
    [-1,1,0,1,1,-1,0,0,1,-1,1,1,-1,-1] representa la siguiente ruta:

                /\
         /\__/\/  \
       _/  
     \/

    El objetivo de esta función es devolver el número de valles que estén 
    representados en la lista, que para el ejemplo que se acaba de mostrar es
    de 3 valles.
    '''
    valles = 0
    bajando = False   
    for i in pasos:
      if (i == -1):
        bajando = True
      if (i == 1):
        if bajando:
          valles += 1          
        bajando = False
    return valles;
#print(contar_valles([-1,1,0,1,1,-1,0,0,1,-1,1,1,#-1,-1]))


def saltando_rocas(rocas):
    '''Mínimo número de saltos en las rocas

    Esta función hace parte de un juego en el que el jugador debe cruzar un río
    saltando de roca en roca hasta llegar al otro lado. Hay dos tipo de rocas, 
    secas y húmedas, y el jugador debe evitar saltar encima de las húmedas para 
    no resbalarse y caer. Además el jugador puede saltar 1 o 2 rocas, siempre y 
    cuando no caiga en una húmeda.

    Esta función debe recibir como argumento una lista de ceros y unos. Los ceros 
    representan las rocas secas y los unos las húmedas.
    El objetivo es devolver el número mínimo de saltos que debe realizar el 
    jugador para ganar la partida
    '''
    saltos = 0
    print(rocas)
    i=-1
    while (i<len(rocas)-1):    
      saltos += 1      
      print (i, saltos)
      if (i<len(rocas)-2 and rocas[i+2] == 0 ): 
        i+= 2
        print('yes', i)
        continue

      if (i<len(rocas)-1 and rocas[i+1] == 0):
        i+= 1
        print('yes2')
        continue
      i+=1
      print ('no')
    return saltos
print(saltando_rocas([0,0,0]))

    

def pares_medias(medias):
    '''Contar pares de medias

    Esta función debe recibir como argumento una lista de enteros. Cada elemento
    de esta lista representa el color de una media, y por lo tanto si hay dos 
    elementos que tienen el mismo entero, esas dos medias tienen el mismo color.
    El objetivo de esta función es devolver un diccionario cuyas keys son cada 
    uno de los colores que se encuentren en la lista, y los valores son la 
    cantidad de pares que se han encontrado para cada color.
    '''
    ans = dict({})
    for media in medias:      
      numero = ans.get(media)
      if numero == None:
        numero = 0
      ans[media] = numero+1    
    for key in ans.keys():
      ans[key] = int(ans[key]/2)
    
    return ans

#print(pares_medias([1,1,1,2,2,2,1]))

# Crear una clase llamada `ListaComa` que reciba en su constructor un iterable
# con el valor inicial para una lista que se guardará en un atributo llamado 
# `lista`. Implementar el método __str__ para que devuelva un string con todos
# los elementos del atributo `lista` unidos a través de comas. Ejemplo:
# si `lista` es [1,2,3,4], __str__ debe devolver '1,2,3,4'
class ListaComa:
  def __init__ (self, iterable_var):
    self.lista = iterable_var

  def __str__(self):
    resultado = ''
    for elemento in self.lista:
      if (len(resultado)>0):
        resultado+=','      
      resultado += str(elemento)
    print('Calculado = ' + resultado)
    print('Profesor  = ' + ','.join([str(el) for el in self.lista]))
    return resultado


a = ListaComa([1,2,3,4])
print('[' + str(a) + "]")

  

# Crear una clase llamada `Persona` que reciba en su constructor como 1er 
# argumento un iterable con el valor inicial para una lista que se guardará en
# un atributo llamado `nombres` y como 2do argumento un iterable con el valor 
# inicial para una lista que se guardará en un atributo llamado `apellidos`.
# Antes de guardar estos atributos se debe verificar que todos los elementos 
# de estas dos listas deben ser de tipo str y procesar todos los elementos de
# cada una de las dos listas para que su primera letra sea mayúscula y las demás
# minúsculas.
#
# Implementar el método `nombre_completo` para que devuelva un string con todos 
# los elementos de `nombres` concatenados con espacio, y esto a su vez 
# concatenado con todos los elementos de `appelidos` concatenados con espacio.
# Ejemplo:
# si `nombres` es ['Juan', 'David'] y `apellidos` es ['Torres', 'Salazar'],
# el método `nombre completo` debe devolver  'Juan David Torres Salazar'
class Persona:
    def __init__(self, iterable_arg, iterable_arg2):
      self.nombres = list()
      for obj in iterable_arg:        
        if not isinstance(obj, str):
          raise Exception('Eleento en iterable de nombres no es Strnig')
        self.nombres.append(obj.capitalize())
      self.apellidos= list()
      for obj in iterable_arg2:        
        if not isinstance(obj, str):
          raise Exception('Eleento en iterable de apellidos no es Strnig')
        self.apellidos.append(obj.capitalize())
    def nombre_completo(self):
      ans = '';
      for nombre in self.nombres:
        if len(ans)>0:
          ans+= ' '
        ans+=nombre
      for apellido in self.apellidos:
        ans+=' ' + apellido
      return ans

#p = Persona(['Alvaro','Pablo','Daniel',],['Infante','Rojas']);
#print(p.nombre_completo())

# Crear una clase llamada `Persona1` que herede de la clase `Persona`, y que en su
# constructor reciba además de los atributos del padre, una variable tipo 
# `datetime` como 3er argumento para guardar en atributo `fecha_nacimiento`.
#
# Implementar el método `edad` para que devuelva un `int` que represente la edad
# de la persona y que se calcule restando los años entre la fecha actual y 
# el atributo `fecha_nacimiento`.
# Ejemplo:
# si `fecha_nacimiento` es 1985-10-21 y la fecha actual es 2020-10-20, el método
# `edad` debe devover 35.
from datetime import date

class Persona1(Persona):
  def __init__ (self, iterable_arg, iterable_arg2, nacimiento):
    super().__init__(iterable_arg, iterable_arg2)
    
    self.fecha_nacimiento = nacimiento

  def edad(self):    
    diferencia =  date.today().year - int(self.fecha_nacimiento.year)
    if date.today().month < self.fecha_nacimiento.month:
      diferencia-= 1
    elif date.today().month ==  self.fecha_nacimiento.month   and date.today().day <  self.fecha_nacimiento.day:
      diferencia-= 1
    return diferencia
    #t = date.now()
    #return (t.year - self.fecha_nacimiento.year) - (1 if t #< date(t.year, self.fecha_nacimiento.month, #self.fecha_nacimiento.day) else 0)


p = Persona1(['Alvaro','Pablo','Daniel'],['Infante','Rojas'],date.fromisoformat('1982-02-27'))
print('Edad', p.edad())