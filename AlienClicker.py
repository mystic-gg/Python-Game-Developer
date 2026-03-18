import pgzrun
import random
WIDTH = 500
HEIGHT = 500
ufo = Actor("ufo")
ufo.x = 250
ufo.y = 100
score = 0

def draw ():
    screen.fill ("Orange" )
    ufo.draw()
    screen.draw.text(str(score),(400,250))
def on_mouse_down(pos):
    global score 
    #print (pos)
    if ufo.collidepoint(pos):
        ufo.x = random.randint (1,500)
        ufo.y = random.randint (1,500)
        score = score+1
        
        
          
pgzrun.go()


