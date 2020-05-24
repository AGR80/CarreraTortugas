import turtle

class Circuito(): #Abrimos la clase
    corredores = [] #Definimos la variable 'corredores' dónde alojaremos las tortugas
    __posStartY = (-30, -10, 10, 30) #Definimos la posición Y de cada tortuga
    __colorTurtle = ('red', 'blue', 'green', 'orange') #Definimos el color de cada tortuga
    
    def __init__(self, width, height): #Definimos la clase Circuito
        self.__screen = turtle.Screen() #Definimos la variable screen (pantalla) que utilizará el módulo Screen Turtle
        self.__screen.setup(width, height) #Definimos el ancho y alto de la pantalla
        self.__screen.bgcolor('lightgray') #Definimos el color de la pantalla
        self.__startLine = -width/2 + 20 #Definimos la linea de comienzo de la carrera en la pantalla
        self.__finishLine = width/2 - 20 #Definimos la linea de fin de la carrera en la pantalla
        
        self.__createRunners()
        
    def __createRunners(self):    
        for i in range(4):
            new_turtle = turtle.Turtle() # Creamos las 4 tortugas
            new_turtle.color(self.__colorTurtle[i]) # Asignamos el color a las tortugas
            new_turtle.shape('turtle') #Comando para asignar al objeto forma de tortuga
            new_turtle.penup() # Comando para que la tortuga no pinte el recorrido
            new_turtle.setpos(self.__startLine, self.__posStartY[i]) #Asignamos a cada tortuga su posición en la pantalla

            self.corredores.append(new_turtle) #Asignamos cada tortuga dentro de la variable 'corredores'
        
        
 
if __name__ == '__main__':
    circuito = Circuito(640, 480)
     