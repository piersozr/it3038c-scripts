import pygame
from pygame.locals import *
import sys
from globals import *
from player import *
from floor import *
from obstacle import *

# pygame needs this
pygame.init()

FramePerSec = pygame.time.Clock()

# screen size
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Game")
pygame.font.init()
pyFont = pygame.font.SysFont('Lucida Console', 14)

plat = floor()
play = Player()
SCORE = 0

# falling objects
OB1 = Obstacle()
OB2 = Obstacle()
OB3 = Obstacle()
OB4 = Obstacle()
OB5 = Obstacle()

all_sprites = pygame.sprite.Group()
all_sprites.add(plat)
all_sprites.add(play)
all_sprites.add(OB1)
all_sprites.add(OB2)
all_sprites.add(OB3)
all_sprites.add(OB4)
all_sprites.add(OB5)

floors = pygame.sprite.Group()
floors.add(plat)

players = pygame.sprite.Group()
players.add(play)

# game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # clear screen
    displaysurface.fill((0, 0, 0))

    textsurf = pyFont.render(str(SCORE), False, (255, 255, 0))
    displaysurface.blit(textsurf, (0, 0))

    for entity in all_sprites:
        entity.move(floors)
        CURR_SCORE = entity.update(floors, players)
        if CURR_SCORE == -1:
            # quit game
            sys.exit(SCORE)
        else:
            # add to score
            SCORE += CURR_SCORE
        displaysurface.blit(entity.surf, entity.rect)

    pygame.display.update()
    FramePerSec.tick(FPS)
