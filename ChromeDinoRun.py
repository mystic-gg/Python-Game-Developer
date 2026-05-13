import pgzrun
import random

WIDTH = 500
HEIGHT = 500
groundx = 0 

dino = Actor ("dino")
dino.x =90
dino.y = 452
cactus_images = ["cactus1","cactus2"]
cacti = []
def spawncactus ():
   cactus = Actor (random.choice(cactus_images))
   cactus.x = 500
   cactus.y = 452
   cacti.append(cactus)

def draw ():
    screen.fill ("Black")
    screen.blit ('dinoground.png',(groundx,465))
    dino.draw ()
    for cactus in cacti:
       cactus.draw()
def on_key_down(key):
   if key == keys.SPACE and dino.y >= 452:
     dino.y -= 150

def update ():
    global groundx
    groundx = groundx - 5
    if abs(groundx) > 100:
        groundx = 0
    for cactus in cacti:
       cactus.x -= 5 
       if cactus.x < 0:
          cacti.remove (cactus)
    
    

    if dino.y < 452:
     dino.y += 5

clock.schedule_interval (spawncactus,random.randint (2,5))










pgzrun.go()