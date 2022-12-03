from globals import *
import pygame
from pygame.locals import *

# player class inherits pygame sprite
class Player(pygame.sprite.Sprite):
    # constructor
    def __init__(self):
        # parent constructor
        super().__init__()
        # draws the square
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((200, 200, 0))
        self.rect = self.surf.get_rect()

        self.pos = vec((10, 385))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    # move function
    def move(self, platforms):
        # set gravity
        self.acc = vec(0, 0.5)

        # keyboard moves player
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC
        if pressed_keys[K_SPACE]:
            self.jump(platforms)

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # this wraps the player around but it snaps, not perfect
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos

    # jumps
    def jump(self, platforms):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        # only jump if on the ground otherwise you fly away
        if hits:
            self.vel.y = -15

    # update every frame
    def update(self, platforms, player):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if self.vel.y > 0:
            if hits:
                self.vel.y = 0
                # move player up
                self.pos.y = hits[0].rect.top + 1

        return 0
