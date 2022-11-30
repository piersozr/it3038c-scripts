import pygame
from pygame.locals import *
from globals import *

class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(WIDTH/2, HEIGHT - 10))

    def move(self, platforms):
        pass

    def update(self, platforms, player):
        return 0