from __future__ import annotations
import math
import pygame as pg


class ObjectBase:
    def tick(self):
        pass

    def render(self, surface: pg.surface.Surface):
        pass


class PosI:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def to_tuple(self) -> tuple[int, int]:
        return self.x, self.y


class PosF:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def to_pos_i(self) -> PosI:
        return PosI(int(self.x), int(self.y))

    def __add__(self, trg):
        return PosF(self.x + trg.x, self.y + trg.y)


class VecF(PosF):
    def __init__(self, x: float, y: float):
        super().__init__(x, y)

    def __mul__(self, trg: float):
        return VecF(self.x * trg, self.y * trg)

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def normalize(self):
        length = self.length()
        return VecF(self.x / length, self.y / length)


def main():
    v = VecF(1, 2)
    v = v * 1.5
    print(f'v*1.5 : ({v.x} {v.y})')
    pass


if __name__ == '__main__':
    main()
