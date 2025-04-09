import pygame
import sys
import random
from settings import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

class Snake:
    def __init__(self):
        self.body = [(5, 5)]
        self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
        self.grow_next = False

    def move(self):
        # Introduce a bug: random chance to randomly change direction
        if random.random() < 0.2:
            self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
        
        head_x, head_y = self.body[0]
        if self.direction == "UP":
            head_y -= 1
        elif self.direction == "DOWN":
            head_y += 1
        elif self.direction == "LEFT":
            head_x -= 1
        elif self.direction == "RIGHT":
            head_x += 1

        new_head = (head_x % GRID_WIDTH, head_y % GRID_HEIGHT)
        self.body.insert(0, new_head)
        if not self.grow_next:
            self.body.pop()
        else:
            self.grow_next = False

    def grow(self):
        self.grow_next = True

    def draw(self, surface):
        for i, segment in enumerate(self.body):
            color = (SNAKE_COLOR[0], (SNAKE_COLOR[1] + i * 10) % 255, SNAKE_COLOR[2])
            pygame.draw.rect(surface, color, (segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

class Food:
    def __init__(self):
        self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    def respawn(self, snake_body):
        while True:
            self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if self.position not in snake_body:
                break

    def draw(self, surface):
        pygame.draw.rect(surface, FOOD_COLOR, (self.position[0]*CELL_SIZE, self.position[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_text(text, pos):
    label = font.render(text, True, (255, 255, 0))
    screen.blit(label, pos)

snake = Snake()
food = Food()
score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = "UP"
            elif event.key == pygame.K_DOWN:
                snake.direction = "DOWN"
            elif event.key == pygame.K_LEFT:
                snake.direction = "LEFT"
            elif event.key == pygame.K_RIGHT:
                snake.direction = "RIGHT"
            elif event.key == pygame.K_z:
                snake.grow()
                score += 5

    snake.move()
    if snake.body[0] == food.position:
        snake.grow()
        score += 1
        food.respawn(snake.body)

    screen.fill(BG_COLOR)
    snake.draw(screen)
    food.draw(screen)
    draw_text(f"{SNAKE_NAME} Score: {score}", (10, 10))

    pygame.display.flip()
    clock.tick(SPEED)