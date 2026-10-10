
import pygame
import random

pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

# Snake and food
snake = [(100, 100), (80, 100), (60, 100)]
direction = (20, 0)
food = (random.randrange(0, WIDTH, 20),
        random.randrange(0, HEIGHT, 20))

score = 0
running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 20):
                direction = (0, -20)
            elif event.key == pygame.K_DOWN and direction != (0, -20):
                direction = (0, 20)
            elif event.key == pygame.K_LEFT and direction != (20, 0):
                direction = (-20, 0)
            elif event.key == pygame.K_RIGHT and direction != (-20, 0):
                direction = (20, 0)

            if game_over and event.key == pygame.K_SPACE:
                snake = [(100, 100), (80, 100), (60, 100)]
                direction = (20, 0)
                food = (random.randrange(0, WIDTH, 20),
                        random.randrange(0, HEIGHT, 20))
                score = 0
                game_over = False

    if not game_over:
        head = (snake[0][0] + direction[0],
                snake[0][1] + direction[1])

        snake.insert(0, head)

        if head == food:
            score += 1
            while True:
                food = (random.randrange(0, WIDTH, 20),
                        random.randrange(0, HEIGHT, 20))
                if food not in snake:
                    break
        else:
            snake.pop()

        # Collision detection
        if (head[0] < 0 or head[0] >= WIDTH or
            head[1] < 0 or head[1] >= HEIGHT or
            head in snake[1:]):
            game_over = True

    screen.fill(BLACK)

    # Draw snake
    for part in snake:
        pygame.draw.rect(screen, GREEN,
                         (part[0], part[1], 20, 20))

    # Draw food
    pygame.draw.rect(screen, RED,
                     (food[0], food[1], 20, 20))

    # Display score
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    if game_over:
        message = font.render("GAME OVER! Press SPACE..!", True, WHITE)
        screen.blit(message, (100, 180))

    pygame.display.update()
    clock.tick(10)

pygame.quit()
#snake game
