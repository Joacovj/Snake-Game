import pygame as pg 
import random

# Configuring the settings of the window, color, time tracking, snake position and speed

width, height = 600, 600
block_size = 20

pg.font.init()
score_font = pg.font.SysFont("consolas", 20)
score = 0

WHITE = (255,255,255)
RED = (255, 0, 0)

pg.init()
window = pg.display.set_mode((width,height))

clock = pg.time.Clock()

snake_pos = [[width / 2 , height / 2]]
snake_speed = [0, block_size]

teleport_walls = True

# Generating the food

def generate_food():
    while True:
        x = random.randint(0, (width - block_size) // block_size) * block_size
        y = random.randint(0, (height - block_size) // block_size) * block_size
        food_pos = [x,y]
        if food_pos not in snake_pos:
            return food_pos

food_pos = generate_food()

# Drawing

def draw_objects():
    window.fill((0,0,0))
    for pos in snake_pos:
        pg.draw.rect(window, (0,128,0), pg.Rect(pos[0], pos[1], block_size, block_size))
    pg.draw.rect(window, RED, pg.Rect(food_pos[0], food_pos[1], block_size, block_size))

    score_text = score_font.render(f"Score: {score}", True, WHITE)
    window.blit(score_text, (10, 10))

# Updating Snake Position
    
def update_snake():
    global food_pos, score
    new_head = [snake_pos[0][0] + snake_speed[0], snake_pos[0][1] + snake_speed[1]]

    if teleport_walls:
        if new_head[0] >= width:
                new_head[0] = 0
        elif new_head[0] < 0:
                new_head[0] = width - block_size
        if new_head[1] >= height:
                new_head[1] = 0
        elif new_head[1] < 0:
                new_head[1] = height - block_size

    if new_head == food_pos:
        food_pos = generate_food()
        score += 1
    else:
        snake_pos.pop()

    snake_pos.insert(0,new_head)

# Checking Game Over Condition

def game_over():
    if teleport_walls:
         return snake_pos[0] in snake_pos[1:]
    else:
        return snake_pos[0] in snake_pos[1:] or \
        snake_pos[0][0] > width - block_size or \
        snake_pos[0][0] < 0 or \
        snake_pos[0][1] > height - block_size or \
        snake_pos[0][1] < 0
        
# Displaying the Game Over Screen
        
def game_over_screen():
    global score
    window.fill((0,0,0))
    game_over_font = pg.font.SysFont("consolas", 50)
    game_over_text = game_over_font.render(f"Game Over! Score: {score}", True, WHITE)
    window.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2, 
                                 height // 2 - game_over_text.get_height() // 2))
    pg.display.update()

# Loop to see if player choses to restart game (r) or quit the game (q)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return
                
            if event.type == pg.KEYDOWN:

                if event.key == pg.K_r:
                    run()
                    return
                elif event.key == pg.K_q:
                    pg.quit()
                    return
                    
# Handling User Input and Main Game Loop

def run():
    global snake_speed, snake_pos, food_pos, score
    snake_pos = [[width//2, height//2]]
    snake_speed = [0, block_size]
    food_pos = generate_food()
    score = 0
    running = True

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            keys = pg.key.get_pressed()

            for key in keys:
                if keys[pg.K_UP]:
                    # when UP is pressed but the snake is moving down, ignore the input
                    if snake_speed[1] == block_size:
                        continue
                    snake_speed = [0, -block_size]
                if keys[pg.K_DOWN]:
                    # when DOWN is pressed but the snake is moving up, ignore the input
                    if snake_speed[1] == -block_size:
                        continue
                    snake_speed = [0, block_size]
                if keys[pg.K_LEFT]:
                    # when LEFT is pressed but the snake is moving right, ignore the input
                    if snake_speed[0] == block_size:
                        continue
                    snake_speed = [-block_size, 0]
                if keys[pg.K_RIGHT]:
                    # when RIGHT is pressed but the snake is moving left, ignore the input
                    if snake_speed[0] == -block_size:
                        continue
                    snake_speed = [block_size,0]

        if game_over():
            game_over_screen()
            return
        update_snake()
        draw_objects()
        pg.display.update()
        clock.tick(15)  # limit the frame rate to 15 FPS

if __name__ == '__main__':
    run()

                         
               
        
                    


            
            


                
