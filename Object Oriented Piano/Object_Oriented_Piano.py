import pygame
pygame.init()#initializes Pygame
pygame.mixer.init()
pygame.display.set_caption("python piano program")#sets the window title
screen = pygame.display.set_mode((1900, 1000))#creates game screen
key = 0
mxpos = 0
mypos = 0
mousePos = (mxpos, mypos) #variable mousePos stores TWO numbers
press = False
keyx = 0
keypos = []
for i in range(11):
    keypos.append(keyx)
    keyx+=100

keyboard_keys = [
    pygame.K_q,
    pygame.K_w,
    pygame.K_e,
    pygame.K_r,
    pygame.K_t,
    pygame.K_y,
    pygame.K_u,
    pygame.K_i,
    pygame.K_o,
    pygame.K_p
]

class panokey:
    def __init__(self, xpos):
        self.xpos = xpos
        #self.keynum
        
    def click(self):
        print("nothing")


    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), (self.xpos, 500, 100, 300))

        pygame.draw.rect(screen, (0, 0, 0), (self.xpos, 500, 100, 300), 2)
    def drawpressed(self):
        pygame.draw.rect(screen, (150,150,150), (self.xpos,500,100,300))

#audio stuff!

keysounds = [
    pygame.mixer.Sound("python-piano/brass1.wav"),
    pygame.mixer.Sound("python-piano/brass2.wav"),
    pygame.mixer.Sound("python-piano/brass3.wav"),
    pygame.mixer.Sound("python-piano/brass4.wav"),
    pygame.mixer.Sound("python-piano/brass5.wav"),
    pygame.mixer.Sound("python-piano/brass6.wav"),
    pygame.mixer.Sound("python-piano/brass7.wav"),
    pygame.mixer.Sound("python-piano/brass-i4.wav"),
    pygame.mixer.Sound("python-piano/brass-i5.wav"),
    pygame.mixer.Sound("python-piano/brass-i6.wav")
]
#this holds onto what key the user has pressed
key = 0

keys = [
    panokey(keypos[0]),
    panokey(keypos[1]),
    panokey(keypos[2]),
    panokey(keypos[3]),
    panokey(keypos[4]),
    panokey(keypos[5]),
    panokey(keypos[6]),
    panokey(keypos[7]),
    panokey(keypos[8]),
    panokey(keypos[9])
]

#gameloop###################################################
while True:
    print(mousePos) #this is just for testing so you can see the mouse coordinates on the screen!
    
    #event queue (bucket that holds stuff that happens in game and passes to one of the sections below)
    event = pygame.event.wait()
    
    #update/timer section---------------------------------------
    #input section----------------------------------------------
   
    if event.type == pygame.QUIT: #close game window
        break
    elif event.type == pygame.MOUSEBUTTONDOWN:
        if mousePos[0] > keypos[0] and mousePos[0] < keypos[1] and mousePos[1] >500:
            key = 1
        elif mousePos[0] > keypos[1] and mousePos[0] < keypos[2] and mousePos[1] >500:
            key = 2
        elif mousePos[0] > keypos[2] and mousePos[0] < keypos[3] and mousePos[1] >500:
            key = 3
        elif mousePos[0] > keypos[3] and mousePos[0] < keypos[4] and mousePos[1] >500:
            key = 4
        elif mousePos[0] > keypos[4] and mousePos[0] < keypos[5] and mousePos[1] >500:
            key = 5
        elif mousePos[0] > keypos[5] and mousePos[0] < keypos[6] and mousePos[1] >500:
            key = 6
        elif mousePos[0] > keypos[6] and mousePos[0] < keypos[7] and mousePos[1] >500:
            key = 7
        elif mousePos[0] > keypos[7] and mousePos[0] < keypos[8] and mousePos[1] >500:
            key = 8
        elif mousePos[0] > keypos[8] and mousePos[0] < keypos[9] and mousePos[1] >500:
            key = 9
        elif mousePos[0] > keypos[9] and mousePos[0] < keypos[10] and mousePos[1] >500:
            key = 10
        #add more keys here!
        else:
            key = 0
    elif event.type == pygame.MOUSEBUTTONUP:
        key = 0
    elif event.type == pygame.KEYDOWN:
        if event.key in keyboard_keys:
            key = keyboard_keys.index(event.key)
    elif event.type == pygame.KEYUP:
        key = 0
    elif event.type == pygame.MOUSEMOTION:
        mousePos = event.pos

    #render section---------------------------------------------

    #the keys 
    for k in keys:
        k.draw()
    #key outlines
    
    #if a key is pressed, highlight in grey and play the sound:
    if key != 0:
        for i in range(10):
            pygame.mixer.Sound.play(keysounds[i])
            keys[i].drawpressed()

    pygame.display.flip() #always needed at the end of every game loop!
    

#end game loop##############################################

pygame.quit()
