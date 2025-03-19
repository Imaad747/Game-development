import pgzrun
TITLE="Quiz master"
HEIGHT=600
WIDTH=850
thelistofshame=[]
quitter=0
totalquitter=0
timebomb=10
scorepelos=0 
bigbillboard_ad=Rect(0,0,850,100)
timebox=Rect(660,110,170,200)
questionbox=Rect(20,110,630,200)
option1=Rect(20,320,300,120)
option2=Rect(20,450,300,120)
option3=Rect(350,320,300,120)
option4=Rect(350,450,300,120)
skipyoutubead=Rect(660,320,170,250)
def draw():
    screen.fill("Dark Green")
    screen.draw.filled_rect(bigbillboard_ad,"White")
    screen.draw.filled_rect(timebox,"Silver")
    screen.draw.filled_rect(questionbox,"Gold")
    screen.draw.filled_rect(option1,"seagreen")
    screen.draw.filled_rect(option2,"seagreen")
    screen.draw.filled_rect(option3,"seagreen")
    screen.draw.filled_rect(option4,"seagreen")
    screen.draw.filled_rect(skipyoutubead,"yellow")
    le_message=(f"Welcome to quizmaster! The question you are on is {quitter}/{totalquitter}")
    screen.draw.textbox(le_message,bigbillboard_ad,color="Gold")
    screen.draw.textbox(str(timebomb),timebox,color="Black",shadow=(0.5,0.5),scolor="Red")
    screen.draw.textbox("Don't Skip",skipyoutubead,color="Black",shadow=(0.5,0.5),scolor="Red",angle=-90)


def update():
  bigbillboard_ad.x-=2
  if bigbillboard_ad.right<0:
     bigbillboard_ad.x=800

def javascribe():
   global totalquitter
   with open("questions.txt","r") as file:
      for q in file:
         thelistofshame.append(q)
         totalquitter+=1
javascribe()
print(thelistofshame)
pgzrun.go()