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
    def __init__(self, x, y, color, player_color, screen, right_key, left_key, fire_key, is_alive):
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
        self.blocks = []
        self.alive = is_alive
        self.st()
        screen.onkeypress(self.turn_left, left_key)
        screen.onkeypress(self.turn_right, right_key)
        screen.onkeypress(self.fire, fire_key)

    def fire(self):
        if len(self.bullets) < 5:
            self.bullets.append(Bullet(self))

    def turn_left(self):
        self.left(10)

    def turn_right(self):
        self.right(10)

class Block(Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.ht()
        self.speed(0)
        self.penup()
        self.color(color)
        self.shape("square")
        self.st()

    def grid(self):
        for i in range(200, -10, -20): #y-axis
            for j in range(-150, 160, 20): #x-axis
                if len(blocks)%3==0:
                    blocks.append(block(x, y, "pink"))
                elif len(blocks)%3==1:
                    blocks.append(block(x, y, "yellow"))
                elif len(blocks)%3==2:
                    blocks.append(block(x, y, "turquiose"))

# class Bomb(Turtle):
#     def __init__(self, x, y, blocks):
#         super().__init__()
#         self.ht()
#         self.speed(0)
#         self.penup()
#         self.color("black")
#         self.shape("square")
#         self.st()

    # def hit(self):
    #     for i in range(y, y+4): #ex) 6, 10 (stops 1 early)
    #         for j in range(y, y+4):
    #             blocks.remove(blocks(j, x))





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
        if self.xcor() > 140 or self.xcor() < -140:
            self.setheading(180 - self.heading())
        if self.ycor() > 190 or self.ycor() < -190:
            self.setheading(-self.heading())

    def die(self):
        self.ht()
        self.player.bullets.remove(self)


# class Score(Turtle):
#     def __init__(Etc.):
#         super().__init__()





# def update():
#   global p1, p2
#   if player.alive:
#     for i in range(len(body)-1, 0, -1):
#       body[i].move(body[i-1])
#     player.move()   
#     for j in range(3, len(body)):
#       if player.distance(body[j]) < 20:
#         player.die()
#     if player.distance(apple) < 30:
#       apple.relocate()
#       body.append(Segment(body[-1]))
#   else:
#     for k in range(1, len(body)):
#       body[k].ht()
#     apple.ht() 
#     yertle = Turtle()
#     yertle.ht()
#     yertle.penup()
#     yertle.goto(-125, -25)
#     yertle.color("red")
#     yertle.speed(0)
#     yertle.write("You died", font=("Arial", 50, "normal"))

#   screen.ontimer(update, 120)

### PROGRAM ###
screen = Screen()
screen.bgcolor("purple")
screen.setup(600,600)
screen.listen()

screen.onkey(update, "space")

playing_area()

p1 = Player(-75, -150, "light blue", "light blue", screen, "d", "a", "w", True)
p2 = Player(75, -150, "dark blue", "dark blue", screen, "l", "j", "i", True)
blocks = []

# while p1.alive == True and p2.alive == True:
#     screen.update()
    
#     for bullet in p1.bullets:
#         bullet.move()
        
#         for block in blocks:
#             if bullet.distance(block) < 20:
#                 block.ht()
#                 blocks.remove(block)
#                 bullet.ht()
#                 if bullet in p1.bullets:
#                     p1.bullets.remove(bullet)
#                 break


screen.exitonclick()