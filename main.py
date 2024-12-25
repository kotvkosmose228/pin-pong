from pygame import *




win_width = 700
win_height = 500
clock = time.Clock()

window = display.set_mode((win_width,win_height))
display.set_caption('galaxy')
background = transform.scale(image.load("enigma.jpg"),(700,500))




class GameSprite(sprite.Sprite):
    def __init__(self, s_image, s_speed, s_x, s_y,s_weight=50,s_height=100):
        super().__init__()
        self.image = transform.scale(image.load(s_image),(s_weight,s_height))
        self.speed = s_speed
        self.rect = self.image.get_rect()
        self.rect.x = s_x
        self.rect.y = s_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))










class Player(GameSprite):

    def update_l(self):
        keys = key.get_pressed()
        if keys [K_w] and self.rect.y > .5:
            self.rect.y -= self.speed
        if keys [K_s]:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys [K_UP] and self.rect.y > .5:
            self.rect.y -= self.speed
        if keys [K_DOWN]:
            self.rect.y += self.speed



player1 = Player('black.png',10,0,250)


player2 = Player('black.png',10,640,250)










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


    clock.tick(60)
    display.update()