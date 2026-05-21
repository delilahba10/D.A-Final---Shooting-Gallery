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
        self.score = 0
        self.alive = is_alive
        self.st()
        self.player_score = 0
        screen.onkeypress(self.turn_left, left_key)
        screen.onkeypress(self.turn_right, right_key)
        screen.onkeypress(self.fire, fire_key)

    def fire(self):
        if len(self.bullets) < 5:
            self.bullets.append(Bullet(self))
            for bullet in self.bullets:
                bullet.move()

    def turn_left(self):
        self.left(5)

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
        self.health = 3
        self.goto(x, y)
        self.st()
    
    def hit(self):
        self.health -= 1
        if self.health == 2:
            self.color("orange")
        if self.health == 1:
            self.color("red")
        if self.health == 0:
            self.remove()

    def remove(self):
        global grid
        if self in grid:
            self.ht()
            grid.remove(self)

class Bomb(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.ht()
        self.speed(0)
        self.penup()
        self.goto(x, y)
        self.color("black")
        self.shape("square")
        self.health = 1
        self.st()

    def hit(self):
        self.health -= 1
        to_remove = []
        for block in grid:
            if (block != self) and (self.distance(block) < 35):
                to_remove.append(block)
        for block in to_remove:
            block.remove()
#for each block the bomb explodes, add 1 to player score, plus the actual bomb
        self.remove()
    
    def remove(self):
        global grid
        if self in grid:
            self.ht()
            grid.remove(self)

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
        if self.ycor() < -190:
            self.setheading(-self.heading())
        if self.ycor() > 190: 
            self.die()

    def die(self):
        if self in self.player.bullets:
            self.ht()
            self.player.bullets.remove(self)


class Score(Turtle):
    def __init__(self, player, player_color):
        super().__init__()
        self.ht()
        self.penup()
        if player_color == "light blue":
            self.goto(300, 0)
        if player_color == "dark blue":
            self.goto(-300, 0)
        self.color(player_color)
        yertle.speed(0)
        yertle.write(f"{str(player_score)}", font=("Arial", 15, "normal"))



def update():
    global p1, p2, grid

    start = time.time()

    if time.time()-start > 2:
        start = time.time()

    for bullet in p1.bullets:
        bullet.move()
        for block in grid:
            if bullet.distance(block) < 20 and block.color != "black":
                block.hit()
                if block.health == 0:
                    block.remove()
                    p1.player_score += 1
                bullet.die()
            if block.color == "black" and bullet.distance(block) < 20:
                block.hit()

    for bullet in p2.bullets:
        bullet.move()
        for block in grid:
            if bullet.distance(block) < 20 and block.color != "black":
                block.hit()
                if block.health == 0:
                    block.remove()
                    p2.player_score += 1
                bullet.die()
            if block.color == "black" and bullet.distance(block) < 20:
                block.hit()

    p1.Score()

    screen.ontimer(update, 120)

### PROGRAM ###
screen = Screen()
screen.bgcolor("purple")
screen.setup(600,600)
screen.listen()

screen.onkey(update, "space")

playing_area()

p1 = Player(-75, -150, "light blue", "light blue", screen, "d", "a", "w", True)
p2 = Player(75, -150, "dark blue", "dark blue", screen, "l", "j", "i", True)
grid = []

screen.tracer(0)

for y in range(190, 140, -20): #y-axis
    for x in range(-140, 150, 20): #x-axis
        if random.randint(1, 10) > 8:
            grid.append(Bomb(x, y))
        elif len(grid)%4==0:
            grid.append(Block(x, y, "pink"))
        elif len(grid)%4==1:
            grid.append(Block(x, y, "yellow"))
        elif len(grid)%4==2:
            grid.append(Block(x, y, "light green"))
        elif len(grid)%4==3:
            grid.append(Block(x, y, "aqua"))


screen.tracer(1)

screen.update()
    
#"press space to start"
# yertle = Turtle()
# yertle.ht()
# yertle.penup()
# yertle.goto(-125, -25)
# yertle.color("green")
# yertle.speed(0)
# yertle.write("Press", font=("Arial", 50, "normal"))


#death

    # yertle = Turtle()
    # yertle.ht()
    # yertle.penup()
    # yertle.goto(-125, -25)
    # yertle.color("red")
    # yertle.speed(0)
    # yertle.write("You died", font=("Arial", 50, "normal"))

screen.exitonclick()