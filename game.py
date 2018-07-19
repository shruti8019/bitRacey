import pygame 
import time
import random

pygame.init()

crash_sound = pygame.mixer.Sound("crash.wav")
pygame.mixer.music.load("Broadway.mp3")

display_width=800
passed=0
display_height=600
car_width=64
car_height=80


black=(0,0,0)       #Colors are defined in RGB format
white=(255,255,255)
red=(200,0,0)
green =(0,200,0)
bright_red=(255,0,0)
bright_green=(0,255,0)

block_color=(53,115,255)

gameDisplay=pygame.display.set_mode((display_width,display_height))  #height and width of game window
pygame.display.set_caption('A Bit Racey') #Caption of the game 
clock=pygame.time.Clock() #to measure frames per second

carImg=pygame.image.load('car.png')
iconImg=pygame.image.load('mycar.png')
pygame.display.set_icon(iconImg)

pause=False
def things_dodged(count):
    font=pygame.font.SysFont('comisansms',25)
    text=font.render("Dodged: "+str(count),True,black)
    gameDisplay.blit(text,(0,0))

def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])
    
    

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text,font):
    textSurface = font.render(text,True,black)
    return textSurface,textSurface.get_rect()

def message_display(x):
    largeText = pygame.font.SysFont('comisansms',115)
    TextSurf, TextRect = text_objects(x,largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)

    pygame.display.update()
    time.sleep(3)
    game_loop()

def crash():

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    
    largeText = pygame.font.SysFont('comisansms',115)
    TextSurf, TextRect = text_objects("You Crashed",largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        #gameDisplay.fill(white)
        

        button(150,450,100,50,bright_green,green,"Play Again",game_loop)
        button(550,450,100,50,bright_red,red,"Quit",quitgame)
        
        pygame.display.update()
        clock.tick(15)

def button(startx,starty,width,height,color1,color2,text,action=None):
    mouse =pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    

    if startx+width >mouse[0] >startx and starty+height>mouse[1]>starty:
        pygame.draw.rect(gameDisplay,color1,(startx,starty,width,height))
        if click[0]==1 and action !=None:
            action()

    else:
        pygame.draw.rect(gameDisplay,color2,(startx,starty,width,height))

    smallText =pygame.font.SysFont('comisansms',20)
    textSurf, textRect = text_objects(text,smallText)
    textRect.center =( (startx+(width/2)),(starty+(height/2)))
    gameDisplay.blit(textSurf,textRect)
def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pause=False
    pygame.mixer.music.unpause()
    
def paused():
    pygame.mixer.music.pause()
    largeText = pygame.font.SysFont('comisansms',115)
    TextSurf, TextRect = text_objects("Paused",largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        #gameDisplay.fill(white)
        

        button(150,450,100,50,bright_green,green,"Continue",unpause)
        button(550,450,100,50,bright_red,red,"Quit",quitgame)
        
        pygame.display.update()
        clock.tick(15)
        
def game_intro():
    intro =True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont('comisansms',115)
        TextSurf, TextRect = text_objects("A bit racy",largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf,TextRect)

        button(150,450,100,50,bright_green,green,"Go!",game_loop)
        button(550,450,100,50,bright_red,red,"Quit",quitgame)
        
        pygame.display.update()
        clock.tick(15)

def game_loop():
    global pause
    pygame.mixer.Sound.stop(crash_sound)
    pygame.mixer.music.play(-1)
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change=0
    y_change=0

    thing_startx = random.randrange(0,display_width)
    thing_starty = -600
    thing_speed = 3
    thing_width = 100
    thing_height = 100
    passed=0
    
    gameExit=False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change=-5
                elif event.key==pygame.K_RIGHT:
                    x_change=5
                elif event.key==pygame.K_UP:
                    y_change=-5
                elif event.key==pygame.K_DOWN:
                    y_change=5
                elif event.key == pygame.K_p:
                    pause=True
                    paused()

            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0
                if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    y_change=0
                
            
        x += x_change
        y += y_change
    
            
        gameDisplay.fill(white)
        things(thing_startx,thing_starty,thing_width,thing_height,block_color)
        thing_starty += thing_speed
        car(x,y)
        things_dodged(passed)
        
        
        if x<0 or x>display_width - car_width or y<0 or y>display_height - car_height: 
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            passed+=1
            thing_speed += 1
            #thing_width+=(passed*1.2)
            
        if y<thing_starty + thing_height and y+car_height > thing_starty:
             if x > thing_startx and x <thing_startx +thing_width or x + car_width > thing_startx and x+car_width <thing_startx:
                  crash()    

        
        pygame.display.update() #Updates entire surface

        clock.tick(70)  #60 frames per second
                        #if you want fast but smooth,increase the number of frames per second
game_intro()
game_loop()

pygame.quit()
quit()
                                    
