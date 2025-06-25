import pygame
import sys
import random
from grass_move_by import Grass


WIDTH, HEIGHT = 1200, 620
BIRD_SIZE_x = 30
BIRD_SIZE_y = 21
gravity = 0.5
pipe_gap = 130
pipe_speed = 5

DARK_BLUE = (0, 0, 139)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

pygame.init()
pygame.mixer.init()

BACKGROUND = pygame.image.load("rose_background.png")
BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
EMMET1 = pygame.image.load("emmet1.png")
EMMET2 = pygame.image.load("emmet2.png")
EMMET1 = pygame.transform.scale(EMMET1, (300, 300))
EMMET2 = pygame.transform.scale(EMMET2, (300, 300))
BUBBLE = pygame.image.load("speech_bubble.png")
BUBBLE = pygame.transform.scale(BUBBLE, (500, 500))
TITLE_BIRD = pygame.image.load("pink_bird.png")

FLAP = pygame.mixer.Sound("flap.wav")
DIE = pygame.mixer.Sound("die.wav")

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


class Bird:
    def __init__(self, screen, x, y, bird_image1):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(bird_image1)
        self.image = pygame.transform.scale(self.image, (BIRD_SIZE_x, BIRD_SIZE_y))

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, BIRD_SIZE_x, BIRD_SIZE_y)


def draw_pipes(screen, x, height):
    bottom_pipe = pygame.Rect(x, height + pipe_gap, 60, HEIGHT)
    top_pipe = pygame.Rect(x, 0, 60, height)
    pygame.draw.rect(screen, GREEN, bottom_pipe)
    pygame.draw.rect(screen, GREEN, top_pipe)
    return top_pipe, bottom_pipe


def check_collision(bird, pipes):
    bird_rect = bird.get_rect()
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False
    if bird_rect.top <= 0 or bird_rect.bottom >= HEIGHT:
        return False
    return True


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Flappy Bird")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Arial', 40)

    bird = Bird(screen, 310, HEIGHT // 2, "pink_bird.png")
    bird_movement = 0
    game_active = False
    start_screen = True
    score = 0

    pipe_x = WIDTH
    pipe_height = random.randint(150, 450)

    grass_list = []
    for i in range(6):
        x = i * 394
        y = 580
        g = Grass(screen, x, 580)
        grass_list.append(g)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            if start_screen:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    start_screen = False
                    game_active = True
            elif game_active:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    bird_movement = -9
                    FLAP.play()
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    bird.y = HEIGHT // 2
                    pipe_x = WIDTH
                    pipe_height = random.randint(150, 450)
                    score = 0
                    bird_movement = 0
                    game_active = True

        screen.blit(BACKGROUND, (0, 0))

        if start_screen:
            title_text = font.render("Welcome to Flappy Bird!", True, WHITE)
            instruction_text = font.render("Press SPACE to Start", True, WHITE)
            screen.blit(title_text, (WIDTH // 2 - 215, HEIGHT // 2 - 50))
            screen.blit(instruction_text, (WIDTH // 2 - 195, HEIGHT // 2))
            screen.blit(TITLE_BIRD,(432,350))


        elif game_active:
            bird_movement += gravity
            bird.y += int(bird_movement)
            pipe_x -= pipe_speed

            if pipe_x + 60 < 0:
                pipe_x = WIDTH
                pipe_height = random.randint(150, 450)
                score += 1

            pipes = draw_pipes(screen, pipe_x, pipe_height)
            bird.draw()

            was_active = game_active
            game_active = check_collision(bird, pipes)
            if was_active and not game_active:
                DIE.play()

            score_text = font.render(f"Score: {score}", True, WHITE)
            screen.blit(score_text, (10, 10))

            for g in grass_list:
                g.move()
                g.draw()

            if grass_list[0].off_screen():
                del grass_list[0]
                x = grass_list[-1].x + 328
                y = 580
                new_grass = Grass(screen, x, y)
                grass_list.append(new_grass)

        else:
            # Game over screen
            label_game_over = font.render("GRASS HOLE!", True, WHITE)
            label_restart = font.render("Press Enter to Restart", True, WHITE)
            label_score = font.render(f"Score: {score}", True, WHITE)

            screen.blit(label_game_over, (WIDTH // 2 - 100, HEIGHT // 2 - 60))
            screen.blit(label_restart, (WIDTH // 2 - 180, HEIGHT // 2 - 10))
            screen.blit(label_score, (WIDTH // 2 - 60, HEIGHT // 2 + 40))

            bird.draw()
            screen.blit(EMMET1, (150, 510))
            screen.blit(EMMET2, (900, 150))
            screen.blit(BUBBLE, (350, 100))

        pygame.display.update()
        clock.tick(60)





main()

