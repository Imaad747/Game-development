import pgzrun
import random
WIDTH=300
HEIGHT=300
def draw():
    screen.fill("Blue")
    w=300
    h=50
    r="Red"
    k="White"
    obj=Rect(0,0,w,h)
    screen.draw.filled_rect(obj,r)
    screen.draw.filled_circle((75,150),35,k)
    screen.draw.filled_circle((225,150),35,k)
    screen.draw.line((85,210),(215,210),k)
    screen.draw.line((65,90),(235,90),k)
    screen.draw.line((0,0),(300,300),"Red")
    screen.draw.line((300,0),(0,300),"Red")
    
pgzrun.go()