from turtle import *
import time
import random

def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.color('white')
    pen.begin_fill()
    pen.goto(-150, -200)
    pen.goto(150, -200)
    pen.goto(150, 200)
    pen.goto(-150, 200)
    pen.goto(-150, -200)
    pen.end_fill()

### CLASS and FUNCTION DEFINITIONS ###

class Player(Turtle):
    def __init__(self, x, y, color, player_color, screen, right_key, left_key, fire_key):
        super().__init__()
        self.ht()
        self.speed(0)
        self.color(color)
        self.player_color = color
        self.penup()
        self.goto(x, y)
        self.setheading(90)
        self.shape("turtle")
        self.bullets = []
        self.alive = True
        self.st()
        screen.onkeypress(self.turn_left, left_key)
        screen.onkeypress(self.turn_right, right_key)
        screen.onkeypress(self.fire, fire_key)

    def fire(self):
        if self.bullets < 5:
            self.bullets.append(Bullet(self))

    def turn_left(self):
        self.left(10)

    def turn_right(self):
        self.right(10)

class Block(Turtle):
    def __init__(self, x, y, color):
        super().__init__()
    
    def grid(self):
        for i in range(200, -10, -20): #y-axis
            for j in range(-150, 160, 20): #x-axis
                if len(blocks)%3==0:
                    blocks.append(block(x, y, gray))

# class Bomb(Turtle):
#     def __init__():
#         super().__init__()

class Bullet(Turtle):
    def __init__(self, player):
        super().__init__()
        self.ht()
        self.speed(0)
        self.color(player.player_color)
        self.penup()
        self.goto(player.xcor(), player.ycor())
        self.setheading(player.heading())
        self.shape("triangle")
        self.player = player
        self.st()

    def move(self):
        self.forward(10)
        if self.xcor() > 150: #right
             self.setheading(135)
        if self.xcor() < -150: #left
            self.setheading(45)
        if self.xcor() < -200:
            self.setheading(90)

    def die(self):
        self.ht()
        self.player.bullets.remove(self)


# class Score(Turtle):
#     def __init__(Etc.):
#         super().__init__()







### PROGRAM ###
screen = Screen()
screen.bgcolor("purple")
screen.setup(600,600)
screen.listen()
playing_area()

# p1 =
# p2 =
blocks = []

screen.exitonclick()