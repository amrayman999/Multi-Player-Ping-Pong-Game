#importing turtle module

import turtle

#setup the screen of the game

window=turtle.Screen()            #initialize the screen
window.title("Ping Pong Game")    #writing the title of the game screen
window.bgcolor("black")           #setting the screen colour
window.setup(width=600,height=400)#setting the screen height and width
window.tracer(0)                  #making the screen updated manualy by me

#score
score1=0
score2=0
score=turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,170)
score.write("Player 1 : 0 | Player 2 : 0",align="center",font=("courier",22,"normal"))

#madrab (1)
madrab1=turtle.Turtle()
madrab1.speed(0)
madrab1.shape("square")
madrab1.color("blue")
madrab1.shapesize(stretch_len=1,stretch_wid=5)
madrab1.penup()
madrab1.goto(-280,0)
def madrab1_up():
    y=madrab1.ycor()
    y+=30
    madrab1.sety(y)
def madrab1_down():
    y = madrab1.ycor()
    y -= 30
    madrab1.sety(y)


#madrab (2)
madrab2=turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.shapesize(stretch_len=1,stretch_wid=5)
madrab2.penup()
madrab2.goto(280,0)
def madrab2_up():
    y=madrab2.ycor()
    y+=30
    madrab2.sety(y)
def madrab2_down():
    y = madrab2.ycor()
    y -= 30
    madrab2.sety(y)

#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dy=0.1
ball.dx=0.1
#keyboard bindings
window.listen()
window.onkeypress(madrab1_up,"w")
window.onkeypress(madrab1_down,"s")
window.onkeypress(madrab2_up,"Up")
window.onkeypress(madrab2_down,"Down")
#the main loop of the game

while True:
    window.update()   #updates the screen  every time the loop runs
    #moving the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    #border check
    if ball.ycor() >190:
        ball.sety(190)
        ball.dy*=-1
    if ball.ycor() <-190:
        ball.sety(-190)
        ball.dy*=-1
    if ball.xcor()>290:
        ball.goto(0,0)
        ball.dx*=-1
        score1+=1
        score.clear()
        score.write("Player 1 : {} | Player 2 : {}".format(score1,score2), align="center", font=("courier", 22, "normal"))
    if ball.xcor()<-290:
        ball.goto(0,0)
        ball.dx*=-1
        score2 += 1
        score.clear()
        score.write("Player 1 : {} | Player 2 : {}".format(score1, score2), align="center", font=("courier", 22, "normal"))
    #ball hit the madrab
    if(ball.xcor()>270 and ball.xcor()<280)and(ball.ycor()<madrab2.ycor()+50 and ball.ycor()>madrab2.ycor()-50):
        ball.setx(270)
        ball.dx*=-1
    if (ball.xcor() < -270 and ball.xcor() > -280) and ( ball.ycor() < madrab1.ycor() + 50 and ball.ycor() > madrab1.ycor() - 50):
        ball.setx(-270)
        ball.dx *= -1
