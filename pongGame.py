# Pong Game

import turtle

wn = turtle.Screen()  # creating the window
wn.title("Pong by @amithinfini")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)  # to manually update, so the game is fast


# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)  # this is the speed of animation
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()  # turtles draw a line as they move, so we dont need to do it
paddleA.goto(-350, 0)


# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)  # this is the speed of animation
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()  # turtles draw a line as they move, so we dont need to do it
paddleB.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)  # this is the speed of animation
ball.shape("circle")
ball.color("blue")
ball.penup()  # turtles draw a line as they move, so we dont need to do it
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)  # this is the speed of animation
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 20, "normal"))


# Functions
# to move the Paddle A Up
def paddleAUp():
    y = paddleA.ycor()  # gets the y cordinate of Paddle A
    y += 20
    paddleA.sety(y)


# to move PAddle A down
def paddleADwn():
    y = paddleA.ycor()  # gets the y cordinate of Paddle A
    y -= 20
    paddleA.sety(y)


# to move the Paddle B Up
def paddleBUp():
    y = paddleB.ycor()  # gets the y cordinate of Paddle A
    y += 20
    paddleB.sety(y)


# to move PAddle B down
def paddleBDwn():
    y = paddleB.ycor()  # gets the y cordinate of Paddle A
    y -= 20
    paddleB.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddleAUp, "w")
wn.onkeypress(paddleADwn, "s")
wn.onkeypress(paddleBUp, "Up")
wn.onkeypress(paddleBDwn, "Down")


# Main game loop
while True:
    wn.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1

    # Paddle and ball collisions
    if (ball.xcor() > 330 and ball.xcor() < 350) and (ball.ycor() < paddleB.ycor() + 50 and ball.ycor() > paddleB.ycor() - 50):
        ball.setx(330)
        ball.dx *= -1

    if (ball.xcor() < -330 and ball.xcor() > -350) and (ball.ycor() < paddleA.ycor() + 50 and ball.ycor() > paddleA.ycor() - 50):
        ball.setx(-330)
        ball.dx *= -1