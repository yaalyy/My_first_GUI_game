import os
from random import shuffle,randint
from guizero import App, Box, Picture,PushButton,Text,warn
from time import sleep
def counter():
    timer.value=int(timer.value)-1     #Make a counter to calcute time
    if int(timer.value)==0:
        result.value="Game over"
        warn("Time out","You've run out of time")
        result.value=""
        set_round()
        timer.value=15                       #Set up limited time 
        num_round.value=int(num_round.value)+1
def match_emoji(matched):
    num_round.value=int(num_round.value)+1   #Add a correct answer in many choices
    if matched:
        result.value="Correct!"
        num_win.value=int(num_win.value)+1
    else:
        result.value="Incorrect!"
    set_round()
def countdown_start():
    timer.repeat(1000,counter)
    start_push.hide()
    for button in buttons:
        button.enable()
def set_round():
    timer.value=15
    for picture in pictures:
        picture.image = emojis.pop()      #Make emojis
    for button in buttons:
        button.image = emojis.pop()
        button.update_command(match_emoji,[False])
    matched_emoji=emojis.pop()
    random_picture=randint(0,15)
    random_button=randint(0,15)
    pictures[random_picture].image=matched_emoji
    buttons[random_button].image=matched_emoji
    buttons[random_button].update_command(match_emoji,[True])
    
emojis_dir = "emojis"
emojis = [os.path.join(emojis_dir, f) for f in os.listdir(emojis_dir) if os.path.isfile(os.path.join(emojis_dir, f))]
shuffle(emojis)

app = App("emoji match",height=800,width=600)
result=Text(app)
round_box=Box(app)
num_round=Text(round_box,text=1,align="right")
round_txt=Text(round_box,text="round",align="right")
grade_box=Box(app)
num_win=Text(grade_box,align="right",text=0)
grade_txt=Text(grade_box,align="right",text="Win:")
game_box=Box(app)
pictures_box = Box(game_box, layout="grid")
buttons_box=Box(game_box,layout="grid")
pictures = []
buttons=[]


for x in range(0,4):
    for y in range(0,4):
        picture = Picture(pictures_box, grid=[x,y])
        pictures.append(picture)
        button=PushButton(buttons_box,grid=[x,y])             #Make grids for emojis
        buttons.append(button)

extra_feature=Box(app)
timer=Text(extra_feature,text="Get ready")
set_round()
for button in buttons:
    button.disable()
start_push=PushButton(extra_feature,text="Game start",command=countdown_start)

timer.value=15
app.display()