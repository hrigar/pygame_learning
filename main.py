import pygame
from sys import exit
pygame.init()

screen = pygame.display.set_mode((600,420))
pygame.display.set_caption('madman')
Clock = pygame.time.Clock()

# test_surface = pygame.Surface((100,200))
# test_surface.fill('BLUE')

# img_surface = pygame.image.load('download (10).jpg')

back_surface = pygame.image.load('asset/images/up.jpg')
down_surface = pygame.image.load('asset/images/down.jpg')
charcater = pygame.image.load('asset/images/char.png')
char_x_pos = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(back_surface,(0,0))      
    screen.blit(down_surface,(0,327))      
    screen.blit(charcater,(char_x_pos,240))  
    char_x_pos += 5    
    if char_x_pos == 600:
        char_x_pos = 0
    pygame.display.update()

    Clock.tick(60)