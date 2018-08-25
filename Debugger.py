import pygame
class Debugger(object):
    """docstring for Debugger."""
    def __init__(self, SimScreen):
        super(Debugger, self).__init__()
        self.SimScreen = SimScreen
        self.TextLines = []
        self.Color = (0,255,0)
        self.Size = 10
        self.font = pygame.font.SysFont('Lucida Console', self.Size)

    def DrawTexts(self):
        for i,text in enumerate(self.TextLines):
            textsurface = self.font.render(text, True, self.Color)
            self.SimScreen.blit(textsurface,(5,(self.Size*i)+3))
    def SetText(self,Line=1,Text=""):
        try:
            self.TextLines[Line-1] = Text
        except IndexError:
            self.TextLines.append("")
            self.TextLines[Line-1] = Text
