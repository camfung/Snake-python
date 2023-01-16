import pygame as pg

# Initialize pygame library
pg.init()

# Set the size of the window
window_size = (width, height) = (500, 500)

# Create the window
screen = pg.display.set_mode(window_size)

# Set the title of the window
pg.display.set_caption("My Snake Game")

#setting up the snake

snake_x = 250
snake_y = 250

snake_size = 25

snake_body = []

snake_head = pg.Rect(snake_x, snake_y, snake_size, snake_size)

#adding the head to the body
snake_body.append(snake_head)

# Run the game loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    for rect in snake_body:
        pg.draw.rect(screen, (255, 255, 255), rect)

    pg.display.flip()




# Clean up and quit pygame
pg.quit()
