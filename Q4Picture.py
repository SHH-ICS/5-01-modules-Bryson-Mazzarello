import pygame
import sys
import random
from pygame.locals import QUIT

x = 900
y = x/2

FPS = 15

Clock = pygame.time.Clock()
pygame.init()
DISPLAYSURF = pygame.display.set_mode((x, y))
DISPLAYSURF.fill(pygame.Color(135,0,0))
pygame.display.set_caption('Maholagoe')
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
   for nil in range(round(244/FPS)):
      pygame.draw.line(DISPLAYSURF, (000,000,000), (Random()), (Random()),round(( 0.1*FPS)*( (x+y)/400+1)))
      pygame.draw.line(DISPLAYSURF, (255,255,255), (Random()), (Random()),round(( 0.05*FPS)*( (x+y)/400+1)))
   Clock.tick(FPS)
   pygame.display.update()
