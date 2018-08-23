import pygame
import Elements
background_color = (0,0,0)
wh = (1280, 720)

screen = pygame.display.set_mode(wh)
pygame.display.set_caption('Test of Physics')
running = True
Universe= Elements.NCUniverse(screen,wh)
TestObj = Elements.NC_Particle(screen,pos=(wh[0]/2,wh[1]/2),Radius=40,Mass=30)
TestObj2 = Elements.NC_Particle(screen,pos=(wh[0]/2,wh[1]/4),Radius=10,Mass=20)
TestObj3 = Elements.NC_Particle(screen,pos=(wh[0]/2,wh[1]/6),Radius=10,Mass=20)
TestObj2.Vector.x=2.3
TestObj2.Vector.y=0
TestObj3.Vector.x=-0.2

Universe.AddObject(TestObj)
Universe.AddObject(TestObj2)
Universe.AddObject(TestObj3)
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
