import pygame
import random
import os
# no boundaries from all side , loop **
# walls for game over after 5 points plus


pygame.init()
pygame.mixer.init()
screen_width = 500
screen_height = 300
gameWindow = pygame.display.set_mode((screen_width,screen_height))
bg_image = pygame.image.load("game_bg_image.jpg")
bg_image = pygame.transform.scale(bg_image, (screen_width, screen_height)).convert_alpha()
pygame.display.set_caption("Snake Game by priyanshu_barnwal")
pygame.display.update()
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 30)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def plot_snake(gameWindow, black, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.ellipse(gameWindow , black, [x, y, snake_size, snake_size])
def welcome_screen():
    if(not os.path.exists("score.txt")):
        with open("score.txt", "w") as f:
            f.write("0")
    else:
        with open("score.txt", "r") as f:
            hiscore = f.read()
    exit_game = False
    while not exit_game:
        gameWindow.fill((255,255,255))
        text_screen("Welcome to snake game", (0,0,0), 120, 100)
        text_screen("Enter space bar for start the game!", (0,0,0), 90, 130)
        text_screen("Highest Score is :- "+hiscore, (0,0,0), 90, 150)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("game_bg.mp3")
                    pygame.mixer.music.play(-1)
                    game_loop()
        pygame.display.update()
        clock.tick(30)
    pygame.quit() #


            
def game_loop():
    white = (255, 255, 255)
    red = (255, 0, 0)
    black = (0, 0, 0)
    green = (0, 128, 0)
    exit_game = False
    game_over = False
    init_velocity = 2
    snake_x = 45
    snake_y = 55
    snake_size = 10

    fps = 30
    velocity_x = init_velocity
    velocity_y = 0
    food_x = random.randint(20, screen_width)
    food_y = random.randint(20, screen_height)
    food_size = 12
    food_color = (255,255,0)
    score = 0
    switch = False
    snake_length = 12
    snake_list = []
    if(not os.path.exists("score.txt")):
        with open("score.txt", "w") as f:
            f.write("0")
    with open("score.txt", "r") as f:
        hiscore = f.read()
    
    while not exit_game:
        if game_over:
            with open("score.txt", "w") as f:
                f.write(str(hiscore))
            
            gameWindow.fill(white)
            text_screen("Game Over! Please Enter to Restart", red,100,100)
            text_screen("Score:-"+str(score), red,100,120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome_screen()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if velocity_y == -init_velocity or velocity_y == init_velocity:
                            velocity_x = init_velocity
                            velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        if velocity_y == -init_velocity or velocity_y == init_velocity:
                            velocity_x = -init_velocity
                            velocity_y = 0
                    if event.key == pygame.K_UP:
                        if velocity_x == -init_velocity or velocity_x == init_velocity:
                            velocity_y = -init_velocity
                            velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        if velocity_x == -init_velocity or velocity_x == init_velocity:    
                            velocity_y = init_velocity
                            velocity_x = 0
                    if event.key == pygame.K_q: #cheat code 'Q' for making snake immortal by hitting the boundary.
                        switch = True
                    if event.key == pygame.K_w: #cheat code 'W' for reverse from snake immortal by hitting the boundary.
                        switch = False
                        
                        
            snake_x += velocity_x
            snake_y += velocity_y

            if abs(food_x - snake_x) < 10 and abs(food_y - snake_y) < 10:
                score += 1
                snake_length += 3
                
                food_x = random.randint(10, screen_width/2)
                food_y = random.randint(40, screen_height/2)

            gameWindow.fill(white)
            gameWindow.blit(bg_image, (0,0))
            
            
            
            if score > int(hiscore):
                hiscore = score
            text_screen("Score- "+str(score) +"  hiscore- "+ str(hiscore), red, 5, 5)
            pygame.draw.rect(gameWindow, food_color, [food_x, food_y, food_size, food_size])    

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list) > snake_length:
                del snake_list[0]
            if head in snake_list[:-1]:
                pygame.mixer.music.stop()
                game_over = True
            if switch: 
                if snake_x < 0:
                    snake_x=screen_width
                    #print("left to right:- ",snake_x,snake_y)
                elif snake_x > screen_width:  
                    snake_x = 0
                    #print("right to left:- ",snake_x,snake_y)
                elif snake_y < 0:
                    #print(snake_x,snake_y)
                    snake_y = screen_height
                elif snake_y >  screen_height:
                    snake_y = 0
                    #print(snake_x,snake_y)
            else:
                 if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y >  screen_height :
                    pygame.mixer.music.stop()
                    game_over = True   
            plot_snake(gameWindow, black, snake_list, snake_size)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
quit()  
#game_loop()
welcome_screen()
