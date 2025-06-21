import pygame
import sys
import random
import time

IMAGE_SIZE_X = 32
IMAGE_SIZE_Y = 18

screen = pygame.display.set_mode((1200, 620))
#
image1 = pygame.image.load("grass.png")
    #
image1 = pygame.transform.scale(image1, (IMAGE_SIZE_X, IMAGE_SIZE_Y))
# TODO 2: Draw (blit) the image onto the screen at position (0, 0)


screen.blit(image1, (0,620- IMAGE_SIZE_Y))