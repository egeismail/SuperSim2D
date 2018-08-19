class MFU(object):
    """docstring for MFU."""
    @staticmethod
    def CalculateInverseSquare(radius,energy):
        return energy/radius**2

class Vector3:
    def __init__(self,x=0.0,y=0.0,z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    def Distancefrom(self,obj):
        return ((self.x-obj.x)**2+(self.y-obj.y)**2+(self.z-obj.z)**2)**0.5
class Vector2:
    def __init__(self,x=0.0,y=0.0):
        self.x = float(x)
        self.y = float(y)
        self.Color = (0,0,0)
    def SetColor(self,r,g,b):
        self.Color = (r,g,b)
    def Distancefrom(self,obj):
        return ((self.x-obj.x)**2+(self.y-obj.y)**2)**0.5
class EnergyObject(object):
    """docstring for EnergyObject."""
    def __init__(self, arg):
        super(EnergyObject, self).__init__()
        self.Position = Vector2(x,y)
class D2GradientUniverse(object):
    """docstring for GradientUniverse."""
    def __init__(self, screen, wh):
        super(GradientUniverse, self).__init__()
        self.screen=screen
        self.UniverseGradient = None
        self.CreateEmptyField(0,wh[0],0,wh[1])
    def ReplaceEObject(self,Obj):

    def CreateEmptyField(self,size_s_x,size_e_x,size_s_y,size_e_y):
        for x in range(size_s_x,size_e_x):
            for y in range(size_s_y,size_e_y):
                self.UniverseGradient[x][y]=Vector2(0,0)
