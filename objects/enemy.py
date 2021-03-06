from __future__ import annotations

from .objectBase import *


class Enemy(ObjectBase):
    def __init__(self, pos: PosF):
        self.score = 100
        self.counter = 0
        self.shotCount = 0
        self.color = [100, 250, 255]
        self.life = 5
        self.pos = pos
        self.speed = 0.1
        self.dirVec = VecF(0, 1)
        self.moveVec = VecF(0, self.speed)
        # 当たり判定.
        self.rect = pg.Rect(0, 0, 30, 30)
        self.rectDir = pg.Rect(0, 0, 10, 10)
        self.update_rect()
        pass

    def update_rect(self):
        self.rect.center = self.pos.to_pos_i().to_tuple()

    def tick(self):
        self.pos += self.moveVec
        self.update_rect()
        self.counter += 1

    def hit(self):
        self.life -= 1

    def is_live(self):
        return self.life > 0 and self.counter < 1000

    def is_destroyed(self):
        return self.life <= 0

    def get_score(self):
        return self.score

    def render(self, surface: pg.surface.Surface):
        pg.draw.rect(surface, color=self.color, rect=self.rect)
        dir_rect_pos = self.pos + self.dirVec * 15
        self.rectDir.center = dir_rect_pos.to_pos_i().to_tuple()
        pg.draw.rect(surface, (255, 255, 255), rect=self.rectDir)

        pass

    pass
