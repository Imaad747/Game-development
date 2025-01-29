import pgzrun
from random import randint
WIDTH=600
HEIGHT=500

flower=Actor("flower")
flower.pos=randint(50,550),randint(50,450)
bee=Actor("bee")
bee.pos=(50,50)
scoor=0
GameOver=False

def draw():
    screen.blit("beebackground",(0,0))
    flower.draw()
    bee.draw()
    screen.draw.text("Score "+str(scoor),color="Black",topleft=(50,50))
    if GameOver:
        screen.fill("Orange")
        screen.draw.text("Gym over :( Time's up!",color="Black",topleft=(100,50))

def update():
    global scoor
    if keyboard.left:
        bee.x-=5
    if keyboard.right:
        bee.x+=5
    if keyboard.up:
        bee.y-=5
    if keyboard.down:
        bee.y+=5
    if bee.colliderect(flower):
        flower.pos=randint(50,550),randint(50,450)
        scoor+=1
def timesup():
    global GameOver
    GameOver=True
clock.schedule(timesup,10)
pgzrun.go()