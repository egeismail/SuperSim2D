import numpy as np
import pygame
def CalculateInverseSquare(distance,energy):
    try:
        return energy/(distance/100)**2
    except ZeroDivisionError:
        return energy
def WavelengthToRgb(wavelength, gamma=0.8):
    wavelength = float(wavelength)
    if wavelength >= 380 and wavelength <= 440:
        attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
        R = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
        G = 0.0
        B = (1.0 * attenuation) ** gamma
    elif wavelength >= 440 and wavelength <= 490:
        R = 0.0
        G = ((wavelength - 440) / (490 - 440)) ** gamma
        B = 1.0
    elif wavelength >= 490 and wavelength <= 510:
        R = 0.0
        G = 1.0
        B = (-(wavelength - 510) / (510 - 490)) ** gamma
    elif wavelength >= 510 and wavelength <= 580:
        R = ((wavelength - 510) / (580 - 510)) ** gamma
        G = 1.0
        B = 0.0
    elif wavelength >= 580 and wavelength <= 645:
        R = 1.0
        G = (-(wavelength - 645) / (645 - 580)) ** gamma
        B = 0.0
    elif wavelength >= 645 and wavelength <= 750:
        attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
        R = (1.0 * attenuation) ** gamma
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0
    R *= 255
    G *= 255
    B *= 255
    if(wavelength>645):
        R=255
    return (abs(int(R)),abs(int(G)),abs(int(B)))
def RR0(energy):
        return energy*1.336+380
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
    def Distancefrom(self,obj):
        return ((self.x-obj.x)**2+(self.y-obj.y)**2)**0.5
    def AngleFrom(self,obj):
        return np.arctan2(obj.x,obj.y)
class EnergyObject(object):
    """docstring for EnergyObject."""
    def __init__(self, x=0.0,y=0.0,Energy=300):
        super(EnergyObject, self).__init__()
        self.Position = Vector2(x,y)
        self.Energy = Energy
class D2GradientUniverse(object):
    """docstring for D2GradientUniverse."""
    def __init__(self, screen, wh):
        super(D2GradientUniverse, self).__init__()
        self.screen=screen
        self.UniverseGradient = []
        self.WH = wh
        self.CreateEmptyField(0,wh[0],0,wh[1])
        self.MaxEOT = 300
    def ReplaceEObject(self,Obj):
        for x in range(0,self.WH[0]):
            for y in range(0,self.WH[1]):
                energyofm = CalculateInverseSquare(Obj.Position.Distancefrom(Vector2(x,y)),Obj.Energy)                
                #sx = np.cos(energyofm)
                #sy = np.sin(energyofm)
                #self.UniverseGradient[x][y].x = np.cos(energyofm)
                #self.UniverseGradient[x][y].y = np.sin(energyofm)
                color = WavelengthToRgb(RR0(energyofm))
                self.screen.set_at((x,y), color)
    def CreateEmptyField(self,size_s_x,size_e_x,size_s_y,size_e_y):
        for x in range(size_s_x,size_e_x):
            self.UniverseGradient.append([])
            for y in range(size_s_y,size_e_y):
                self.UniverseGradient[x].append(Vector2())
