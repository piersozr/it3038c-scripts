import pygame
from pygame.locals import *
from globals import *
import random


class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((10, 10))
        self.surf.fill((0, 0, 255))
        self.rect = self.surf.get_rect()

        self.pos = vec(((random.random() * WIDTH), 0 - random.randint(0, 1000)))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def respawn(self):
        self.pos = vec(((random.random() * WIDTH), 0 - random.randint(0, 1000)))
        self.vel = vec(0, 0)

    def move(self, platforms):
        self.acc = vec(0, 1)
        self.vel += self.acc

        if self.vel.y > 15:
            self.vel.y = 15

        self.pos += self.vel + 0.05 * (self.acc / 2)
        self.rect.midbottom = self.pos

    def update(self, platforms, player):
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        if self.pos.y > HEIGHT:
            self.respawn()
            return 1
        
        # detect player hit
        hits = pygame.sprite.spritecollide(self, player, False)
        if hits:
            self.respawn()
            return -1

        return 0
