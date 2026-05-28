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
        self.setheading(-90)
    
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
        self.setheading(-90)

    def hit(self):
        self.health -= 1
        if self.health <= 0:
            to_remove = []
            for block in grid:
                if (block != self) and (self.distance(block) < 35):
                    to_remove.append(block)
            for block in to_remove:
                block.remove()

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
        self.ht()
        if self in self.player.bullets:
            self.player.bullets.remove(self)


class Score(Turtle):
    def __init__(self, player, player_color):
        super().__init__()
        self.player = player
        self.ht()
        self.penup()
        if player_color == "light blue":
            self.goto(-250, 0)
        if player_color == "dark blue":
            self.goto(175, 0)
        self.color(player_color)
        self.speed(0)
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.player.score}", font=("Arial", 15, "normal"))



def update():
    global p1, p2, grid, new_game, start

    if p1.alive == False or p2.alive == False:
        yertle = Turtle()
        yertle.ht()
        yertle.penup()
        yertle.goto(-125, -25)
        yertle.color("red")
        yertle.speed(0)
        yertle.write("You died", font=("Arial", 50, "normal"))
        p1.ht()
        p2.ht()
        for bullet in p2.bullets:
            bullet.ht()
        for block in grid:
            block.ht()
        return

    if new_game:
        start = time.time()
        new_game = False

    if time.time()-start > 2:
        start = time.time()
        screen.tracer(0)
        for block in grid:
            block.forward(20)
        for x in range(-140, 150, 20): #x-axis
            if random.randint(1, 10) > 8:
                grid.append(Bomb(x, 190))
            elif len(grid)%4==0:
                grid.append(Block(x, 190, "pink"))
            elif len(grid)%4==1:
                grid.append(Block(x, 190, "yellow"))
            elif len(grid)%4==2:
                grid.append(Block(x, 190, "light green"))
            elif len(grid)%4==3:
                grid.append(Block(x, 190, "aqua"))
        screen.tracer(1)

    for bullet in p1.bullets:
        bullet.move()
        for block in grid:
            if bullet.distance(block) < 20:
                block.hit()
                if block.health == 0:
                    block.remove()
                    p1.score += 1
                    p1_score_board.refresh()
                bullet.die()

    for bullet in p2.bullets:
        bullet.move()
        for block in grid:
            if bullet.distance(block) < 20:
                block.hit()
                if block.health == 0:
                    block.remove()
                    p2.score += 1
                    p2_score_board.refresh()
                bullet.die()
        
    for block in grid:
        if block.distance(p1) < 20:
            p1.alive = False
        if block.distance(p2) < 20:
            p2.alive = False


    screen.ontimer(update, 120)

### PROGRAM ###
screen = Screen()
screen.bgcolor("purple")
screen.setup(600,600)
screen.listen()
new_game = True

screen.onkey(update, "space")

playing_area()

# "press space to start"
# yertle = Turtle()
# yertle.ht()
# yertle.penup()
# yertle.goto(-149, -25)
# yertle.color("green")
# yertle.speed(0)
# yertle.write("Press 'space' to start", font=("Arial", 25, "normal"))


p1 = Player(-75, -150, "light blue", "light blue", screen, "d", "a", "w", True)
p2 = Player(75, -150, "dark blue", "dark blue", screen, "l", "j", "i", True)
grid = []

p1_score_board = Score(p1, "light blue")
p2_score_board = Score(p2, "dark blue")

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

while p1.alive == True and p2.alive == True:
    screen.tracer(1)
    screen.update()
    screen.exitonclick()