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
        self.hue = 0

    def move(self):
        # TODO: Remove following block of code to make snake not randomly change direction
        ### Block Start
        if random.random() < 0.1:
            possible_directions = ["UP", "DOWN", "LEFT", "RIGHT"]
            
            # Remove the opposite direction of the current direction
            if self.direction == "UP":
                possible_directions.remove("DOWN")
            elif self.direction == "DOWN":
                possible_directions.remove("UP")
            elif self.direction == "LEFT":
                possible_directions.remove("RIGHT")
            elif self.direction == "RIGHT":
                possible_directions.remove("LEFT")
            
            # Pick a new direction from the remaining options
            self.direction = random.choice(possible_directions)
        ### Block End
        
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

        # TODO add following lines for collisions
        ### START OF CHANGE
        # Check for collisions with walls (you can keep this commented out for "pacman" style snake)
        #if not (0 <= head_x < GRID_WIDTH and 0 <= head_y < GRID_HEIGHT):
        #    pygame.quit()
        #    sys.exit()
        
        # Check for collisions with self
        if new_head in self.body[1:]:
            pygame.quit()
            sys.exit()
        ### END OF CHANGE

        if not self.grow_next:
            self.body.pop()
        else:
            self.grow_next = False

    def grow(self):
        self.grow_next = True

    def draw(self, surface):
        for i, segment in enumerate(self.body):
            # Calculate the hue for this segment
            hue = (self.hue + i * 10) % 360  # Shift hue based on segment index

            # Convert hue to RGB
            color = pygame.Color(0)
            color.hsva = (hue, 100, 100)  # Use full saturation and brightness
            
            pygame.draw.rect(surface, color, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        # Increment the hue for the next frame (to cycle the colors)
        self.hue = (self.hue + 1) % 360

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
            if event.key == pygame.K_UP and snake.direction != "DOWN":
                snake.direction = "UP"
            elif event.key == pygame.K_DOWN and snake.direction != "UP":
                snake.direction = "DOWN"
            elif event.key == pygame.K_LEFT and snake.direction != "RIGHT":
                snake.direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake.direction != "LEFT":
                snake.direction = "RIGHT"
            # TODO remove this elif statement to prevent growth from key z in original game
            # (or if you're feeling fun you can try and add something else)
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