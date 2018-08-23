from mathematics import *
from pygame import draw
class NCObject(object):
    Mass=1.0
    signatureofobject=True
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
