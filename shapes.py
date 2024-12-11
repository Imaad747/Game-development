import pgzrun
import random
WIDTH=300
HEIGHT=300
def draw():
    screen.fill("Black")
    w=300
    h=50
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    obj=Rect(0,0,w,h)
    screen.draw.filled_rect(obj,(r,g,b))
    screen.draw.filled_circle((150,150),50,(r,g,b))
    screen.draw.line((0,0),(300,300),"Yellow")
    """for i in range(20):
     r=random.randint(0,255)
     g=random.randint(0,255)
     b=random.randint(0,255)
     obj=Rect(0,0,w,h)
     obj.center=150,150
     screen.draw.rect(obj,(r,g,b))
     w-=10
     h+=10"""
pgzrun.go()