import pgzrun
import random
WIDTH = 500
HEIGHT = 500
ash = Actor ("ash")
ash.x = 250
ash.y = 250

pikachu = Actor ("pikachu")
pikachu.x = 50
pikachu.y = 200

def draw ():
 screen.blit ("background",(0,0))
 ash.draw ()
 pikachu.draw ()


def update ():
    if keyboard.w: 
     ash.y = ash.y-20

    if keyboard.s:
      ash.y = ash.y+20

    if keyboard.a:
      pikachu.x = pikachu.x-20

    if keyboard.d:
      pikachu.x = pikachu.x+20

    if ash.y < 0:
      ash.y = 50

    if ash.y > 500:
      ash.y = 450
    
    if pikachu.x < 0:
      pikachu.x = 50

    if pikachu.x > 500:
      pikachu.x = 450

      
pgzrun.go()