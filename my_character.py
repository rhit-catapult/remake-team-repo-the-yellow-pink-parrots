import pygame
import sys


class Character:
    def __init__(self, screen: pygame.Surface, x, y,bird_image_filename):
        self.screen = screen
        self.x = x
        self.y = y
        self.bird = pygame.image.load(bird_image_filename)

    def draw(self):
        current_image = self.bird.copy()
        self.screen.blit(current_image, (self.x, self.y))
# This function is called when you run this file, and is used to test the Character class individually.
# When you create more files with different classes, copy the code below, then
# change it to properly test that class
def test_character():
    # TODO: change this function to test your class
    screen = pygame.display.set_mode((1200, 620))
    character = Character(screen, 400, 400)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill("white")
        character.draw()
        pygame.display.update()
    bird = Bird(screen, 200, 400, "pink_bird.png")


# Testing the classes
# click the green arrow to the left or run "Current File" in PyCharm to test this class
if __name__ == "__main__":
    test_character()
