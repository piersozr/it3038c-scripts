import pygame
from pygame.locals import *
from globals import *
import random

# falling obstacle
class Obstacle(pygame.sprite.Sprite):
    # constructor
    def __init__(self):
        # parent constructor
        super().__init__()
        # draws the square
        self.surf = pygame.Surface((10, 10))
        self.surf.fill((int(255 * random.random()), 0, int(255 * random.random())))
        self.rect = self.surf.get_rect()

        # move starting placement randomly but still on screen
        self.pos = vec(((random.random() * WIDTH), 0 - random.randint(0, 1000)))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        self.speed = 0.05
        self.maxFallSpeed = 15

    # just move to above screen
    def respawn(self):
        self.pos = vec(((random.random() * WIDTH),
                       0 - random.randint(0, 1000)))
        self.vel = vec(0, 0)
        
        # Make them faster until you lose!
        self.maxFallSpeed += 0.1

    # falls
    def move(self, platforms):
        self.acc = vec(0, 1)
        self.vel += self.acc

        if self.vel.y > self.maxFallSpeed:
            self.vel.y = self.maxFallSpeed

        self.pos += self.vel + self.speed * (self.acc / 2)
        self.rect.midbottom = self.pos

    def update(self, platforms, player):
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        # off screen move back up
        if self.pos.y > HEIGHT:
            self.respawn()
            return 1

        # detect player hit
        hits = pygame.sprite.spritecollide(self, player, False)
        if hits:
            self.respawn()
            # kill player
            return -1

        return 0
