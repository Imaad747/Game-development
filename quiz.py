import pgzrun
TITLE="Quiz master"
HEIGHT=800
WIDTH=800
quitter=0
totalquitter=0
timebomb=10
scorepelos=0
bigbillboard_ad=Rect(0,0,800,80)
def draw():
    screen.fill("honeydew")
    screen.draw.filled_rect(bigbillboard_ad,"darkkhaki")

pgzrun.go()