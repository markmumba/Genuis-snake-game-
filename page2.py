import pygame,sys
from mathgenerator import mathgen
import random


pygame.init()
clock=pygame.time.Clock()
screen = pygame.display.set_mode([800,800])
base_font = pygame.font.Font('SourceSansPro-SemiBold.ttf', 35)
user_text = ''
x= []


question1= "What is 10 + 10"
answer1 = "20"
question2 = "what is GCD of 30 and 10"
answer2  = 10

def string():
    return "".join(x)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            if event.key == pygame.K_RETURN:
                x.append(user_text)
                if string() == answer:
                    question=question2
                    answer =answer2
                    print(True)

            else:
                user_text += event.unicode
                


    
    screen.fill((175, 215, 70))
    #input field 
    text_surface = base_font.render(user_text,True,(0,0,0))
    screen.blit(text_surface,(300,300))
   
    #question to appear
    question = question1
    answer = answer1
    question_surface = base_font.render(question, True, (112,102,102))
    screen.blit(question_surface, (200,200))
   

    
    

    pygame.display.update()
    clock.tick(60)

