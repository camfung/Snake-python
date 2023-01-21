import pygame as pg
import random
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
snake_pos = []

snake_head = pg.Rect(snake_x, snake_y, snake_size, snake_size)




#adding the head to the body
snake_body.append(snake_head)
snake_pos.append([snake_x, snake_y])

# setting up the food
food_x = 25
food_y = 25

food_rect = pg.Rect(food_x, food_y, snake_size, snake_size)

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


    snake_pos[0][0] += snake_dir_x * snake_size
    snake_pos[0][1] += snake_dir_y * snake_size

    # check for if its colliding with the food
    if snake_pos[0][1] == food_y and snake_pos[0][0] == food_x:
        # going rigth
        new_x = 0
        new_y = 0
        if snake_dir_x == 1 and snake_dir_y == 0:
            new_x = snake_pos[0][0] - snake_size
            new_y = snake_pos[0][1]
            snake_body.append(pg.Rect(new_x, new_y, snake_size, snake_size))
            snake_pos.append([new_x, new_y])
        elif snake_dir_x == -1 and snake_dir_y == 0:
            new_x = snake_pos[0][0] + snake_size
            new_y = snake_pos[0][1]
            snake_body.append(pg.Rect(new_x, new_y, snake_size, snake_size))
            snake_pos.append([new_x, new_y])
        elif snake_dir_x == 0 and snake_dir_y == 1:
            new_x = snake_pos[0][0]
            new_y = snake_pos[0][1] - snake_size
            snake_body.append(pg.Rect(new_x, new_y, snake_size, snake_size))
            snake_pos.append([new_x, new_y])
        elif snake_dir_x == 0 and snake_dir_y == -1:
            new_x = snake_pos[0][0]
            new_y = snake_pos[0][1] + snake_size
            snake_body.append(pg.Rect(new_x, new_y, snake_size, snake_size))
            snake_pos.append([new_x, new_y])


    if snake_pos[0][1] < 0:
        snake_pos[0][1] = height
    elif snake_pos[0][1] > height:
        snake_pos[0][1] = 0
    if snake_pos[0][0] < 0:
        snake_pos[0][0] = width
    elif snake_pos[0][0] > width:
        snake_pos[0][0] = 0

    pg.draw.rect(screen, (255, 0, 0), food_rect)
    for i in range(len(snake_body)):
        rect = snake_body[i]
        rect.x = snake_pos[i][0]
        rect.y = snake_pos[i][1]
        pg.draw.rect(screen, (255, 255, 255), rect)

    pg.display.flip()



    # check if the snake has collided with its own body
    for i in range(1, len(snake_body)):
        if snake_pos[0][0] == snake_pos[i][0] and snake_pos[0][1] == snake_pos[i][1]:
            running = False
            print("Game Over")


    # check for collision with the food
    if snake_pos[0][0] == food_x and snake_pos[0][1] == food_y:
        # randomly place the food in a new location

        random_array = range(0, width, 25)

        food_x = random_array[random.randint(0, len(random_array))-1]

        food_y = random_array[random.randint(0, len(random_array))-1]

        food_rect = pg.Rect(food_x, food_y, snake_size, snake_size)

        # grow the snake
        new_x = 0
        new_y = 0
        if snake_dir_x == 1 and snake_dir_y == 0:
            new_x = snake_pos[-1][0] - snake_size
            new_y = snake_pos[-1][1]
            snake_body.append(pg.Rect(new_x, new_y, snake_size, snake_size))
            snake_pos.append([new_x, new_y])
        elif snake_dir_x == -1 and snake_dir_y == 0:
            new_x = snake_pos[-1][0] + snake_size
            new_y = snake_pos[-1][1]
            snake_body.append(pg.Rect(new_x, new_y, snake_size, snake_size))
            snake_pos.append([new_x, new_y])
        elif snake_dir_x == 0 and snake_dir_y == 1:
            new_x = snake_pos[-1][0]
            new_y = snake_pos[-1][1] - snake_size
            snake_body.append(pg.Rect(new_x, new_y, snake_size, snake_size))
            snake_pos.append([new_x, new_y])
        elif snake_dir_x == 0 and snake_dir_y == -1:
            new_x = snake_pos[-1][0]
            new_y = snake_pos[-1][1] + snake_size
            snake_body.append(pg.Rect(new_x, new_y, snake_size, snake_size))
            snake_pos.append([new_x, new_y])




# Clean up and quit pg
pg.quit()






