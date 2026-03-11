import pgzrun
import random
WIDTH = 500
HEIGHT = 500
def draw ():
    screen.fill ("Black")
    radius = 35
    for i in range (25):
     r = random.randint(1,255)
     g = random.randint(1,255)
     b = random.randint(1,255)
     screen.draw.circle((250,250),radius,(r,g,b))
     radius = radius + 10
     
     
def update ():
   pass
 
        
pgzrun.go()

