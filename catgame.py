import pgzrun
from random import randint
WIDTH=1000
HEIGHT=600

goal=Actor("goal-removebg-preview")
goal.pos=randint(50,550),randint(50,450)
ball=Actor("football")
ball.pos=(50,50)
scoor=0
GameOver=False

def draw():
    screen.blit("grassbackground.png",(0,0))
    goal.draw()
    ball.draw()
    screen.draw.text("Score "+str(scoor),color="Black",topleft=(50,50))
    if GameOver:
        screen.fill("Orange")
        screen.draw.text("Gym over :( Time's up!",color="Black",topleft=(100,50))

def update():
    global scoor
    if keyboard.left:
        ball.x-=5
    if keyboard.right:
        ball.x+=5
    if keyboard.up:
        ball.y-=5
    if keyboard.down:
        ball.y+=5
    if ball.colliderect(goal):
        goal.pos=randint(50,550),randint(50,450)
        scoor+=1
def timesup():
    global GameOver
    GameOver=True
clock.schedule(timesup,10)
pgzrun.go()