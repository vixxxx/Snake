#! python3
import pygame
import time
import random
#initialisation
pygame.init()
#snake lenght
snakeLenght=1
#levelup action
lvl=False
#pause
paused=True
#fonts
small_font=25
medium_font=50
large_font=80
#snake image
img=pygame.image.load('snake.png')
#direction snake
direction='right'
#window width and height
w=800
h=600
#Frame per second
FPS=15
#block width and height
wb=10
hb=10
#snake width and height
ws=10
hs=10
#colors
black=(0,0,0)
white=(255,255,255)
red=(200,0,0)
green=(0,200,0)
blue=(0,0,200)
bright_red=(255,0,0)
bright_green=(0,255,0)
bright_blue=(0,0,255)
#level
level=1
#clock
clock=pygame.time.Clock()
#create our surface
gameDisplay=pygame.display.set_mode((w,h))
#fill our Frame with a White color
gameDisplay.fill(white)
#update our Frame
pygame.display.update()
#add caption to our Frame
pygame.display.set_caption('Snake v1.0')
#update the entire service
gameExit=False
#speed of the block when going left or right
speed_x=10
speed_y=10
#font
font=pygame.font.SysFont(None,25)
#unpause()
def unpause():
    global paused
    paused=False
#level up function
def levelup():
	global level
	global speed_x
        global FPS
    	global snakeLenght
	global speed_y
	global lvl
	if (snakeLenght-1)%5==0 and lvl==True:
		level=snakeLenght/5+1
		FPS+=1
		#speed_x+=1
		#speed_y+=1
		lvl=False
		
#pause
def pause():
    while paused:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        #gameDisplay.fill(white)
        message("Paused",large_font,w/2,h/2,green)
        button('Resume!',150,450,100,50,green,bright_green,unpause)
        button('Quit!',550,450,100,50,red,bright_red,quit_app)
        pygame.display.update()
        clock.tick(60)
#score
def score(score):
    global level
    text='Score:'+str(score) + ' Level:' + str(level)
    size=gettextsize(text,small_font)
    normal_message(text,small_font,size[0]/2,size[1]/2,black)
#game intro
def game_intro():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        message("Snake Game",large_font,w/2,h/2,green)
        button('GO!',150,450,100,50,green,bright_green,game_loop)
        button('Quit!',550,450,100,50,red,bright_red,quit_app)
        pygame.display.update()
        clock.tick(60)
#get font size
def gettextsize(text,font):
    font=pygame.font.Font(None,font)
    size=font.size(text)
    return size
#message function
def normal_message(text,font,x,y,color):
    size=gettextsize(text,font)
    font = pygame.font.Font(None, font)
    TextSurf=font.render(text,True,color)
    gameDisplay.blit(TextSurf,[x-size[0]/2,y-size[1]/2])
def text_objects(text,font,color):
    TextSurf=font.render(text,True,color)
    return TextSurf,TextSurf.get_rect()
def message(text,font,x,y,color):
        Font=pygame.font.Font('freesansbold.ttf',font)
        TextSurf,TextRect=text_objects(text,Font,color)
        TextRect.center=((x),(y))
        gameDisplay.blit(TextSurf,TextRect)
#snake function to draw
def snake(snakelist,ws,hs):
    if direction=='right':
        head=pygame.transform.rotate(img,270)
    if direction=='left':
        head=pygame.transform.rotate(img,90)
    if direction=='up':
        head=pygame.transform.rotate(img,0)
    if direction=='down':
        head=pygame.transform.rotate(img,180)
    gameDisplay.blit(head,[snakelist[-1][0],snakelist[-1][1]])
    for l in snakelist[:-1]:
        pygame.draw.rect(gameDisplay,green,[l[0],l[1],ws,hs])
#quit app function
def quit_app():
    #quit pygame
    pygame.quit()
    #quit python
    quit()
#button function
def button(msg,x,y,w,h,icol,acol,action=None):
    #mouse position
    mouse=pygame.mouse.get_pos()
    #is the mouse clicked?
    click=pygame.mouse.get_pressed()
    #logic to see if the mouse is clicked inside the button rectangle
    if x+w>mouse[0] >x and y+h>mouse[1]>y:
        pygame.draw.rect(gameDisplay,acol,(x,y,w,h))
        if click[0]==1 and action != None:
            action() #if we pass a function to action
    else:
        pygame.draw.rect(gameDisplay,icol,(x,y,w,h))
    #text in button
    message(msg,20,x+w/2,y+h/2,black)
#game over loop
def gameover():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        message('Game over',small_font,w/2,h/2,black)
        button('Play Again',150,450,100,50,green,bright_green,game_loop)
        button('Quit!',550,450,100,50,red,bright_red,quit_app)
        pygame.display.update()
        clock.tick(60)
def gameover2():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        normal_message('Game over',50,w/2,h/2,red)
        normal_message('Press c to play again or Q to quit',medium_font,w/2,h/2+gettextsize('P',medium_font)[1],red)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    quit_app()
                if event.key==pygame.K_c:
                    game_loop()
def game_loop():
    global direction,lvl
    global snakeLenght
    global FPS
    global ws
    global level
    global paused
    global hs
    #FPS
    FPS=15
    #level
    level=1
    #snake(outside while not difining everytime)
    snakeList=[]
    #snakeLenght
    snakeLenght=1
    #beggining of the first block(head of the snacke)
    lead_x=w/2
    lead_y=h/2
    #so it will move if we hold the key 
    lead_x_change=0
    lead_y_change=0
    #apple x and y round them to be multiple of 10
    apple_x=round(random.randrange(0,w-wb))
    apple_y=round(random.randrange(0,h-hb))
    gameExit=False
    while not gameExit:
            #capture events
        for event in pygame.event.get():
            #quit event
            if event.type==pygame.QUIT:
                quit_app()
            #keydown move block
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    direction='left'
                    lead_x_change =- speed_x
                    lead_y_change=0
                elif event.key==pygame.K_RIGHT:
                    direction='right'
                    lead_x_change =speed_x
                    lead_y_change=0
                elif event.key==pygame.K_UP:
                    direction='up'
                    lead_y_change =-speed_y
                    lead_x_change=0
                elif event.key==pygame.K_DOWN:
                    direction='down'
                    lead_y_change =speed_y
                    lead_x_change=0
                elif event.key==pygame.K_p:
                    paused=True
                    pause()
        #x of the block change (when holding)
        lead_x+=lead_x_change
        lead_y+=lead_y_change
        #logic
        if lead_x+ws>w or lead_x<0 or lead_y+hs>h or lead_y<0:
            gameover2()
        if lead_x>=apple_x and lead_x<=apple_x+wb or lead_x+ws>=apple_x and lead_x+ws<=apple_x+wb:
            if lead_y>=apple_y and lead_y<=apple_y+hb or lead_y+hs>=apple_y and lead_y+hs<=apple_y+hb:
                apple_x=round(random.randrange(0,w-wb))
                apple_y=round(random.randrange(0,h-hb))
                snakeLenght+=1
		lvl=True
		levelup()
        #fill with white
        gameDisplay.fill(white)
        #draw our apple
        pygame.draw.rect(gameDisplay,red,[apple_x,apple_y,wb,hb])
        #gameDisplay.blit(appleimg,[apple_x,apple_y])
        #score
        score(snakeLenght-1)
        
        #snake head
        snakeHead=[]
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        if snakeLenght==2:
            for eachSegment in snakeList[:-1]:
                if eachSegment==snakeHead:
                    gameover2()
        if len(snakeList)>snakeLenght:
            del snakeList[0]
        #if the snake eat herself
        for eachSegment in snakeList[:-1]:
            if eachSegment==snakeHead:
                gameover2()
        #draw snake(Frame,color,x,y,w,h)
        snake(snakeList,ws,hs)
        #update
        pygame.display.update()
        #the frame per second
        clock.tick(FPS)
game_intro()
game_loop()


