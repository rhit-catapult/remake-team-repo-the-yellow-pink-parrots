import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1440, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Game variables
gravity = 0.5
bird_movement = 0
game_active = True
score = 0
font = pygame.font.SysFont('Arial', 40)

# Bird
bird = pygame.Rect(100, HEIGHT // 2, 30, 30)

# Pipes
pipe_width = 60
pipe_height = random.randint(150, 450)
pipe_gap = 150
pipe_x = WIDTH
pipe_speed = 4

# Clock
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLUE = (135, 206, 250)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def draw_pipes(x, height):
    bottom_pipe = pygame.Rect(x, height + pipe_gap, pipe_width, HEIGHT)
    top_pipe = pygame.Rect(x, 0, pipe_width, height)
    pygame.draw.rect(screen, GREEN, bottom_pipe)
    pygame.draw.rect(screen, GREEN, top_pipe)
    return top_pipe, bottom_pipe

def check_collision(bird, pipes):
    for pipe in pipes:
        if bird.colliderect(pipe):
            return False
    if bird.top <= 0 or bird.bottom >= HEIGHT:
        return False
    return True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_movement = -8
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # Reset game
                bird.y = HEIGHT // 2
                pipe_x = WIDTH
                pipe_height = random.randint(150, 450)
                score = 0
                bird_movement = 0
                game_active = True

    screen.fill(BLUE)

    if game_active:
        # Bird
        bird_movement += gravity
        bird.y += int(bird_movement)
        pygame.draw.ellipse(screen, RED, bird)

        # Pipes
        pipe_x -= pipe_speed
        if pipe_x + pipe_width < 0:
            pipe_x = WIDTH
            pipe_height = random.randint(150, 450)
            score += 1

        pipes = draw_pipes(pipe_x, pipe_height)

        # Collision
        game_active = check_collision(bird, pipes)

        # Score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

    else:
        game_over_text = font.render("Game Over!", True, WHITE)
        screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 40))
        restart_text = font.render("Press SPACE to Restart", True, WHITE)
        screen.blit(restart_text, (WIDTH // 2 - 150, HEIGHT // 2 + 10))

    pygame.display.update()
    clock.tick(60)
