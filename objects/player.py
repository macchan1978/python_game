from __future__ import annotations

from pygame_main import GamePad
from .bullet import *


class Player(ObjectBase):
    def __init__(self, pos: PosF):
        self.counter = 0
        self.shotCount = 0
        self.color = [100, 100, 255]
        self.pos = pos
        self.speed = 5
        self.dirVec = VecF(1, 0)
        self.moveVec = VecF(0, 0)
        # 当たり判定.
        self.rect = pg.Rect(0, 0, 30, 30)
        self.rectDir = pg.Rect(0, 0, 10, 10)
        self.update_rect()

    def play(self, pad: GamePad, bullets: list[Bullet]):
        if pad.buttonSpace:
            self.shot(bullets)

        angle = self.calc_move_angle(pad)
        if not angle[0]:
            return
        rad = math.radians(angle[1])
        vx, vy = (self.speed * math.cos(rad), self.speed * math.sin(rad))
        self.set_move_vec(VecF(vx, vy))

    @staticmethod
    def calc_move_angle(pad: GamePad) -> tuple[bool, float]:
        if pad.keyUp and pad.keyRight:
            return True, -45.0
        if pad.keyRight and pad.keyDown:
            return True, 45.0
        if pad.keyDown and pad.keyLeft:
            return True, 135.0
        if pad.keyLeft and pad.keyUp:
            return True, -135.0
        if pad.keyUp:
            return True, -90.0
        if pad.keyRight:
            return True, 0.0
        if pad.keyDown:
            return True, 90.0
        if pad.keyLeft:
            return True, 180.0
        if pad.keyUp:
            return True, -90
        return False, 0

    def update_rect(self):
        self.rect.center = self.pos.to_pos_i().to_tuple()

    def set_move_vec(self, vec: VecF):
        self.moveVec = vec
        self.dirVec = vec.normalize()

    def shot(self, bullets: list[Bullet]):
        if self.shotCount + 10 > self.counter:
            return
        bullets.append(Bullet(self.pos, self.dirVec * 2 * self.speed))
        self.shotCount = self.counter

        pass

    def tick(self):
        self.pos += self.moveVec
        self.moveVec = VecF(0, 0)
        self.update_rect()
        self.counter += 1

    def render(self, surface: pg.surface.Surface):
        pg.draw.rect(surface, color=self.color, rect=self.rect)
        dir_rect_pos = self.pos + self.dirVec * 15
        self.rectDir.center = dir_rect_pos.to_pos_i().to_tuple()
        pg.draw.rect(surface, (255, 255, 255), rect=self.rectDir)

        pass
