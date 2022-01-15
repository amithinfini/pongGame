
import turtle

wn = turtle.Screen()  # creating the window
wn.title("Pong by @amithinfini")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)  # to manually update, so the game is fast


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
ball.goto(330, 0)


# Main game loop
while True:
    wn.update()