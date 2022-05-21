import os
from enum import Enum, auto
import pygame as pg
from pygame.event import Event
from pygame.surface import Surface


class GamePad:
    button_escape: bool
    button_space: bool
    key_left: bool
    key_down: bool
    key_right: bool
    key_up: bool

    def __init__(self):
        self.key_up = False
        self.key_right = False
        self.key_down = False
        self.key_left = False
        self.button_space = False
        self.button_escape = False
        pass

    def tick(self):
        for event in pg.event.get():
            self.process_event(event)

    def process_event(self, event: Event):

        is_key_down = event.type == pg.KEYDOWN
        if event.type in [pg.KEYDOWN, pg.KEYUP]:
            if event.key == pg.K_RIGHT:
                self.key_right = is_key_down
            if event.key == pg.K_LEFT:
                self.key_left = is_key_down
            if event.key == pg.K_UP:
                self.key_up = is_key_down
            if event.key == pg.K_DOWN:
                self.key_down = is_key_down
            if event.key == pg.K_SPACE:
                self.button_space = is_key_down
            if event.key == pg.K_ESCAPE:
                self.button_escape = is_key_down


class SoundType(Enum):
    HIT = auto()
    DESTROY = auto()


class SoundManager:
    def __init__(self):
        pg.mixer.init(11025)  # raises exception on fail
        main_dir = os.path.split(os.path.abspath(__file__))[0]
        sound_path = os.path.join(main_dir, "resources", "boom.wav")

        self.sounds = {SoundType.DESTROY: pg.mixer.Sound(sound_path)}

    def play(self, t: SoundType):
        self.sounds[t].play()
        pass

    pass


sound_mgr: SoundManager
game_pad: GamePad
screen: Surface


def initialize():
    global sound_mgr, game_pad, screen
    sound_mgr = SoundManager()
    game_pad = GamePad()
    screen = pg.display.set_mode((800, 600))


def get_pad() -> GamePad:
    return game_pad


def get_sound() -> SoundManager:
    return sound_mgr


def get_screen() -> Surface:
    return screen
