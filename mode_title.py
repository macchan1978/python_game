from enum import Enum, auto

import pygame as pg

import game_context


# noinspection PyArgumentList
class MenuType(Enum):
    EXIT = auto()
    PLAY = auto()
    NONE = auto()


class TitleMode:
    def __init__(self):
        self.font = pg.font.SysFont("", 25)
        self.menus = [(MenuType.PLAY, 'Play'), (MenuType.EXIT, 'Exit')]
        self.menu_index = 0
        self.counter = 0
        self.counter_disable = 0
        pass

    def tick(self) -> MenuType:
        self.counter += 1
        pad = game_context.get_pad()
        menu_move = 0

        if self.counter >= self.counter_disable:
            if pad.key_up:
                menu_move -= 1
            if pad.key_down:
                menu_move += 1
            if menu_move != 0:
                self.counter_disable = self.counter + 10
            self.menu_index = (self.menu_index + menu_move + len(self.menus)) % len(self.menus)

        screen = game_context.get_screen()
        screen.fill((0, 0, 0))
        for i, item in enumerate(self.menus):
            header = '> ' if i == self.menu_index else '  '
            disp = self.font.render(header + item[1], False, (255, 255, 255))
            screen.blit(disp, (100, 100 + 50 * i))

        if pad.button_space:
            return self.menus[self.menu_index][0]

        return MenuType.NONE


instance: TitleMode = None


def initialize() -> TitleMode:
    global instance
    instance = TitleMode()
    return instance


pass
