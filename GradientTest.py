import pygame
import mathematics
from Elements import EnergyObject,D2GradientUniverse
background_color = (0,0,0)
wh = (480, 480)

screen = pygame.display.set_mode(wh)
pygame.display.set_caption('Test of Gradient Field')
running = True
EO = EnergyObject(x=128,y=128,Energy=200.0)
Universe= D2GradientUniverse(screen,wh)
print("Universe created. %sx%s"%(wh))
screen.fill(background_color)
def Waver(energy):
    if(energy!=300):
        energy+=24
    else:
        energy=0
    return energy
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    EO.Energy = Waver(EO.Energy)
    Universe.ReplaceEObject(EO)
    pygame.display.flip()