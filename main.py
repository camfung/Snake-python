import pygame

# Initialize pygame library
pygame.init()

# Set the size of the window
window_size = (width, height) = (500, 500)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("My Snake Game")

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Clean up and quit pygame
pygame.quit()
