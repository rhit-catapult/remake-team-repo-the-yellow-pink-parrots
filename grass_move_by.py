import pygame
import sys
import random
import time

class Grass:
    def __init__(self, screen, x, y):
        """ Creates a Raindrop sprite that travels down at a random speed. """
        # TODO 8: Initialize this Raindrop, as follows:
        #     - Store the screen.
        #     - Set the initial position of the Raindrop to x and y.
        #     - Set the initial speed to a random integer between 5 and 15.
        #   Use instance variables:   screen  x  y  speed.
        self.image1 = pygame.image.load("grass_for_flappy.png")
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = 5
        self.grass_list = []
        grass_list = self.grass_list


    def move(self):

        self.x = self.x - self.speed


    def off_screen(self):
        """ Returns true if the Raindrop y value is not shown on the screen, otherwise false. """
        image_length = 384
        return self.x < 0 - image_length

    def draw(self):
        """ Draws this sprite onto the screen. """
        # TODO 9: Draw a vertical line that is 5 pixels long, 2 pixels thick,
        #      from the current position of this Raindrop (use either a black or blue color).
        self.screen.blit(self.image1, (self.x ,580))

def main():
    pygame.init()



    screen = pygame.display.set_mode((1200, 620))
    grass1 = Grass(screen, 1200, 580)
    grass2 = Grass(screen, 900, 580)
    grass3 = Grass(screen, 600, 580)
    grass4 = Grass(screen, 300, 580)
    grass5 = Grass(screen, 000, 580)
    clock = pygame.time.Clock()
    grass_list = []
    for i in range(6):
        x = i* 394
        y = 580
        g = Grass(screen, x, 580)
        grass_list.append(g)

    # TODO 05: Change the window size, make sure your circle code still works.
    while True:
        screen.fill((255, 255, 255))
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        clock = pygame.time.Clock()

        for g in grass_list:
            g.move()
            g.draw()

        if grass_list[0].off_screen() :
            del grass_list[0]
            x = grass_list[-1].x + 328
            y = 580
            new_grass = Grass (screen, x,y)
            grass_list.append(new_grass)



        font = pygame.font.SysFont('Arial', 40)
        pygame.display.update()





if __name__ == "__main__":
    main()