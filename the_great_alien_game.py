import pgzrun
import random
TITLE="The Great Alien Clicker Game"
WIDTH=500
HEIGHT=500
alien=Actor("pinkalien")
alien.pos=random.randint(50,450),random.randint(50,450)
message=""
def draw():
    screen.fill("pink")
    alien.draw()
    screen.draw.text(message,(150,0),fontsize=30,color="green")
def on_mouse_down(pos):
    global message 
    if alien.collidepoint(pos):
        alien.pos=random.randint(50,450),random.randint(50,450)
        message="Great shot!"
    else:
        message="You missed! Totally good job!"


pgzrun.go()
