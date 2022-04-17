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


class PosF:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def toPosI(self) -> PosI:
        return PosI(int(self.x), int(self.y))

    def __add__(self, trg):
        return PosF(self.x+trg.x, self.y+trg.y)


class VecF(PosF):
    def __init__(self, x: float, y: float):
        super().__init__(x, y)

    def __mul__(self, trg: float):
        return VecF(self.x*trg, self.y*trg)


def main():
    v = VecF(1, 2)
    v = v*1.5
    print(f'v*1.5 : ({v.x} {v.y})')
    pass


if __name__ == '__main__':
    main()
