from pygame import *




win_width = 700
win_height = 500
clock = time.Clock()

window = display.set_mode((win_width,win_height))
display.set_caption('galaxy')
background = transform.scale(image.load("enigma.jpg"),(700,500))








































































play = True
while play:
    window.blit(background,(0,0))



    for e in event.get():
        if e.type == QUIT:
            play = False



    clock.tick(60   )
    display.update()