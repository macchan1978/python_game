from __future__ import annotations
import pygame as pg
import numpy as np
from .objectBase import *
from .bullet import *
from pygame_main import GamePad


class Player(ObjectBase):
    def __init__(self, pos: PosF):
        self.counter = 0
        self.shotCount = 0
        self.color = [100, 100, 255]
        self.pos = pos
        self.speed = 5
        self.dirVec = VecF(1, 0)
        self.moveVec = VecF(0, 0)
        self.rect = pg.Rect(0, 0, 30, 30)
        self.rectDir = pg.Rect(0, 0, 10, 10)
        self.updateRect()

    def play(self, pad: GamePad, bullets: list[Bullet]):
        speed = self.speed
        if pad.keyUp:
            self.setMoveVec(VecF(0, -speed))
        if pad.keyRight:
            self.setMoveVec(VecF(speed, 0))
        if pad.keyDown:
            self.setMoveVec(VecF(0, speed))
        if pad.keyLeft:
            self.setMoveVec(VecF(-speed, 0))
        if pad.buttonSpace:
            self.shot(bullets)
        pass

    def updateRect(self):
        self.rect.center = self.pos.toPosI().toTuple()

    def setMoveVec(self, vec: VecF):
        self.moveVec = vec
        self.dirVec = vec.normalize()

    def shot(self, bullets: list[Bullet]):
        if self.shotCount + 10 > self.counter:
            return
        bullets.append(Bullet(self.pos, self.dirVec*2*self.speed))
        self.shotCount = self.counter

        pass

    def tick(self):
        self.pos += self.moveVec
        self.moveVec = VecF(0, 0)
        self.updateRect()
        self.counter += 1

    def render(self, surface: pg.surface.Surface):
        pg.draw.rect(surface, color=self.color, rect=self.rect)
        dirRectPos = self.pos + self.dirVec*15
        self.rectDir.center = dirRectPos.toPosI().toTuple()
        pg.draw.rect(surface, (255, 255, 255), rect=self.rectDir)

        pass
