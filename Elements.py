from mathematics import *
from pygame import draw,transform
from Scaler import Scaler
class NCObject(object):
    Mass=1.0
    signatureofobject=True
class NCS_Particle(NCObject):
    def __init__(self,display,pos=(1,1),Mass=1.0,Radius=5,Color=(0,0,255),scaler=Scaler(),name="Unknown"):
        self.scaler=scaler
        self.display=display
        self.Position=Vector2(self.scaler.ConvertMeters(pos[0]),self.scaler.ConvertMeters(pos[1]),scaler=scaler)
        self.Vector=Vector2(0,0)
        self.Mass = Mass
        self.Radius=Radius
        self.Color = Color
        self.pointlist = []
        self.name = name
        self.font = pygame.font.SysFont('Lucida Console', 20)
        self.textsurface = self.font.render(self.name, True, self.Color)
    def RenderName(self,name):
        self.name = name
        self.textsurface = self.font.render(text, True, self.Color)
    def DisplayObject(self):
        pos = self.Position.ReturnTuple()
        if(pos[0] < 1000000 and pos[0] > -1000000 and pos[1] < 1000000 and pos[1] > -1000000):
            radius = self.scaler.ConvertPixel(self.Radius)
            try:
                draw.circle(self.display,self.Color,pos,radius)
            except OverflowError:
                print "p",pos
                print "rad",radius
            self.display.blit(self.textsurface,(pos[0]+radius+3,pos[1]+radius+3))
            pygame.draw.lines(self.display,(255,255,255),False,self.Position.UsePadding(self.scaler.ConvertPointListPixel(self.pointlist)),1)

class NCSUniverse(object):
    def __init__(self,screen,wh):
        self.display = screen
        self.WH = wh
        self.scaler = Scaler()
        self.Objs = []
        self.FocusCenter = [0,0]
        self.Padding = (0,0)
        self.clock = pygame.time.Clock()
    def TickUniverse(self):
        self.ExecuteGravitation()
        self.TransferVectors()
        for objection in self.Objs:
            if(objection.signatureofobject):
                objection.DisplayObject()
    def UsePadding(self,points):
        nwl = []
        for point in points:
            nwl.append((self.Padding[0]+point[0],self.Padding[1]+point[1],))
        return nwl
    def CalculateFocusCenter(self):
        mx = (self.scaler.ConvertPixel(self.FocusCenter[0]),self.scaler.ConvertPixel(self.FocusCenter[1]))
        self.Padding=(self.WH[0]/2-mx[0],self.WH[1]/2-mx[1])
    def ExecuteGravitation(self):
        for from_ in self.Objs:
            for to in self.Objs:
                if(from_!=to):
                    try:
                        N = (6.67408e-11*from_.Mass*to.Mass)/(from_.Position.Distancefrom(to.Position)**2)
                        N = N/from_.Mass
                    except:
                        continue
                    Angle=from_.Position.AngleFrom(to.Position)
                    if(str(N)!="inf"):
                        from_.Vector.x += np.cos(Angle)*N
                        from_.Vector.y += np.sin(Angle)*N
                #draw.line(self.display, (255,255,255), (from_.Position.x,from_.Position.y), (from_.Position.x+from_.Vector.x*12,from_.Position.y-from_.Vector.y*12), 2)
    def TransferVectors(self):
        for item in self.Objs:
            item.Position.x+=item.Vector.x
            item.Position.y+=item.Vector.y
    def AddObject(self,Object):
        if(Object.signatureofobject):
            self.Objs.append(Object)
    def UpdateFocus(self):
            for objection in self.Objs:
                if(objection.signatureofobject):
                    self.CalculateFocusCenter()
                    objection.Position.paddingTuple=self.Padding
#----------------------------------------------------
class NC_Particle(NCObject):
    def __init__(self,display,pos=(1,1),Mass=1.0,Radius=5,Color=(0,0,255)):
        self.display=display
        self.Position=Vector2(pos[0],pos[1])
        self.Vector=Vector2(0,0)
        self.Mass = Mass
        self.Radius=Radius
        self.Color = Color
    def DisplayObject(self):
        draw.circle(self.display,self.Color,self.Position.ReturnTuple(),self.Radius)
class EnergyObject(object):
    """docstring for EnergyObject."""
    def __init__(self, x=0.0,y=0.0,Energy=300):
        self.Position = Vector2(x,y)
        self.Energy = Energy
class NCUniverse(object):
    def __init__(self,screen,wh):
        self.display = screen
        self.WH = wh
        self.Objs = []
    def TickUniverse(self):
        for objection in self.Objs:
            if(objection.signatureofobject):
                objection.DisplayObject()
        self.ExecuteGravitation()
        self.TransferVectors()
    def ExecuteGravitation(self):
        for from_ in self.Objs:
            for to in self.Objs:
                N = CalculateGravitation(from_.Mass,to.Mass,from_.Position.Distancefrom(to.Position))
                Angle=from_.Position.AngleFrom(to.Position)
                if(str(N)!="inf"):
                    from_.Vector.x+= np.cos(Angle)*N
                    from_.Vector.y+= np.sin(Angle)*N
                #draw.line(self.display, (255,255,255), (from_.Position.x,from_.Position.y), (from_.Position.x+from_.Vector.x*12,from_.Position.y-from_.Vector.y*12), 2)
    def TransferVectors(self):
        for item in self.Objs:
            item.Position.x+=item.Vector.x
            item.Position.y+=item.Vector.y
    def AddObject(self,Object):
        if(Object.signatureofobject):
            self.Objs.append(Object)
class D2GradientUniverse(object):
    """docstring for D2GradientUniverse."""
    def __init__(self, screen, wh):
        self.screen=screen
        self.UniverseGradient = []
        self.WH = wh
        self.CreateEmptyField(0,wh[0],0,wh[1])
        self.MaxEOT = 300
    def ReplaceEObject(self,Obj):
        for y in range(0,self.WH[1]):
            for x in range(0,self.WH[0]):
                energyofm = CalculateInverseSquare(Obj.Position.Distancefrom(Vector2(x,y)),Obj.Energy)
                self.screen.set_at((x,y), WavelengthToRgb(RR0(energyofm)))
    def CreateEmptyField(self,size_s_x,size_e_x,size_s_y,size_e_y):
        for x in range(size_s_x,size_e_x):
            self.UniverseGradient.append([])
            for y in range(size_s_y,size_e_y):
                self.UniverseGradient[x].append(Vector2())
def ConvertDistance(distance):
    LY = 946073000000000000.0
    AU = 14959790000000.0
    km = 1000.0
    dm = 10.0
    m = 1.0
    cm = 0.01
    mm = 0.001    
    um = 0.000001
    nm = 0.000000001
    Ang = 0.0000000001
    if(distance>LY):
        return "%.2f Light Years"%(distance/LY)
    elif(distance>AU):
        return "%.2f AU"%(distance/AU)
    elif(distance>km):
        return "%.2f kilometers"%(distance/km)
    elif(distance>dm):
        return "%.2f decameters"%(distance/dm)
    elif(distance>m):
        return "%.2f meters"%(distance/m)
    elif(distance>cm):
        return "%.2f centimeters"%(distance/cm)
    elif(distance>mm):
        return "%.2f milimeters"%(distance/mm)
    elif(distance>um):
        return "%.2f micrometers"%(distance/um)
    elif(distance>nm):
        return "%.2f nanometers"%(distance/nm)
    else:
        return "%.2f Angstrom"%(distance/Ang)
class GridBarX(object):
    """docstring for GridBarX"""
    def __init__(self, display,wh,scaler):
        super(GridBarX, self).__init__()
        self.display = display
        self.WH = wh
        self.font = pygame.font.SysFont('Lucida Console', 12)
        self.scaler = scaler
        self.textsurface = self.font.render("Grid : %s"%(ConvertDistance(self.scaler.ConvertMeters(self.WH[0]-10))), True, (255,255,255))
    def UpdateText(self):
        self.textsurface = self.font.render("Grid : %s"%(ConvertDistance(self.scaler.ConvertMeters(self.WH[0]-10))), True, (255,255,255))
    def DrawGridBar(self):
        draw.line(self.display,(255,255,255),(5,self.WH[1]-5),(self.WH[0]-5,self.WH[1]-5),5)
        self.display.blit(self.textsurface,(5,self.WH[1]-30))

class GridBarY(object):
    """docstring for GridBarX"""
    def __init__(self, display,wh,scaler):
        super(GridBarY, self).__init__()
        self.display = display
        self.WH = wh
        self.font = pygame.font.SysFont('Lucida Console', 12)
        self.scaler = scaler
        self.textsurface = self.font.render("Grid : %s"%(ConvertDistance(self.scaler.ConvertMeters(self.WH[1]-10))), True, (255,255,255))
        self.textsurface = transform.rotate(self.textsurface,90)
    def UpdateText(self):
        self.textsurface = self.font.render("Grid : %s"%(ConvertDistance(self.scaler.ConvertMeters(self.WH[1]-10))), True, (255,255,255))
        self.textsurface = transform.rotate(self.textsurface,90)
    def DrawGridBar(self):
        draw.line(self.display,(255,255,255),(self.WH[0]-5,5),(self.WH[0]-5,self.WH[1]-5),5)
        self.display.blit(self.textsurface,(self.WH[0]-30,30))