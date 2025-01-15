from pygame import *




win_width = 700
win_height = 500
clock = time.Clock()

window = display.set_mode((win_width,win_height))
display.set_caption('galaxy')
background = transform.scale(image.load("enigma.jpg"),(700,500))




class GameSprite(sprite.Sprite):
    def __init__(self, s_image, s_speed, s_x, s_y,s_weight=50,s_height=150):
        super().__init__()
        self.image = transform.scale(image.load(s_image),(s_weight,s_height))
        self.speed_x = s_speed
        self.speed_y = s_speed
        self.rect = Rect(s_x,s_y,s_weight-30,s_height-70)
        self.rect.x = s_x
        self.rect.y = s_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class Ball(GameSprite):
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y -= self.speed_y
        if self.rect.y < 0:
            self.speed_y *= -1
        if self.rect.y > 400:
            self.speed_y *= -1
        if self.rect.colliderect(player1.rect):
            self.speed_x *= -1
        if self.rect.colliderect(player2.rect):
            self.speed_x *= -1
        

        
        





class Player(GameSprite):

    def update_l(self):
        keys = key.get_pressed()
        if keys [K_w] and self.rect.y > .5:
            self.rect.y -= self.speed_y
        if keys [K_s]:
            self.rect.y += self.speed_y

    def update_r(self):
        keys = key.get_pressed()
        if keys [K_UP] and self.rect.y > .5:
            self.rect.y -= self.speed_y
        if keys [K_DOWN]:
            self.rect.y += self.speed_y



player1 = Player('black.png',5,0,250)

miacik = Ball('ball.png',3,350,250,100,100)

player2 = Player('black.png',5,640,250)











play = True
while play:
    window.blit(background,(0,0))



    for e in event.get():
        if e.type == QUIT:
            play = False

    player1.update_l()
    player1.reset()
    player2.update_r()
    player2.reset()
    miacik.update()
    miacik.reset()

    clock.tick(60)
    display.update()
