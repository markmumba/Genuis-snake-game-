import pygame
import sys
import random
from pygame.math import Vector2
from mathgenerator import mathgen
import textwrap
import database_connection






class SNAKE:

    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
        self.new_block = False

        self.head_up = pygame.image.load(
            'Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load(
            'Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load(
            'Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load(
            'Graphics/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load(
            'Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load(
            'Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load(
            'Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load(
            'Graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load(
            'Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load(
            'Graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load(
            'Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load(
            'Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load(
            'Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load(
            'Graphics/body_bl.png').convert_alpha()

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1]-self.body[0]

        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2]-self.body[-1]

        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)




class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(
            int(self.pos.x * cell_size), int(self.pos.y*cell_size), cell_size, cell_size)
        screen.blit(apple, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number-1)
        self.y = random.randint(0, cell_number-1)
        self.pos = Vector2(self.x, self.y)


class MAIN:
    

    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        self.question_page()
        
    
        
    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
        self.highest_score_data()
        self.pause_ins()
        

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()

    def check_fail(self):
       
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]: 
                self.game_over()



        

    def game_over(self):
        self.snake.reset()

    def draw_grass(self):
        grass_color = (167,209,61)

        for row in range(cell_number):
            if row % 2 == 0 :
                for col in range(cell_number):
                    if col %2  == 0:
                        grass_rect = pygame.Rect(col*cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (0, 0, 0))
        score_x = int((cell_size*cell_number)-60)
        score_y = int((cell_size * cell_number)-70)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        bg_rect = pygame.Rect(score_rect.left, score_rect.top,
                              score_rect.width + 10, score_rect.height)

        pygame.draw.rect(screen, (255, 127, 80), bg_rect, 2)
        screen.blit(score_surface, score_rect)

    def pause_ins(self):
        pause_instructions= " Use p to pause"
        pause_surface= game_font.render(pause_instructions, True, (0, 0, 0))
        pause_x=int((cell_size*cell_number)-770)
        pause_y=int((cell_size * cell_number)-770)
        screen.blit(pause_surface,(pause_x,pause_y))

    def highest_score_data(self):
        highest_score_data =f" highest score {database_connection.x[0]}"
        highscore_surface = game_font.render(highest_score_data,True, (0,0,0))
        high_x=int(0)
        high_y=int(730)
        screen.blit(highscore_surface,(high_x,high_y))

    def question_page(self):
        score = len(self.snake.body)-3 
        return score




        

  

class Gamestate:
    def __init__(self):
        self.state= "intro"

    
    def intro(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.state = "main_game"
          

        welcome_text = game_font.render("Welcome to snake game Press the Space bar  to start", True, (0,0,0))
        screen.fill((175, 215, 70))
        screen.blit(snake_png,(cell_size*cell_number/2 -250,cell_size*cell_number/2-250))
        screen.blit(welcome_text,(cell_size*cell_number/2 -350,cell_size*cell_number/2-290) )
        pygame.display.update()   
     


    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE:
                main_game.update()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if main_game.snake.direction.y != 1:
                        main_game.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_RIGHT:
                    if main_game.snake.direction.x != -1:
                        main_game.snake.direction = Vector2(1, 0)
                if event.key == pygame.K_DOWN:
                    if main_game.snake.direction.y != -1:
                        main_game.snake.direction = Vector2(0, 1)
                if event.key == pygame.K_LEFT:
                    if main_game.snake.direction.x != -1:
                        main_game.snake.direction = Vector2(-1, 0)
  
                if event.key == pygame.K_p:
                    self.state ="pause"

                if main_game.question_page()>1 and main_game.question_page() % 5 == 0:
                    self.state = "question_page"
                    main_game.snake.add_block()

           




        screen.fill((175, 215, 70))
        main_game.draw_elements()
        pygame.display.update()
      

         
    def pause (self):

        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False
                        self.state = "main_game"
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()
            
            
            screen.fill((175, 215, 70))
            text= "Press C to continue and Q to quit"
            text_render = game_font.render(text, True, (0,0,0))
            screen.blit(text_render,(cell_size*cell_number/2 -250,cell_size*cell_number/2-100))
            pygame.display.update() 




  
    def math_page(self):
        i = random.randint(1, 120)
        question1=mathgen.genById(i)
        user_text = ''
        x=[]
        input_rect = pygame.Rect(50,450,140,32)
        color = pygame.Color('black')
        #Function to  turn the list into string 
        def string():
            return "".join(x)

        #function to wrap long question to fit in screen 
        def wrap_text(text:str):
            word_list = []
            width = 30
            wrapped_lines = textwrap.wrap(text ,width)
            for  i  in wrapped_lines :
                word_list.append(i)
            return word_list 
        #while loop to run when answering a question
        answering = True 
        while answering:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        if str(x[-1])== answer:
                            
                            answering = False
                            game_state.state = "main_game"

                        else: 
                            database_connection.insert_scores(main_game.question_page())
                            game_state.state = "main_game"
                            answering = False
                            main_game.game_over()
                            
                            
                     
                    else:
                        user_text += event.unicode
                        x.append(user_text)
                        print(x)
                            


            
            screen.fill((175, 215, 70))
            #input field 
            text_surface = game_font.render(user_text ,True,(0,0,0))
            screen.blit(text_surface,(50,450))
            # rectangle for input 
            pygame.draw.rect(screen,color,input_rect,2)
            input_rect.w = max(100,text_surface.get_width() + 10)
            
            #question to appear
            question = str(question1[0])
            print(question)
            answer = str(question1[1])
            print(answer)

            #Variables for the question page 
            txtX, txtY = 50, 100
            wraplen = 20
            count = 0
            max_length = 8
        
            wrap_list = wrap_text(question)
            for i in wrap_list:
                if count != max_length:
                    txtY = txtY + 35
                    Mtxt = game_font.render(f"{i}", True, (0, 0, 0))
                    screen.blit(Mtxt, (txtX, txtY))
                    count += 1


            pygame.display.update() 

            
                    


    def state_manger(self):

        if self.state == 'intro':
            self.intro()

        if self.state == 'main_game':
            self.main_game()

        if self.state == 'pause':
            self.pause()
        if self.state == 'question_page':
            self.math_page()





pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode(
    (cell_size*cell_number  , cell_size*cell_number ))
     
clock = pygame.time.Clock()
apple = pygame.image.load('Graphics/apple.png').convert_alpha()
snake_png = pygame.image.load('Graphics/snake.png').convert_alpha()
game_font = pygame.font.Font('SF-Pro-Display-Bold.otf', 30)
user_text =''

main_game = MAIN()
game_state = Gamestate()
# maths =Math()


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)




while True:

    game_state.state_manger()
    


    clock.tick(60)

    
