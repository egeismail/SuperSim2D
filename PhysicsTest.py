import pygame
import Elements
background_color = (0,0,0)
wh = (1280, 720)

screen = pygame.display.set_mode(wh)
pygame.display.set_caption('Test of Physics')
running = True
Universe= Elements.NCUniverse(screen,wh)
TestObj = Elements.NC_Particle(screen,pos=(wh[0]/2,wh[1]/2),Radius=10,Mass=100)
TestObj2 = Elements.NC_Particle(screen,pos=(wh[0]/3,wh[1]/3),Radius=5)
TestObj2.Vector.x=0.3
Universe.AddObject(TestObj)
Universe.AddObject(TestObj2)
print("Universe created. %sx%s"%(wh))
while running:
    screen.fill(background_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Code Of Draw
    Universe.TickUniverse()
    TestObj.Position.x=wh[0]/2
    TestObj.Position.y=wh[1]/2
    
    #Code Of Draw
    pygame.display.flip()