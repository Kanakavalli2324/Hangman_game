import pygame
import math
import random

pygame.init()
W,H=800,500
win=pygame.display.set_mode((W,H))
pygame.display.set_caption("It's a hangman game!!")
 
r=20
g=15
FPS=60
clock=pygame.time.Clock()
run=True
img=[]
words=["DISPLAY","IDE","PYTHON","HANGMAN","HANGING","CAT","DOG","KITTEN","CAR","SCOOTER","OPPOSE","AGAINST","MELANCHOLIA"]
actual_word=random.choice(words)
guessed=[]
for i in range(7):
    img.append(pygame.image.load("hangman"+str(i)+".png"))

#buttons
A=65
l=[]
startx=round((W-((g+r*2)*13))/2)
starty=400
for i in range(26):
    x=startx+g*2+((r*2+g)*(i%13))
    y=starty+((r*2+g)*(i//13))
    l.append([x,y,chr(A+i),True])
col=(195,234,116)
bla=(0,0,0)
#font
l_f=pygame.font.SysFont('comicsans',35)
w_f=pygame.font.SysFont('comicsans',45)
t_f=pygame.font.SysFont('comicsans',55)
h_s=0
def draw():
    win.fill(col)
    t=t_f.render("Hangman Game!!",1,bla)
    win.blit(t,(W/2-t.get_width()/2,10))
    dis_word=""
    for le in actual_word:
        if le in guessed:
            dis_word+=le+' '
        else:
            dis_word+="_ "
    c=w_f.render(dis_word,1,bla)
    win.blit(c,(350,200))
    for le in l:
        x,y,ltr,vis=le
        if(vis):
            pygame.draw.circle(win,bla,(x,y),r,3)
            text=l_f.render(ltr,1,bla)
            win.blit(text,(x-text.get_width()/2,y-text.get_height()/2))
    
    win.blit(img[h_s],(60,120))
    pygame.display.update()
def dis_msg(msg):
    pygame.time.delay(1000)
    win.fill(col)
    t=w_f.render(msg,1,bla)
    win.blit(t,(W/2-t.get_width()/2,H/2-t.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)


while run:
    clock.tick(FPS)
    

    for e in pygame.event.get():
        if(e.type==pygame.QUIT):
            run=False
        if(e.type==pygame.MOUSEBUTTONDOWN):
            m_x,m_y=pygame.mouse.get_pos()
            for le in l:
                x,y,ltr,vis=le
                if(vis):
                    dis= math.sqrt(((x-m_x)**2)+((y-m_y)**2))
                    if(dis < r):
                        le[3]=False
                        guessed.append(ltr)
                        if(ltr not in actual_word):
                            h_s+=1
    draw()
    won=True
    for i in actual_word:
        if i not in guessed:
            won=False
            break
    if won:
        dis_msg("YOU WON!!!")
        break
    if(h_s==6):
        dis_msg("YOU LOST!!!")
        break
    
pygame.QUIT
