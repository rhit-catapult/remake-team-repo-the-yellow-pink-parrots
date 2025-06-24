import pygame
import sys
import random

# Game Constants
WIDTH, HEIGHT = 1200, 620
BIRD_SIZE = 60
gravity = 0.5
pipe_gap = 150
pipe_speed = 5

# Colors
DARK_BLUE = (0, 0, 139)
GREEN = (0, 255, 0)

# Load Background and Images
BACKGROUND = pygame.image.load("rose_background.png")
BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
EMMET1 = pygame.image.load("emmet1.png")
EMMET2 = pygame.image.load("emmet2.png")
EMMET1 = pygame.transform.scale(EMMET1, (300, 300))
EMMET2 = pygame.transform.scale(EMMET2, (300, 300))


class Bird:
    def __init__(self, screen, x, y, bird_image1):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(bird_image1)
        self.image = pygame.transform.scale(self.image, (BIRD_SIZE, BIRD_SIZE))

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, BIRD_SIZE, BIRD_SIZE)


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
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Flappy Bird")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Arial', 40)

    bird = Bird(screen, 310, HEIGHT // 2, "pink_bird.png")
    bird_movement = 0
    game_active = True
    score = 0

    pipe_x = WIDTH
    pipe_height = random.randint(150, 450)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if game_active:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    bird_movement = -8
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    bird.y = HEIGHT // 2
                    pipe_x = WIDTH
                    pipe_height = random.randint(150, 450)
                    score = 0
                    bird_movement = 0
                    game_active = True

        screen.blit(BACKGROUND, (0, 0))

        if game_active:
            bird_movement += gravity
            bird.y += int(bird_movement)
            pipe_x -= pipe_speed

            if pipe_x + 60 < 0:
                pipe_x = WIDTH
                pipe_height = random.randint(150, 450)
                score += 1

            pipes = draw_pipes(screen, pipe_x, pipe_height)
            bird.draw()
            game_active = check_collision(bird, pipes)

            score_text = font.render(f"Score: {score}", True, DARK_BLUE)
            screen.blit(score_text, (10, 10))
        else:
            # Show Game Over Text
            label_game_over = font.render("GRASS HOLE!", True, DARK_BLUE)
            label_restart = font.render("Press Enter to Restart", True, DARK_BLUE)
            label_score = font.render(f"Score: {score}", True, DARK_BLUE)

            screen.blit(label_game_over, (WIDTH // 2 - 100, HEIGHT // 2 - 60))
            screen.blit(label_restart, (WIDTH // 2 - 180, HEIGHT // 2 - 10))
            screen.blit(label_score, (WIDTH // 2 - 60, HEIGHT // 2 + 40))

            bird.draw()
            screen.blit(EMMET1, (bird.x - 250, bird.y - 300))
            screen.blit(EMMET2, (bird.x + 550, bird.y - 300))

        pygame.display.update()
        clock.tick(60)


main()
