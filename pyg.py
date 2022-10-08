import pygame
from pathlib import Path
import os

pygame.init()

width = 800
height = int(width*0.8)

scre = pygame.display.set_mode((width, height))
pygame.display.set_caption('shooter')
clock = pygame.time.Clock()
FPS = 60
GRAVITY = 0.75

bullet = pygame.image.load('img/other/bullet.png').convert_alpha()
moving_left = False
moving_right = False
up = False
bg = (5, 6, 42)
white = (250, 240, 230)


def draw_bg():
    scre.fill(bg)
    pygame.draw.line(scre, white, (0, 300), (width, 300))


class charac(pygame.sprite.Sprite):

    def __init__(self, char_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.char_type = char_type
        self.speed = speed
        self.direction = 1
        self.vel_y = 0
        self.air = True
        self.jump = False
        self.flip = False
        self.list = []
        self.index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        # loading all images for animations
        anime_types = ['idel', 'run', 'jump']
        for anime in anime_types:
            # reset temporary list of images
            tem_list = []
            num_frame = len(os.listdir(f'img/{self.char_type}/{anime}'))
            for a in range(1, num_frame):
                img = pygame.image.load(
                    f'img/{self.char_type}/{anime}/{a}.png').convert_alpha()
                img = pygame.transform.scale(
                    img, (img.get_width()*scale, img.get_height()*scale))
                tem_list.append(img)
            self.list.append(tem_list)
            tem_list = []

        self.image = self.list[self.action][self.index]
        self.rec = self.image.get_rect()
        self.rec.center = (x, y)

    def move(self, moving_left, moving_right, up):
        dx = 0
        dy = 0

        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1

        if moving_right:
            dx = +self.speed
            self.flip = False
            self.direction = 1

        if self.jump and self.air != True:
            self.vel_y = -11
            self.jump = False
            self.air = True
# add gravity
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y
        dy += self.vel_y
# collision with floor
        if self.rec.bottom + dy > 300:
            dy = 300 - self.rec.bottom
            self.air = False

        self.rec.x += dx
        self.rec.y += dy

    def update_anime(self):
        # update the animation
        COOL_DOWN = 100
        # update image base on current frame
        self.image = self.list[self.action][self.index]
        if pygame.time.get_ticks() - self.update_time > COOL_DOWN:
            self.update_time = pygame.time.get_ticks()
            self.index += 1
        if self.index >= len(self.list[self.action]):
            self.index = 0

    def update_action(self, new):
        if new != self.action:
            self.action = new
            self.index = 0
            self.update_time = pygame.time.get_ticks()

    def draw(self):
        scre.blit(pygame.transform.flip(
            self.image, self.flip, False), self.rec)

    def form(self):
        return charac.draw(self), charac.update_anime(self), charac.move(self, moving_left, moving_right, up)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.img = bullet
        self.rec = self.img.get_rect()
        self.rec.center = (x, y)
        self.direction = direction


bullet_group = pygame.sprite.Group()

player = charac("biker", 200, 200, 1.5, 5)
enemy = charac("punk", 434, 200, 1.5, 5)


run = True
while run:

    clock.tick(FPS)

    draw_bg()
    # gernade.draw()
    # player.draw()
    # player.update_anime()
    # player.move(moving_left, moving_right, up)
    player.form()
    enemy.draw()
    enemy.update_anime()
    # update and draw group
    bullet_group.update()
    bullet_group.draw(scre)

    # update player action
    if player.alive:
        if player.air:
            player.update_action(2)  # 2 = jump
        elif moving_left or moving_right:
            player.update_action(1)  # 1 = run
        else:
            player.update_action(0)  # 0 = idel

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    # keyboard
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    moving_left = True

                if event.key == pygame.K_d:
                    moving_right = True

                if event.key == pygame.K_SPACE:
                    shoot = True

                if event.key == pygame.K_w and player.alive:
                    player.jump = True

                if event.key == pygame.K_ESCAPE:
                    run = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    moving_left = False

                if event.key == pygame.K_d:
                    moving_right = False

                if event.key == pygame.K_w:
                    up = False

    pygame.display.update()

pygame.quit()

# visit  http://codingwithruss.com/pygame/shooter/player.html
# http://codingwithruss.com/pygame/shooter/levels.html
