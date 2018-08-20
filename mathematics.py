import numpy as np
import pygame
def CalculateInverseSquare(distance,energy):
    try:
        return energy/(distance/100)**2
    except ZeroDivisionError:
        return energy
def CalculateGravitation(mass1,mass2,distance):
    return CalculateInverseSquare(distance,mass1*mass2*6.67408e-5)
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
    def Distancefrom(self,obj,Scale=1):
        return (((self.x-obj.x)**2+(self.y-obj.y)**2+(self.z-obj.z)**2)**0.5)/Scale
class Vector2:
    def __init__(self,x=0.0,y=0.0):
        self.x = float(x)
        self.y = float(y)
        self.Color = (0,0,0)
    def ReturnTuple(self):
        return (int(self.x),int(self.y))
    def Distancefrom(self,obj,Scale=1):
        return (((self.x-obj.x)**2+(self.y-obj.y)**2)**0.5)/Scale
    def AngleFrom(self,obj):
        return np.arctan2(obj.x,obj.y)
