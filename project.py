import pygame
import sys
import random


WIDTH, HEIGHT = 1200, 620
BIRD_SIZE = 60
gravity = 0.5
pipe_gap = 150
pipe_speed = 4

WHITE = (255, 255, 255)
BLUE = (135, 206, 250)
GREEN = (0, 255, 0)

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
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    bird.y = HEIGHT // 2
                    pipe_x = WIDTH
                    pipe_height = random.randint(150, 450)
                    score = 0
                    bird_movement = 0
                    game_active = True

        screen.fill(BLUE)

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

            score_text = font.render(f"Score: {score}", True, WHITE)
            screen.blit(score_text, (10, 10))
        else:
            game_over_text = font.render("Game Over!", True, WHITE)
            screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 40))
            restart_text = font.render("Press SPACE to Restart", True, WHITE)
            screen.blit(restart_text, (WIDTH // 2 - 150, HEIGHT // 2 + 10))
            bird.draw()

        pygame.display.update()
        clock.tick(60)

main()
