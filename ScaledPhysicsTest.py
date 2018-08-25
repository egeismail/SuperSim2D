import pygame
import Elements
from Debugger import Debugger
def CreateOrbitSpeed(mass,distance):
    return ((6.67408e-11*mass)/distance)**0.5
pygame.font.init()
background_color = (0,0,0)
wh = (1600, 1000)
AU = 1500000000000
screen = pygame.display.set_mode(wh)
pygame.display.set_caption('Test of Scaled Physics')
running = True
Universe= Elements.NCSUniverse(screen,wh)
GBX = Elements.GridBarX(screen,wh,Universe.scaler)
GBY = Elements.GridBarY(screen,wh,Universe.scaler)
mscaler = AU/8000/wh[0]
Universe.scaler.SetRate(1,mscaler)
print("Size : X: %.1fm - Y: %1.fm"%(Universe.scaler.ConvertMeters(wh[0]),Universe.scaler.ConvertMeters(wh[1])))
TestObj = Elements.NCS_Particle(screen,pos=(0,0),Radius=6371000,Mass=5.9736e+24,scaler=Universe.scaler,name="Dunya",Color=Elements.WavelengthToRgb(720))
TestObj2 = Elements.NCS_Particle(screen,pos=(0,-Universe.scaler.ConvertPixel(362600000)),Radius=1737000,Mass=7.342e+22,scaler=Universe.scaler,name="Ay",Color=Elements.WavelengthToRgb(520))
#TestObj3 = Elements.NCS_Particle(screen,pos=(Universe.scaler.ConvertPixel(152100000000),0),Radius=696392000,Mass=1.9885e+30,scaler=Universe.scaler)
TestObj4 = Elements.NCS_Particle(screen,pos=(0,-Universe.scaler.ConvertPixel(6371000+403000)),Radius=100,Mass=419725,scaler=Universe.scaler,name="ISS",Color=Elements.WavelengthToRgb(480))
Universe.FocusCenter = [0,-6371000-340000]#Universe.FocusCenter = [152100000000,0]
Debug = Debugger(screen)
TestObj2.Vector.x=1022# CreateOrbitSpeed(7.342e+22,100400000)
TestObj2.Vector.y=0# CreateOrbitSpeed(7.342e+22,100400000)
#TestObj.Vector.y=29.78*1000
TestObj4.Vector.x=7.67e+3#CreateOrbitSpeed(7.342e+22,6711000)*7.2
Universe.AddObject(TestObj)
Universe.AddObject(TestObj2)
Universe.AddObject(TestObj4)
#Universe.AddObject(TestObj3)
print("Universe created. %sx%s"%(wh))
bg = pygame.transform.scale(pygame.image.load("nebula.jpg"), (wh[0], wh[1]))
da = None
dd = None
Focus = None
Universe.UpdateFocus()
for item in Universe.Objs:
        item.pointlist.append((item.Position.x,item.Position.y))         
while running:
    keys = pygame.key.get_pressed()
    if(keys[pygame.K_a]):
            Universe.FocusCenter[0] -= mscaler**1.4
            Universe.UpdateFocus()
    if(keys[pygame.K_w]):
            Universe.FocusCenter[1] -= mscaler**1.4
            Universe.UpdateFocus()
    if(keys[pygame.K_s]):
            Universe.FocusCenter[1] += mscaler**1.4
            Universe.UpdateFocus()
    if(keys[pygame.K_d]):
            Universe.FocusCenter[0] += mscaler**1.4
            Universe.UpdateFocus()
    if(keys[pygame.K_UP]):
        mscaler += mscaler**1.001
        Universe.scaler.SetRate(1,mscaler)
        Universe.UpdateFocus()
        GBX.UpdateText()
        GBY.UpdateText()
    elif(keys[pygame.K_DOWN]):
        mscaler -= mscaler*0.98
        Universe.scaler.SetRate(1,mscaler)
        Universe.UpdateFocus()
        GBX.UpdateText()
        GBY.UpdateText()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if (event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_UP):
                mscaler += mscaler*1.3
                Universe.scaler.SetRate(1,mscaler)
                Universe.UpdateFocus()
                GBX.UpdateText()
                GBY.UpdateText()
            elif(event.key == pygame.K_DOWN):
                mscaler -= mscaler*0.8
                Universe.scaler.SetRate(1,mscaler)
                Universe.UpdateFocus()
                GBX.UpdateText()
                GBY.UpdateText()
            elif(event.key == pygame.K_RIGHT):
                print("TimeLapse 100000 ticks")
                for i in range(0,100000):
                    Universe.ExecuteGravitation()
                    Universe.TransferVectors()
            elif(event.key == pygame.K_LEFT):
                if(Focus):
                    print("ok")
                    index = Universe.Objs.index(Focus)
                    print index,len(Universe.Objs)
                    if(index == len(Universe.Objs)-1):
                        Focus = None
                    else:
                        Focus = Universe.Objs[index+1]
                else:
                    Focus = Universe.Objs[0]
    for item in Universe.Objs:
        item.pointlist.append((item.Position.x,item.Position.y))
        if(len(item.pointlist)>1000):
            del item.pointlist[0]
    screen.blit(bg, (0, 0))
    #screen.fill(background_color)
    #Code Of Draw
    #print(TestObj2.Position.ReturnTuple())
    #print(TestObj.Positionself.ReturnTuple())
    #for i in range(0,1000): # Timelapse
    #    Universe.ExecuteGravitation()
    #    Universe.TransferVectors()
    Universe.TickUniverse()
    Debug.SetText(Line=1,Text="FPS : %s"%(Universe.clock.get_fps()))
    Debug.SetText(Line=2,Text="Scale : %sp=%sm"%(Universe.scaler.pixel,Universe.scaler.meters))
    Debug.SetText(Line=3,Text="Size : X: %s m- Y: %s m"%(Universe.scaler.ConvertMeters(wh[0]),Universe.scaler.ConvertMeters(wh[1])))
    Debug.DrawTexts()
    if(Focus):
        Universe.FocusCenter = [Focus.Position.x,Focus.Position.y]
        Universe.UpdateFocus()
    #Code Of Draw
    GBX.DrawGridBar()
    GBY.DrawGridBar()

    pygame.display.flip()
    Universe.clock.tick(20)

                
                

