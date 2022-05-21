import defs
from .objectBase import *


class Wall(ObjectBase):
    def __init__(self, pos: PosF):
        self.rect = pg.Rect(0, 0, defs.cell_width, defs.cell_width)
        self.color = [255, 255, 255]
        self.pos = pos
        self.update_rect()

    def update_rect(self):
        self.rect.center = self.pos.to_pos_i().to_tuple()

    def render(self, surface: pg.surface.Surface):
        pg.draw.rect(surface, color=self.color, rect=self.rect)

    def update_rect(self):
        self.rect.center = self.pos.to_pos_i().to_tuple()
