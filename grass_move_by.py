import pygame
import sys
import random
import time


def main():
    pygame.init()


    pygame.display.set_caption("Hello World")
    x = 900

    screen = pygame.display.set_mode((1200, 620))
    # TODO 05: Change the window size, make sure your circle code still works.
    while True:
        screen.fill((255, 255, 255))
        image1 = pygame.image.load("grass_for_flappy.png")
        screen.blit(image1, (x , 580))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        clock = pygame.time.Clock()
        font = pygame.font.SysFont('Arial', 40)
        pygame.display.update()


class grass:
    def __init__(self, screen, x, y):
        """ Creates a Raindrop sprite that travels down at a random speed. """
        # TODO 8: Initialize this Raindrop, as follows:
        #     - Store the screen.
        #     - Set the initial position of the Raindrop to x and y.
        #     - Set the initial speed to a random integer between 5 and 15.
        #   Use instance variables:   screen  x  y  speed.
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = (5)


    def move(self):

        self.x = self.x - self.speed

    def off_screen(self):
        """ Returns true if the Raindrop y value is not shown on the screen, otherwise false. """
        # Note: this will be used for testing, but not used in the final version of the code for the sake of simplicity.
        # TODO 13: Return  True  if the  y  position of this Raindrop is greater than 800.
        image_length = 394
        return self.x < 0 + image_length

    def draw(self):
        """ Draws this sprite onto the screen. """
        # TODO 9: Draw a vertical line that is 5 pixels long, 2 pixels thick,
        #      from the current position of this Raindrop (use either a black or blue color).
        image1 = pygame.image.load("grass_for_flappy.png")
        self.screen.blit(image1, (900,580))



if __name__ == "__main__":
    main()