# Using the pygame library, draw a simple picture. 
# It can be anything you like, but you must use at least 2 different types of shapes and 3 different colors.

import random

import pygame

from pygame.event import wait

x = 750
y = 400
pygame.init()
GameSurface = pygame.display.set_mode((x, y))
print("Type disconnect to exit, or press enter to continue: ")
while True:
    for i in range(round(x*y/150)):
        color = random.randint(0,5)
        if color == 1:
            color = "blue"
        elif color == 2:
            color = "red"
        elif color == 3:
            color = "green"
        elif color == 4:
            color = "yellow"
        else:
            color = "white"
        pygame.draw.circle(GameSurface,color,(random.randint(0,x), random.randint(0,y)), x*y/10000)
        pygame.draw.circle(GameSurface,color,(random.randint(0,x), random.randint(0,y)), x*y/10000)
    if input() == "disconnect":
        break