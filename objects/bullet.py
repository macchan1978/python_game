import pygame as pg
from .objectBase import *


class Bullet(ObjectBase):
    def __init__(self, pos: PosF, vec: VecF):
        self.color = [255, 0, 0]
        self.pos = pos
        self.vec = vec
        self.rect = pg.Rect(0, 0, 10, 10)
        self.counter = 0
        self.life = 1

    def tick(self):
        self.pos += self.vec
        self.updateRect()
        self.counter += 1

    def isLive(self):
        return self.life >0 and self.counter < 30

    def hit(self):
        self.life -= 1

    #TODO : そのうち共通化
    def updateRect(self):
        posI = self.pos.toPosI()
        self.rect.center = (posI.x, posI.y)

    def render(self, surface: pg.surface.Surface):
        pg.draw.rect(surface, color=self.color, rect=self.rect)
