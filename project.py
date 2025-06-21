import pygame
import sys
import random
import time

class Bird:
    def __init__(self, screen, x, y, bird_image1):
        self.screen = screen
        self.x = x
        self.y = y
        self.bird_image1 = pygame.image.load(bird_image1)

    def draw(self):
        self.screen.blit(self.bird_image1, (self.x, self.y))

def main():
    # turn on pygame
    pygame.init()

    # create a screen
    pygame.display.set_caption("Flappy Bird")
    # TODOne: Change the size of the screen as you see fit!
    screen = pygame.display.set_mode((1200, 620))
    # creates a Character from the my_character.py file
    bird = Bird(screen, 600, 310, "pink_bird.png")
    # let's set the framerate
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)  # this sets the framerate of your game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            screen.fill((25, 255, 255))

        # draws the character every frame
        bird.draw()
        # TODO: Add your project code

        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()


main()