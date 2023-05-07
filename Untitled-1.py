from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x                                                      
        self.rect.y = player_y
        


    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y))    

class Player(GameSprite):
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= 10

        if keys_pressed[K_DOWN] and self.rect.y < 460:
            self.rect.y += 10

    def update_l(self):
        if keys_pressed[K_RIGHT] and self.rect.x < 600:
            self.rect.x += 10

        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= 10

       


back = (200, 255, 255)
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

racket1 = Player('hero.png', 100, 289, 80, 200)
racket2 = Player('hero.png', 100, 220, 190, 70)
ball = GameSprite('cyborg.png', 255, 80, 70, 210)

clock = time.Clock()
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    racket1.reset()
    racket2.reset()
    ball.reset()






    display.update()       
    clock.tick(60)
