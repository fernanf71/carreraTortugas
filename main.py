import turtle

class Circuito():
    corredores = [] #lista vacía
    __posStartY = (-30, -10, 10, 30)
    __colorTurtle = ('red', 'blue', 'green', 'orange')
    
    def __init__(self, width, height): # tamaño de la pantalla donde se va a realizar la carrera.
        # self.width = width  # al poner abajo "self.screen.setup(width, height)", este atributo y el siguiente no hacen falta.
        # self.height = height
        
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor('lightgray')
        self.__starline = -width/2 + 20 # si el centro de la pantalla es (0,0) y queremos empezar la carrera en el margen izquierdo, dividimos el ancho de la pantalla en dos y desplazamos a la izqda con el signo (-). Sumamos 20 para que no quede pegado al margen.
        self.__finishline = width/2 - 20 # línea donde acaba la carrera.
        
        self.__createRunners() #inicializo a los corredores. Poner esto aquí es buena práctica, pero podría omitirse junto a la definición de la función "def __createRunners(self):"
    
    def __createRunners(self): # es buena práctica poner esto bajo una función, para diferencia la parte de pantalla (arriba) y la de abajo (corredores-tortugas-)        
        for i in range(4): # esto es para la creación de cada una de las tortugas. Crea los 4 "corredores".
            new_turtle = turtle.Turtle() # le estoy asignando siempre la etiqueta "new_turtle", pero me da igual siempre darle el mismo nombre ("new_tutle"), puesto que en la línea siguiente la estoy metiendo en la lista "corredores".
            new_turtle.color(self.__colorTurtle[i])
            new_turtle.shape('turtle')
            new_turtle.penup() # levantar el lápiz; para que no dibuje las rayas cuando van del centro pantalla al margen izquierdo.
            new_turtle.setpos(self.__starline, self.__posStartY[i])
            
        
            self.corredores.append(new_turtle)


if __name__ == '__main__': # si utilizaramos este código como Módulo, no ejecutaría este "if". Este "if" no pertenece a la clase.
        circuito = Circuito(640, 640) # con esta instancia, se "forma" la pantalla con el fondo gris del tamaño indicado.
        
'''
Para acceder al atributo privado, indico el siguiente código:

c = Circuito(250, 250)
c.__screen (da error, por que es privado)

Si accedo para hacerlo "no privado", tendría que poner el siguiente código:

c._Circuito__screen (con esto te sale la dirección de memoria dónde está y, por tanto, te ha dejado acceder)

c._Circuito__screen.bgcolor('black')  (con esto, se pone la pantalla negra)

Puedo poner los siguiente para que avance la tortuga:

circuito
circuito.corredores[0].fd(50)
circuito.corredores[1].left(90) #para que gire 90 grados.
circuito.corredores[2].pos() # para que me cree la posición en la pantalla donde se hubicará una de las tortugas. Por defecto, si no pongo nada entre paréntesis, da la posición (0,0)
                                la posición (0,0) es el punto central de la pantalla. 
'''
