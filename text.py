import pygame,sys

import random
import textwrap


pygame.init()
clock=pygame.time.Clock()
screen = pygame.display.set_mode([800,800])
base_font = pygame.font.Font('SourceSansPro-SemiBold.ttf', 35)

def wrap_text(text:str):
    word_list = []
    width = 50
    wrapped_lines = textwrap.wrap(text ,width)
    for  i  in wrapped_lines :
        word_list.append(i)
    return word_list 

# while True:
    
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()



#         screen.fill((175, 215, 70))

#         text = "Try things that may not work.You must not let anyone define your limits  because of where you come from. Your only limit is your soul.Only the fearless can be great the ratatouille"
#         text_wrapped  = wrap_text(text)
    
#         for i in text_wrapped:
#             text_surface= base_font.render(i,True,(0,0,0))   
#             print(i) 
#         screen.blit(text_surface, (200,300))
#         pygame.display.update()
#         clock.tick(60)




font = pygame.font.SysFont("Times New Roman, Arial", 20, bold=True)
your_text = "Try things that may not work.You must not let anyone define your limits  because of where you come from. Your only limit is your soul.Only the fearless can be great the ratatouille"
txtX, txtY = 100, 100
wraplen = 20
count = 0
max = 4

while True:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


       
        wrap_list = wrap_text(your_text)
        # Draw one line at a time further down the screen
        for i in wrap_list:
            if count != max:
                txtY = txtY + 35
                Mtxt = font.render(f"{i}", True, (255, 255, 255))
                screen.blit(Mtxt, (txtX, txtY))
                count += 1
            

        # Update All Window and contents
        pygame.display.update()
        clock.tick(60)
