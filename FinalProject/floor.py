import pygame
from pygame.locals import *
from globals import *

# bottom of screen
class floor(pygame.sprite.Sprite):
    # constructor
    def __init__(self):
        # parent constructor
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((0, 110, 0))
        self.rect = self.surf.get_rect(center=(WIDTH/2, HEIGHT - 10))

        self.timerMax = 120
        self.timer = 0

        self.pos = (WIDTH/2, HEIGHT-10)

    # Have to have
    def move(self, platforms):
        pass

    # Have to have
    def update(self, platforms, player):
        self.timer += 1

        if (self.timer >= self.timerMax):
            self.timer = 0
            self.pos -= vec(0, 5)
            self.rect.midbottom = self.pos

        return 0
