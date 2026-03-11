import pgzrun
import random
WIDTH = 500
HEIGHT = 500
def draw ():
    screen.fill ("Black")
    w = 500
    h = 100
    for i in range (25):
     r = random.randint(1,255)
     g = random.randint(1,255)
     b = random.randint(1,255)
     Rectangle = Rect((170,250),(w,h)) 
     Rectangle.center = 250,250
     screen.draw.rect(Rectangle,(r,g,b))
     w = w - 25
     h = h + 25
def update ():
   pass
 
        
pgzrun.go()
