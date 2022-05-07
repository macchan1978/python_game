import os
from enum import Enum, auto
import pygame as pg
from pygame.event import Event


# define a main function
class GamePad:
    def __init__(self):
        self.keyUp = False
        self.keyRight = False
        self.keyDown = False
        self.keyLeft = False
        self.buttonSpace = False
        pass

    def process_event(self, event: Event):
        is_key_down = event.type == pg.KEYDOWN
        if event.type in [pg.KEYDOWN, pg.KEYUP]:
            if event.key == pg.K_RIGHT:
                self.keyRight = is_key_down
            if event.key == pg.K_LEFT:
                self.keyLeft = is_key_down
            if event.key == pg.K_UP:
                self.keyUp = is_key_down
            if event.key == pg.K_DOWN:
                self.keyDown = is_key_down
            if event.key == pg.K_SPACE:
                self.buttonSpace = is_key_down


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


def initialize():
    global sound_mgr, game_pad
    sound_mgr = SoundManager()
    game_pad = GamePad()


def pad() -> GamePad:
    return game_pad


def sound() -> SoundManager:
    return sound_mgr
