from __future__ import annotations
import pygame as pg
from .objectBase import *
from .bullet import *


class Player(ObjectBase):
    def __init__(self, pos: PosF):
        self.color = [100, 100, 255]
        self.pos = pos
        self.dirVec = VecF(1, 0)
        self.moveVec = VecF(0, 0)
        self.rect = pg.Rect(0, 0, 30, 30)
        self.updateRect()

    def updateRect(self):
        posI = self.pos.toPosI()
        self.rect.center = (posI.x, posI.y)

    def move(self, vec: VecF):
        self.moveVec = self.dirVec = vec

    def shot(self, bullets: list[Bullet]):
        bullets.append(Bullet(self.pos, self.dirVec*2))
        pass

    def tick(self):
        self.pos += self.moveVec
        self.moveVec = VecF(0, 0)
        self.updateRect()

    def render(self, surface: pg.surface.Surface):
        pg.draw.rect(surface, color=self.color, rect=self.rect)

        pass
