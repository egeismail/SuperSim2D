class Vector2:
    def __init__(self,x=0.0,y=0.0,z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    def Distancefrom(self,obj):
        return ((self.x-obj.x)**2+(self.y-obj.y)**2+(self.z-obj.z)**2)**0.5
