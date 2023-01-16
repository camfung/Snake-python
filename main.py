import pygame as pg

# Initialize pygame library
pygame.init()

# Set the size of the window
window_size = (width, height) = (500, 500)

# Create the window
screen = pg.display.set_mode(window_size)

# Set the title of the window
pg.display.set_caption("My Snake Game")

fff

# Run the game loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

# Clean up and quit pygame
pg.quit()
