import pygame
import sys
import random
from pygame.locals import QUIT

x = 900
y = 500

FPS = 16

Clock = pygame.time.Clock()
pygame.init()
DISPLAYSURF = pygame.display.set_mode((x, y))
DISPLAYSURF.fill(pygame.Color(135,0,0))
pygame.display.set_caption('Idk')
def Random():
   rndX = random.randint(0,x)
   rndY = random.randint(0,y)
   return rndX, rndY

def Malev():
   DISPLAYSURF.fill(pygame.Color(135,0,0))
   pygame.draw.rect(DISPLAYSURF, pygame.Color(0,0,100), (x/3.25,y/3.25,x/3.25,y/3.25))
   return

while True:
   for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
   Malev()
   for nil in range(round(7*32/FPS)):
      pygame.draw.line(DISPLAYSURF, (0,0,0), (Random()), (Random()),round(9/32*FPS+3))
      pygame.draw.line(DISPLAYSURF, (255,255,255), (Random()), (Random()),round(6/32*FPS+3))
   Clock.tick(FPS)
   pygame.display.update()