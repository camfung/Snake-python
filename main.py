import pygame as pg

# Initialize pg library
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
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                snake_y -= snake_size
            elif event.key == pg.K_DOWN:
                snake_y += snake_size
            elif event.key == pg.K_LEFT:
                snake_x -= snake_size
            elif event.key == pg.K_RIGHT:
                snake_x += snake_size
        pg.display.flip()
    for rect in snake_body:
        rect.x = snake_x
        rect.y = snake_y
        pg.draw.rect(screen, (255, 255, 255), rect)





# Clean up and quit pg
pg.quit()
