import pygame
from pygame.locals import *
from constants import *


class Player(pygame.sprite.Sprite):

    def __init__(self):
        #call parent constructor
        super().__init__()
        #create player sprite image
        self.image = pygame.image.load(player_sprite)
        self.rect = self.image.get_rect()
        self.onGround = False
        self.dx = 0
        self.dy = 0

    def jump(self):
        pass

    def handle_input(self, platforms):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            if self.onGround:
                self.dy -= 16

        if key[pygame.K_DOWN]:
            pass
        if key[pygame.K_LEFT]:
            self.dx = -8

        if key[pygame.K_RIGHT]:
            self.dx = 8

        if not self.onGround:
            self.dy += 0.5
        if not(key[pygame.K_LEFT] or key[pygame.K_RIGHT]):
            self.dx = 0

        self.rect.left += self.dx
        #collision for x axis
        self.collide(self.dx, 0, platforms)
        self.rect.top += self.dy
        self.onGround = False
        #collision for y axis
        self.collide(0, self.dy, platforms)


    def gravity(self):
        pass

    def collide(self, dx, dy, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if dx > 0:
                    #colliding on the right
                    self.rect.right = p.rect.left
                if dx < 0:
                    self.rect.left = p.rect.right
                    #colliding on the left
                if dy > 0:
                    #you are on the ground
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.dy = 0
                if dy < 0:
                    self.rect.top = p.rect.bottom
                    self.dy += 2

    #draws player sprite to screen
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))


    #handles the player input
    # def handle_input(self):
    #     key = pygame.key.get_pressed()
    #     dist = player_speed
    #     if key[pygame.K_DOWN]:
    #         self.rect.y += dist
    #     if key[pygame.K_UP]:
    #         self.rect.y -= dist
    #     if key[pygame.K_RIGHT]:
    #         self.rect.x += dist
    #     if key[pygame.K_LEFT]:
    #         self.rect.x -= dist

