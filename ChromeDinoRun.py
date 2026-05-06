import pgzrun
WIDTH = 500
HEIGHT = 500
groundx = 0 

def draw ():
    screen.fill ("Black")
    screen.blit ('dinoground.png',(groundx,465))

def update ():
    global groundx
    groundx = groundx - 5
    if abs(groundx) > 100:
        groundx = 0













pgzrun.go()