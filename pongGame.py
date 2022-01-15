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
ball.color("white")
ball.penup()  # turtles draw a line as they move, so we dont need to do it
ball.goto(0, 0)


# Main game loop
while True:
    wn.update()