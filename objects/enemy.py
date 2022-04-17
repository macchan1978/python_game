from __future__ import annotations
import pygame as pg
import numpy as np
from .objectBase import *


class Enemy(ObjectBase):
    def __init__(self, pos:PosF):
        self.counter = 0
        self.shotCount = 0
        self.color = [100, 250, 255]
        self.life = 5
        self.pos = pos
        self.speed = 1
        self.dirVec = VecF(1, 0)
        self.moveVec = VecF(1, 0)
        # 当たり判定.
        self.rect = pg.Rect(0, 0, 30, 30)
        self.rectDir = pg.Rect(0, 0, 10, 10)
        self.updateRect()
        pass

    def updateRect(self):
        self.rect.center = self.pos.toPosI().toTuple()

    def tick(self):
        self.pos += self.moveVec
        self.updateRect()
        self.counter += 1

    def hit(self):
        self.life -=1

    def isLive(self):
        return self.life>0 and self.counter < 500

    def render(self, surface: pg.surface.Surface):
        pg.draw.rect(surface, color=self.color, rect=self.rect)
        dirRectPos = self.pos + self.dirVec*15
        self.rectDir.center = dirRectPos.toPosI().toTuple()
        pg.draw.rect(surface, (255, 255, 255), rect=self.rectDir)

        pass
    pass


