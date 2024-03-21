import pygame #library for games
import time #time functions
import random #generate random numbers 

pygame.init() #initialize pygame modules
dis_width=700
dis_height=600 #give dimensions of the game window
dis=pygame.display.set_mode((dis_width,dis_height))#set the game window
pygame.display.set_caption('Snake game by Kaoutar')#gives the window a title
#set colors https://www.rapidtables.com/web/color/RGB_Color.html
light_blue=(102,178,255)
blue=(0,0,200)
dark_blue=(0,0,153)
light_green=(204,255,229)
pink=(255,0,127)

clock=pygame.time.Clock() #create a clok object to contol the frame rate of the game
speed=15
snake_block=10
#writing fonts
font_style=pygame.font.SysFont("roboto",20)
score_font=pygame.font.SysFont("roboto",18)
#display the score count
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, pink)
    dis.blit(value, [0, 0])#place the message on the screen
#draw the shapes    
def our_snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.circle(dis,light_blue,(x[0],x[1]),20)
        pygame.draw.circle(dis,dark_blue,(x[0],x[1]),5)
        
def message(msg,color):
    mesg=font_style.render(msg,True,color)
    dis.blit(mesg,[dis_width/6,dis_height/3])
    
def gameloop():
    game_over=True
    game_close=False
    x1=dis_width/2
    y1=dis_height/2

    x1_change=0
    y1_change=0
    
    foodx=round(random.randrange(0,dis_width-snake_block)/10)*10
    foody=round(random.randrange(0,dis_width-snake_block)/10)*10

    snake_list=[]
    Length_of_snake=1
    
    while game_over:
        while game_close==True:
            dis.fill(light_green)
            message('You Lost! Press Q-quit or C-pl',dark_blue) 
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        game_over= False
                        game_close=False
                    if event.key==pygame.K_c:
                        gameloop()
        
        for x in pygame.event.get(): #event.get() returns list of all events
            if x.type==pygame.QUIT:
                game_over=False
            if x.type==pygame.KEYDOWN:
                if x.key==pygame.K_LEFT:
                    x1_change=-snake_block
                    y1_change=0
                elif x.key==pygame.K_RIGHT:
                    x1_change=snake_block
                    y1_change=0
                elif x.key==pygame.K_UP:
                    x1_change=0
                    y1_change=-snake_block
                elif x.key==pygame.K_DOWN:
                    x1_change=0
                    y1_change=snake_block
        if x1>=dis_width or x1<0 or y1>=dis_height or y1<0:
            game_close=True
                    
        x1+=x1_change
        y1+=y1_change
        dis.fill(light_green)
        pygame.draw.rect(dis,blue,[foodx,foody,snake_block,snake_block])
        snake_head=[]
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list)>Length_of_snake:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x==snake_head:
                game_close=True
        
        our_snake(snake_block,snake_list)
        Your_score(Length_of_snake - 1)
        pygame.display.update()
        
        if x1==foodx and y1==foody:
            foodx=round(random.randrange(0,dis_width-snake_block)/10)*10
            foody=round(random.randrange(0,dis_height-snake_block)/10)*10
            Length_of_snake+=1
        clock.tick(speed)

    pygame.quit()#initialize everything
    quit()
gameloop()