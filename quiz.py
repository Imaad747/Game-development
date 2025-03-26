import pgzrun
TITLE="Quiz master"
HEIGHT=600
WIDTH=850
the_void=False
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
the_option_archive=[option1,option2,option3,option4]
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
    screen.draw.textbox(les_questions[0],questionbox,color="White")
    user_id=1
    for i in the_option_archive:
       screen.draw.textbox(les_questions[user_id],i,color="White")
       user_id+=1
def the_end_dimension():
   global the_void,the_final_essay,les_questions,timebomb
   the_void=True
   the_final_essay=(f"Game over :D. You got {scorepelos}/{totalquitter} ")
   les_questions=[the_final_essay,"N/A","N/A","N/A","N/A",1992]
   timebomb=0
def on_mouse_down(pos):
   one=1
   for i in the_option_archive:
      if i.collidepoint(pos):
         if one is int(les_questions[5]):
            namee()
         else:
            the_end_dimension()
      one+=1
      
def diffuse():
   global timebomb
   if timebomb:
      timebomb-=1
   else:
      the_end_dimension()
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
def evilville_castle_of_the_first_fan_made_minecraft_video_lost_media():
   global quitter
   quitter+=1
   return thelistofshame.pop(0).split("|")
javascribe()
les_questions=evilville_castle_of_the_first_fan_made_minecraft_video_lost_media()
print(les_questions)
clock.schedule_interval(diffuse,1)
pgzrun.go()