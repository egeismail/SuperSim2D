import pygame
import mathematics
background_colour = (0,0,0)
wh = (1280, 720)

screen = pygame.display.set_mode(wh)
pygame.display.set_caption('Test of Gradient Field')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(background_colour)
    pygame.display.flip()
    
