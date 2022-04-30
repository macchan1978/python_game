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
        self.update_rect()
        self.counter += 1

    def is_live(self):
        return self.life > 0 and self.counter < 30

    def hit(self):
        self.life -= 1

    # TODO : そのうち共通化
    def update_rect(self):
        pos_i = self.pos.to_pos_i()
        self.rect.center = (pos_i.x, pos_i.y)

    def render(self, surface: pg.surface.Surface):
        pg.draw.rect(surface, color=self.color, rect=self.rect)
