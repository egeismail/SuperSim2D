import pygame
import mathematics
background_color = (0,0,0)
wh = (480, 480)

screen = pygame.display.set_mode(wh)
pygame.display.set_caption('Test of Gradient Field')
running = True
EO = mathematics.EnergyObject(0,0,300)
Universe= mathematics.D2GradientUniverse(screen,wh)
print("Universe created. %sx%s"%(wh))
screen.fill(background_color)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.circle(screen,(255,0,0),(50,50),10,1)
    Universe.ReplaceEObject(EO)
    pygame.display.flip()