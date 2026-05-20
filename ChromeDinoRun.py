import pgzrun
import random

WIDTH = 500
HEIGHT = 500
groundx = 0 

game = True


dino = Actor ("dino2")
dino.x =90
dino.y = 449
restart = Actor ("retry")
restart.x = 250
restart.y = 250
cactus_images = ["cactus1","cactus2"]
cacti = []
def updateimages ():
   global game
   if game == True:
           
      if dino.image == "dino2":
        dino.image = "dino3"
      elif dino.image == "dino3":
        dino.image = "dino2"
def spawncactus ():
   cactus = Actor (random.choice(cactus_images))
   cactus.x = 500
   cactus.y = 449
   cacti.append(cactus)

def draw ():
    screen.fill ("Black")
    screen.blit ('dinoground.png',(groundx,465))
    dino.draw ()
    if game == True:
      for cactus in cacti:
        cactus.draw()
    else:
       restart.draw () 

def on_key_down(key):
   if key == keys.SPACE and dino.y >= 449:
     dino.y -= 150

def update ():
    global groundx  
    global game
    if game == True:
      groundx = groundx - 5
      if abs(groundx) > 100:
         groundx = 0
      for cactus in cacti:
         cactus.x -= 5 
         if cactus.x < 0:
            cacti.remove (cactus)
         if cactus.colliderect (dino):
            game = False
          


    
    

    if dino.y < 449:
     dino.y += 3

clock.schedule_interval (spawncactus,random.randint (2,5))
clock.schedule_interval (updateimages,0.1)









pgzrun.go()