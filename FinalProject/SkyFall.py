import pygame
from pygame.locals import *
import sys
from globals import *
from player import *
from platform import *
from obstacle import *

pygame.init()

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Game")
pygame.font.init()
pyFont = pygame.font.SysFont('Lucida Console', 14)

PT1 = platform()
P1 = Player()
SCORE = 0

OB1 = Obstacle()
OB2 = Obstacle()
OB3 = Obstacle()
OB4 = Obstacle()
OB5 = Obstacle()

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)
all_sprites.add(OB1)
all_sprites.add(OB2)
all_sprites.add(OB3)
all_sprites.add(OB4)
all_sprites.add(OB5)

platforms = pygame.sprite.Group()
platforms.add(PT1)

players = pygame.sprite.Group()
players.add(P1)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    displaysurface.fill((0, 0, 0))

    textsurf = pyFont.render(str(SCORE), False, (255, 255, 0))
    displaysurface.blit(textsurf, (0,0))

    for entity in all_sprites:
        entity.move(platforms)
        CURR_SCORE = entity.update(platforms, players)
        if CURR_SCORE == -1:
            sys.exit(SCORE)
        else:
            SCORE += CURR_SCORE
        displaysurface.blit(entity.surf, entity.rect)

    pygame.display.update()
    FramePerSec.tick(FPS)
