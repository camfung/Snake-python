import pygame as pg
import time

fps = 5

clock = pg.time.Clock()

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

snake_dir_x = 1

snake_dir_y = 0


snake_body = []

snake_head = pg.Rect(snake_x, snake_y, snake_size, snake_size)

#adding the head to the body
snake_body.append(snake_head)

# Run the game loop
running = True
while running:
    clock.tick(fps)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                snake_dir_y = -1
                snake_dir_x = 0
            elif event.key == pg.K_DOWN:
                snake_dir_x = 0
                snake_dir_y = 1
            elif event.key == pg.K_LEFT:
                snake_dir_x = -1
                snake_dir_y = 0
            elif event.key == pg.K_RIGHT:
                snake_dir_x= 1
                snake_dir_y= 0



    screen.fill(0)


    snake_x += snake_dir_x * snake_size
    snake_y += snake_dir_y * snake_size
    if snake_y <0:
        snake_y=height
    elif snake_y >height:
        snake_y=0
    if snake_x <0:
        snake_x= width
    elif snake_x> width:
        snake_x=0
    for rect in snake_body:
        rect.x = snake_x
        rect.y = snake_y
        pg.draw.rect(screen, (255, 255, 255), rect)

    pg.display.flip()




# Clean up and quit pg
pg.quit()
