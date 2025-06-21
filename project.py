import pygame
import sys
import my_character
import random
import time


def main():
    # turn on pygame
    pygame.init()

    # create a screen
    pygame.display.set_caption("Flappy Bird")
    # TODOne: Change the size of the screen as you see fit!
    screen = pygame.display.set_mode((1200, 620))
    # creates a Character from the my_character.py file
    character = my_character.Character(screen, 100, 100)

    # let's set the framerate
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)  # this sets the framerate of your game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            screen.fill((25, 255, 255))

        # draws the character every frame
        character.draw()

        # TODO: Add your project code

        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()


main()