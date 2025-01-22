import pgzrun
import random
import time
TITLE="The Great Amazing Chocolate Clicker Game"
WIDTH=1000
HEIGHT=500
choc=Actor("chocolate")
choc.pos=random.randint(50,450),random.randint(50,450)
message=""
def draw():
    screen.fill("white")
    choc.draw()
    screen.draw.text(message,(150,0),fontsize=30,color="green")
def on_mouse_down(pos):
    global message 
    if choc.collidepoint(pos):
        
        message="Great shot!"
    else:
        message="You missed! GoOd trY!"

def update():
    choc.pos=random.randint(50,450),random.randint(50,450)
    time.sleep(2)
pgzrun.go()
