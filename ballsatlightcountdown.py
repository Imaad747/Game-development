import pgzrun
from random import randint
from time import time
WIDTH=800
HEIGHT=600
GameOver=False
GameWin=False
numsat=10
start_time=0
end_time=0
num=1
nummer=0
timer=0
therunwaylayout=[]
the_cast=[]
for i in range(10):
    satellite=Actor("boingmarbleball")
    satellite.pos=(randint(50,550),randint(50,550))
    the_cast.append(satellite)
start_time=time()

def draw():
    global end_time
    
    num=1
    screen.blit("stars",(0,0))
    for the_great_sat in the_cast:
        the_great_sat.draw()
        screen.draw.text(str(num),(the_great_sat.pos[0],the_great_sat.pos[1]+40))
        num+=1
    if nummer<numsat:

        end_time=time()-start_time
        screen.draw.text(str(round(end_time,1)),(50,50))
    else:
        screen.draw.text(str(round(end_time,1)),(50,50))
    for i in therunwaylayout:
        screen.draw.line(i[0],i[1],"grey")
    if GameOver:
        screen.fill("Orange")
        screen.draw.text("You have entered the void, where strings and floaties swim",color="Black",topleft=(100,50))
    if GameWin:
        screen.fill("Red")
        screen.draw.text("Welcome to the abandoned airport TWA terminal at New York",color="White",topleft=(100,50))        
def timesup():
    global GameOver,GameWin
    if len(therunwaylayout)==9:
        GameWin=True
    else:

       GameOver=True

def update():
    pass
def on_mouse_down(pos):
    global therunwaylayout,nummer
    if nummer<numsat:

        if the_cast[nummer].collidepoint(pos):
            if nummer:
                therunwaylayout.append((the_cast[nummer-1].pos,the_cast[nummer].pos))
            nummer+=1    
        else:
            therunwaylayout=[]
            nummer=0

clock.schedule(timesup,20)
pgzrun.go()