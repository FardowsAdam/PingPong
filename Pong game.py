"""
this program is to create PingPong game
"""
import turtle

'''
initializations
'''
#iniatilze the important function in the screen
screen=turtle.Screen()
screen.title("Ping Pong game")
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.tracer(0)
#iniatlize the first racket
fr=turtle.Turtle()
fr.speed(0)
fr.shape("square")
fr.color("blue")
fr.shapesize(stretch_wid=5,stretch_len=1)
fr.penup()
fr.goto(-350,0)
#iniatlize the second racket
sr=turtle.Turtle()
sr.speed(0)
sr.shape("square")
sr.color("red")
sr.shapesize(stretch_wid=5,stretch_len=1)
sr.penup()
sr.goto(350,0)
#initialize the ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.dx=0.1
ball.dy=0.1
score1=0
score2=0
score=turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("First Player : 0  Second Player: 0 ", align="center",font=("Courier",24,"normal"))
'''
functions
'''
#function to move the first rocket up
def fr_up():
    y=fr.ycor() # to know where the rocket is right now
    y+=20 # add a 20 pixels to its y coordinate
    fr.sety(y) # set the new value as the y cor to the first rocket
#function to move the first rocket down
def fr_down():
    y=fr.ycor() # to know where the rocket is right now
    y-=20 # add a 20 pixels to its y coordinate
    fr.sety(y) # set the new value as the y cor to the first rocket
#function to move the second rocket up
def sr_up():
    y=sr.ycor() # to know where the rocket is right now
    y+=20 # add a 20 pixels to its y coordinate
    sr.sety(y) # set the new value as the y cor to the second rocket
#function to move the second rocket down
def sr_down():
    y=sr.ycor() # to know where the rocket is right now
    y-=20 # add a 20 pixels to its y coordinate
    sr.sety(y) # set the new value as the y cor to the second rocket


# keyboard binding
screen.listen() # the screen to expect that the keyboard will be  used
screen.onkeypress(fr_up,"w") # everytime the w letter is pressed, the func fr_up will work
screen.onkeypress(fr_down,"s")# everytime the s letter is pressed, the func fr_down  will work
screen.onkeypress(sr_up,"Right")# everytime the i letter is pressed, the func sr_up  will work
screen.onkeypress(sr_down,"Left")# everytime the k letter is pressed, the func sr_down  will work

#loop to control the speed manually

while True:
    screen.update()
    # move the ball
    ball.setx(ball.xcor()+ball.dx)# ball starts at 0 and everytime loops run -->+2.5
    ball.sety(ball.ycor() + ball.dy)# ball starts at 0 and everytime loops run -->+2.5
    # border check, to rebound when it touches the bouderies
    if ball.ycor()>290 :# becuase its 20 pixels
        ball.sety(290)
        ball.dy*=-1
    if ball.ycor() <-290:  # becuase its 20 pixels
        ball.sety(-290)
        ball.dy *= -1
     # to put the ball again in the middle
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score1+= 1
        score.clear()
        score.write(" First Player : {} Second Player : {} ".format(score1, score2), align="center",
                    font=("Courier", 24, "normal"))
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        score2 += 1
        score.clear()
        score.write(" First Player : {} Second Player : {} ".format(score1, score2), align="center",
                    font=("Courier", 24, "normal"))
    #collusion between the ball and the racket
    if (ball.xcor()>340 and ball.xcor()<350) and ball.ycor()<sr.ycor()+40 and ball.ycor()>sr.ycor()-40:
      ball.setx(340)
      ball.dx*=-1
    if (ball.xcor()<-340 and ball.xcor()>-350) and ball.ycor()<fr.ycor()+40 and ball.ycor()>fr.ycor()-40:
      ball.setx(-340)
      ball.dx*=-1