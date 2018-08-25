class Scaler(object):
    """docstring for Scaler."""
    def __init__(self,pixel=1.0,metrics=1.0):
        super(Scaler, self).__init__()
        self.SetRate(pixel,metrics)
    def CalculateRate(self):
        try:
            self.PixelRate=self.pixel/self.meters
        except ZeroDivisionError:
            self.PixelRate = 1
            self.meters=1
        self.MetricRate=self.meters/self.pixel
    def SetRate(self,pixel=1,metrics=1):
        self.pixel=float(pixel)
        self.meters=float(metrics)
        self.CalculateRate()
    def ConvertPixel(self,meters):
        return int(self.PixelRate*meters)
    def ConvertMeters(self,pixel):
        return pixel*self.MetricRate
    def ConvertMeters_(self,pixels):
        b = []
        for pixel in pixels:
            b.append(self.ConvertMeters(pixel))
        return tuple(b)
    def ConvertPixels(self,meterss):
        b = []
        for meters in meterss:
            b.append(self.ConvertPixel(meters))
        return tuple(b)
    def ConvertPointListPixel(self,pointlist):
        b=[]
        for point in pointlist:
            b.append(self.ConvertPixels(point))
        return tuple(b)