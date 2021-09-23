
#Drawing desert
import turtle as screen
screen.pensize(130)
screen.speed(300)
screen.bgcolor("wheat")
screen.penup()
screen.goto(-500,0)
screen.pendown()
screen.forward(1000)
screen.penup()

screen.pensize(20)
screen.pencolor("yellow")
screen.goto(-500,0)
screen.pendown()
screen.forward(1000)

screen.pensize(8)
screen.pencolor("black")
screen.goto(-500,0)
screen.pendown()
screen.forward(1000)




#Gorrila code
import turtle as gorilla
screen_h = 400
screen_w = 420
startx = -120
starty = 0
turtle_scale = 1.5

import time
def fxn():
   gorilla.forward(120)
   time.sleep(0.1)

gorilla.onkey(fxn,'Up')
def fxn1():
   gorilla.forward(-120)
   time.sleep(0.1)
gorilla.onkey(fxn1,'Down')

gorilla.listen()



#setup gorilla
wn = gorilla.Screen()
wn.setup(width=screen_w, height=screen_h)

gorilla_image = "big gorilla.gif"
wn.addshape(gorilla_image)

gorilla = gorilla.Turtle(shape=gorilla_image)
gorilla.hideturtle()
gorilla.color("darkorchid")
gorilla.penup()
gorilla.setheading(90)
gorilla.turtlesize(turtle_scale, turtle_scale)
gorilla.goto(startx, starty)
gorilla.speed(2)
gorilla.showturtle()


#cactus code
import turtle as cactus
wne = cactus.Screen()
wne.setup(width=screen_w, height=screen_h)

cactus_image = "ok cactus.gif"
wne.addshape(cactus_image)
cactus = cactus.Turtle(shape=cactus_image)
cactus.hideturtle()
cactus.penup()
cactus.setheading(90)
cactus.turtlesize(turtle_scale, turtle_scale)
cactus.goto(600, -140)
cactus.speed(2.8)
cactus.showturtle()
cactus.left(90)

#Motion of Cactus and collision

import random
import sys
numruns=0
hp = 3
while numruns < 100:
  cacdist = 0
  position = random.randrange(-140,280,140)
  while cacdist < 2:
 
    cactus.hideturtle()
    cactus.goto(600,position)
    cactus.showturtle()
    cactus.forward(720)
    if gorilla.distance(cactus) < 40:
      print("ouch")
      screen.bgcolor("red")
      time.sleep(0.5)
      screen.bgcolor("wheat")
      time.sleep(0.5)
      screen.bgcolor("red")
      time.sleep(0.5)
      screen.bgcolor("wheat")
      hp -= 1
      if hp == 0:
        print("Harambe")
        sys.exit(1)

    
    cactus.forward(400)
    cacdist += 1
  
  numruns += 1
