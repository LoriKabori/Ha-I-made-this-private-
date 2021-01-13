import pygame
import random
import time
import os

def show_start_screen():
    screen.fill(blue)
    draw_text(screen, "Just... Run Around, I Guess.", 64, Width / 2, Height / 4)
    draw_text(screen, "Use the arrow keys to move", 22, Width / 2, Height / 4)
    draw_text(screen, "Just press any key to start", 18, Width / 2, Height * 3 / 4)
    pygame.display.flip()

    waiting = True
    while waiting:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                print("Don't worry, I'll pay for your therapy bills (I won't).")
                waiting = False

Width = 800
Height = 600
FPS = 30
x = 0
GROUND = Height - 30

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, red)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

PLAYER_ACC = 0.9
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.9
vec = pygame.math.Vector2




red = (130, 14, 4)
black = (0, 0, 0)
blue = (3, 76, 135)

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")



class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "p1_jump.png")).convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center = (Width / 2, Height / 2)
        self.y_speed = 5
        self.radius = 20
        self.rect.centerx = Width / 2
        self.rect.bottom = Height - 10
        self.speedx = 0
        self.sheild = 100
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()

        self.pos = vec(10, GROUND -60)
        self.vel = vec(0, 0)
        self.acc = vec(0,0)


    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_RIGHT]:
            self.acc.x += 0.9
        if keystate[pygame.K_LEFT]:
            self.acc.x += -0.9
        if keystate[pygame.K_UP]:
            self.rect.y += -5
        if keystate[pygame.K_DOWN]:
            self.rect.y += 5
        if self.vel.y == 0 and keystate[pygame.K_SPACE]:
            self.vel.y = -20

        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.rect.right > Width:
            self.rect.left = 0
        if self.rect.left < 0:
            self.rect.right = Width

        if self.pos.y > GROUND:
            self.pos.y = GROUND + 1
            self.vel.y =0

        self.rect.midbottom = self.pos
 

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "images.jfif")).convert()
        self.image.set_colorkey(blue)
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.center = (Width / 2, Height / 2)
        self.x_speed = 5

    def update():
        self.acc = vec(0, PLAYER_GRAV)
        self.rect.x(-5)
        if self.rect.right < 0:
            self.rect.left = Width
            
 class Healthbar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.healthbars = [
            pygame.image.load(os.path.join(img_folder, "Hp5.PNG")).convert(),
            pygame.image.load(os.path.join(img_folder, "Hp4.PNG")).convert(),
            pygame.image.load(os.path.join(img_folder, "Hp3.PNG")).convert(),
            pygame.image.load(os.path.join(img_folder, "Hp2.PNG")).convert(),
            pygame.image.load(os.path.join(img_folder, "Hp1.PNG")).convert(),
            pygame.image.load(os.path.join(img_folder, "Hp0.PNG")).convert()
            ]
        self.healthbar_count = 0

        self.image = self.healthbars[self.healthbar_count]
        self.image = pygame.transform.scale(self.image, (100, 50))
        self.image.set_colorkey(black)

        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10

    def setHealth(self):
        return self.healthbar_count

    def setHealth(self, health):
        if health == 1:
            self.healthbar_count -= 1
            if self.healthbar_count < 0:
                self.healthbar_count = 5

    def update(self):
        self.image = self.healthbars[self.healthbar_count]
        self.image = pygame.transform.scale(self.image, (100, 50))
        self.image.set_colorkey(black)

   


        
       




pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("I have no idea what this is either")

clock = pygame.time.Clock()

bkgr_image = pygame.image.load(os.path.join(img_folder, "3306-4254-6617.jpg")).convert()
background = pygame.transform.scale(bkgr_image, (Width, Height))
background_rect = background.get_rect()

all_sprites = pygame.sprite.Group()
player = Player()
platform = Platform()
all_sprites.add(player)



start = True
running = True
while running:
    if start:
        show_start_screen
        start - False

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    all_sprites.update()

    screen.blit(background, background_rect)
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()




































































#oh wow. you actually scrolled down here
#uh... congrats?
