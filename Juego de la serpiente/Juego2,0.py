
""""
INTEGRANTES:

KATY ALVARADO
ALICIA ULLOA
STEPHANIE MACHADO
CIELO SANCHEZ


"""


import turtle
import time
import random
import winsound

posponer = 0.1

#Marcador
score = 0
high_score = 0

#Configuracion de la ventana
wn = turtle.Screen()
wn.title("Circle Snake 4.0")
wn.bgcolor("black")
wn.setup(width = 600, height = 600)
wn.tracer(0)
# Agregar fondo
wn.bgpic("fondo.gif")


#Cabeza serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("yellow")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

#Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("purple")
comida.penup()
comida.goto(0,100)

#Segmentos
segmentos = []

#Texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("black")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0     High Score: 0", align = "center", font =("Courier", 24, "normal"))

#Funciones
def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def izquierda():
    cabeza.direction = "left"
def derecha():
    cabeza.direction = "right"

def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
        
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

#Función para escribir "Game Over"
def game_over():
    game_over = turtle.Turtle()
    game_over.speed(0)
    game_over.color("white")
    game_over.penup()
    game_over.hideturtle()
    game_over.goto(0, 0)
    game_over.write("GAME OVER", align="center", font=("Courier", 30, "normal"))
    
    turtle.ontimer(game_over.clear, t=2000)

#Teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

while True:
    wn.update()
    

    #Colisiones bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        cabeza.goto(0, 0)
        cabeza.direction = "stop"
       
        #Play boom
        winsound.PlaySound("boom", winsound.SND_ASYNC)
        
        #Esconder los segmentos
        for segmento in segmentos:
            segmento.goto(1000,1000)
            
        #Limpiar lista de segmentos
            segmento.clear()
         
        game_over()
           
        #Resetear marcador
        score = 0
        texto.clear()   
        texto.write("Score: {}     High Score: {}".format(score, high_score), 
                align = "center", font =("Courier", 24, "normal"))
        
      
 
    #Colisiones comida
    if cabeza.distance(comida) < 20: 
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x,y)
        
        #Play beep
        winsound.Beep(440, 100)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("circle")
        nuevo_segmento.color("yellow")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)
         
        

        #Aumentar marcador 
        score += 1
         
        if score > high_score: 
           high_score = score 

        texto.clear()   
        texto.write("Score: {}    High Score: {}".format(score, high_score), 
                align = "center", font =("Courier", 24, "normal"))
    
    #Mover el cuerpo de la serpiente
    totalSeg = len(segmentos)
    for index in range(totalSeg -1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x,y)

    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)

    mov()

    #Colisiones con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep
            cabeza.goto(0,0)
            cabeza.direction = "stop"
            
           #Play boom
            winsound.PlaySound("boom", winsound.SND_ASYNC)


            #Esconder los segmentos
            for segmento in segmentos:
                segmento.goto(1000,1000)

            segmentos.clear()

            game_over()
            
            score = 0
            texto.clear()   
            texto.write("Score: {}    High Score: {}".format(score, high_score), 
                align = "center", font =("Courier", 24, "normal"))
            
    
            
        
    time.sleep(posponer)
