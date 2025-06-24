import pygame
import sys
import random
from grass_move_by import grass


WIDTH, HEIGHT = 1200, 620
BIRD_SIZE = 60
gravity = 0.5
pipe_gap = 150
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

FLAP = pygame.mixer.Sound("flap.wav")
DIE = pygame.mixer.Sound("die.wav")


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

            was_active = game_active
            game_active = check_collision(bird, pipes)
            if was_active and not game_active:
                DIE.play()

            score_text = font.render(f"Score: {score}", True, WHITE)
            screen.blit(score_text, (10, 10))

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

