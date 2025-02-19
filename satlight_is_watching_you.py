import pgzrun
from random import randint
from time import time
WIDTH=800
HEIGHT=600
numsat=10
start_time=0
end_time=0
num=1
the_cast=[]
for i in range(10):
    satellite=Actor("satlight")
    satellite.pos=(randint(50,550),randint(50,550))
    the_cast.append(satellite)
start_time=time()

def draw():
    num=1
    screen.blit("stars",(0,0))
    for the_great_sat in the_cast:
        the_great_sat.draw()
        screen.draw.text(str(num),(the_great_sat.pos[0],the_great_sat.pos[1]+20))
        num+=1
    end_time=time()-start_time
    screen.draw.text(str(round(end_time,1)),(50,50))
def update():
    pass
pgzrun.go()