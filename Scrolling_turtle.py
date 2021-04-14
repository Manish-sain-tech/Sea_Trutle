import random 
import pygame
'''
In this perticular scrolling game I pick sea theme in which i take three charcter
turtle(which is main player who scroll up and down using up and down arrow respectively)
red_harm_crabe(harm) and green_benifit_fish(benifit)
if turtle tuch(eat) green_benifit_fish score will increse by 5 and
if touch red_harm_crabe he lose his lives by one.
In this game i take a common word for both character(green_benifit_fish and red_harm_crabe) that is food(food_width,food_hight and food_vel).
Here the speed of red_harm_crabe is greater than green_benifit_fish we can change it in the move member function of food (food_vel+...).'''
#initilizing pygame
pygame.init()
##########################################

display_width=500
display_height=500
#initializing display winndow(win) 
win =pygame.display.set_mode((display_width,display_height))

#fonts for text message to display on game window
font=pygame.font.SysFont('chiller',30)
font1=pygame.font.SysFont('chiller',80)
#game title
pygame.display.set_caption("Scrolling_turtle")

#score and lives
score=0
lives=3
#music

music=pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)#For continue playing the music
#background & turtle
bg=pygame.transform.scale((pygame.image.load('backround.png')),(display_width,display_height))

#to fix fps (game run on same speed on any device)
clock=pygame.time.Clock()

#flag to check lost
lost=False
lost_count=0
#to run the main loop
run=True
fps=30
#######################################################
class turtle:
    '''Class for turtle charecter'''
    def __init__(self,turtle_width,turtle_height,turtle_vel,x,y):
        
        '''To initialize the turtle atribute'''
        self.turtle_width=turtle_width
        self.turtle_height=turtle_height
        self.x=x
        self.y=y
        self.turtle_vel=turtle_vel
        self.turtle=pygame.transform.scale((pygame.image.load('turtle.png')),(self.turtle_width,self.turtle_height))

       #flags for key up and down
        self.up=False
        self.down=False
    def draw(self,win):
        '''To draw the turtle charecter'''
        if self.up or self.down :
            win.blit(self.turtle,(self.x,self.y))
        else:
            win.blit(self.turtle,(self.x,self.y))
class food:
    '''Class for food '''
    def __init__(self,food_width,food_hight,food_vel):
        '''Initialize food atribute and charcters'''
        self.food_width=food_width
        self.food_hight=food_hight
        self.food_vel=food_vel
       #food png
        self.red_harm_crabe=pygame.transform.scale((pygame.image.load('red_harm_crabe.png')),(self.food_width,self.food_hight))
        self.green_benifit_fish=pygame.transform.scale((pygame.image.load('green_benifit_fish.png')),(self.food_width,self.food_hight))
        # harm charcter (collision of red_harm_crabe(harm) decrease lives
        
        self.y_red_harm_crabe=random.randint(food_width,500)-food_width
        self.x_red_harm_crabe=random.randint(550,560)
        # benifit (collision of green_benifit_fish(benifit) increase score
        self.y_green_benifit_fish=random.randint(food_width,330)-food_width
        self.x_green_benifit_fish=random.randint(580,590)
       
    def draw(self,win):
        '''To draw the food charecter'''
        self.move()
        win.blit(self.red_harm_crabe,(self.x_red_harm_crabe,self.y_red_harm_crabe))#display red_harm_crabe
    
        win.blit(self.green_benifit_fish,(self.x_green_benifit_fish,self.y_green_benifit_fish))#display green_benifit_fish
    def move(self):
        '''Function to move the food'''
        # motion of foods       
        #for right to left motion of red_harm_crabe(decresing x cordinate)     
        if self.x_red_harm_crabe>-(self.food_width+20):
            self.x_red_harm_crabe-=self.food_vel+3
        else:
            self.y_red_harm_crabe=random.randint(self.food_width,500)-self.food_width
            self.x_red_harm_crabe=random.randint(550,560)

        #for right to left motion of green_benifit_fish(decresing x cordinate)     

        if self.x_green_benifit_fish>-(self.food_width+20):
            self.x_green_benifit_fish-=self.food_vel+2

        else:
            self.y_green_benifit_fish=random.randint(self.food_width,330)-self.food_width
            self.x_green_benifit_fish=random.randint(580,590)
        


#
def redrawGameWindow():
    '''function to display charcters and update display'''
    win.blit(bg,(0,0))#display background
    if not lost:
        tur.draw(win)
        foo.draw(win)
    #for continue displaying lives and score
    score_label=font.render(f"score:{score}",1,(0,0,0))
    lives_label=font.render(f"lives:{lives}",1,(0,0,0))

    win.blit(score_label,(display_width-score_label.get_width()-60,0))
    
    win.blit(lives_label,(lives_label.get_width()-20,0))
    if lost:
       game_label=font1.render("Game Over ",1,(255,0,0))#display game over when lives are equal to 0
       win.blit(game_label,((display_width//2)-100,(display_height//2)-game_label.get_height()))
    #refreshing the window
    pygame.display.update()

#####################################################
tur=turtle(80,70,4,0,230)#object of turtle class
foo=food(90,70,0)#object of food class

#main loop

def main():
    '''Main function to run game.'''
    global run
    global lives
    global score
    global lost
    global lost_count
    while run:
        #fixing on 60 fps
        clock.tick(fps)
        
        redrawGameWindow()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        #tocheck lives is >0 for continuing game          
        if lives<=0:

                lost=True
                lost_count+=1
        if lost:
           if lost_count>fps*3:
              run=False
           else:
               continue

            
        ######################################################    
        #collision
        if tur.x-foo.food_width<foo.x_green_benifit_fish<tur.x+tur.turtle_width and tur.y-foo.food_hight<foo.y_green_benifit_fish<tur.y+foo.food_hight:
            score+=5#increse score by 5 if green_benifit_fish(benifit) collide with turtle
            #if collide then render them at a random position at right side of display window
            foo.y_green_benifit_fish=random.randint(foo.food_width,330)-foo.food_width
            foo.x_green_benifit_fish=random.randint(580,590)

        if tur.x-foo.food_width<foo.x_red_harm_crabe<tur.x+tur.turtle_width and tur.y-foo.food_hight<foo.y_red_harm_crabe<tur.y+foo.food_hight:
            lives-=1#lose 1 lives if turtle collide with red_harm_crabe(harm)
            #if collide then render them at a random position at right side of display window
            foo.y_red_harm_crabe=random.randint(foo.food_width,500)-foo.food_width
            foo.x_red_harm_crabe=random.randint(550,560)


        ################################################################        
        # keys
        keys=pygame.key.get_pressed()#for key press

        # up arrow for moving up     
        if keys[pygame.K_UP] and tur.y>0:
            tur.y-=tur.turtle_vel
            tur.up=True
            tur.down=False

        # down arrow for moving down  
        elif keys[pygame.K_DOWN] and tur.y<display_height-tur.turtle_height:
            tur.y+=tur.turtle_vel

            tur.down=True
            tur.up=False

        else:
            tur.up=False
            tur.down=False



    pygame.quit()

main()        
