import os
from random import shuffle,randint
from guizero import App, Box, Picture,PushButton,Text,warn
from time import sleep
def counter():
    timer.value=int(timer.value)-1     #Make a counter to calcute time
    if int(timer.value)==0:
        result.value="Game over"
        warn("Time out","You've run out of time, next player")
        result.value=""
        num_round.value=int(num_round.value)+1
        set_round()
        timer.value=10                      #Set up limited time 
        
def match_emoji(matched):
    num_round.value=int(num_round.value)+1
    if matched:
        result.value="Correct!"
        if player_now.value=="Player 1":
            num1.value=int(num1.value)+1             #Add score
        elif player_now.value=="Player 2":
            num2.value=int(num2.value)+1
    else:
        result.value="Incorrect!"
    set_round()
def countdown_start():
    start_push.hide()
    timer.repeat(1000,counter)
    for button in buttons:
        button.enable()           
def set_round():
    timer.value=10
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
    if int(num_round.value)%2==0:
        player_now.value="Player 2"
    else:
        player_now.value="Player 1"
    
emojis_dir = "emojis"
emojis = [os.path.join(emojis_dir, f) for f in os.listdir(emojis_dir) if os.path.isfile(os.path.join(emojis_dir, f))]
shuffle(emojis)


# Here is ready to insert the code about the rule-window
rule_win=App(title="Game rules")  #Make a window to introduce game rules
title1_txt=Text(rule_win,text="Emojis game rules")
title2_txt=Text(rule_win,text="2 players-edition")
title2_txt.text_color="red"
title1_txt.text_size=30
title2_txt.text_size=50
rules_box=Box(rule_win,width="fill",height="fill")
rules1_txt=Text(rules_box,text="Two players take it in turns to control.")
rules2_txt=Text(rules_box,text="Scores of each player will be displayed separately")
rules3_txt=Text(rules_box,text="Each one has 10 seconds to look for answer")
rules4_txt=Text(rules_box,text="If you are ready ,then click 'Game Start' ")




app = App("emoji match",height=800,width=600)
player_now=Text(app,text="Player 1")
result=Text(app)
round_box=Box(app)
num_round=Text(round_box,text=1,align="right")
round_txt=Text(round_box,text="round",align="right")
grade_box=Box(app,width="fill")
space1=Text(grade_box,align="right",text="  ")
num1=Text(grade_box,align="right",text=0)
player1=Text(grade_box,align="right",text="Player 2:")
space2=Text(grade_box,align="left",text="  ")
player2=Text(grade_box,align="left",text="Player 1:")
num2=Text(grade_box,align="left",text=0)
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
    button.disable()            #Avoid clicking the button of Starting again
start_push=PushButton(extra_feature,text="Game start",command=countdown_start)   #Make a pushbutton to run countdown


timer.value=10

app.display()
