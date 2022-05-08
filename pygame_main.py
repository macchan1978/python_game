from __future__ import annotations

import os
from enum import Enum, auto

import mode_play
import mode_title
from objects import *


# noinspection PyArgumentList
class ModeType(Enum):
    TITLE = auto()
    PLAY = auto()


def main():
    print(f'current dir : [{os.getcwd()}]')

    pg.init()
    pg.display.set_caption("minimal program")
    clock = pg.time.Clock()
    game_context.initialize()

    play_mode: mode_play.PlayMode = None
    title_mode = mode_title.initialize()
    current_mode = ModeType.TITLE

    running = True
    while running:
        clock.tick(60)

        pad = game_context.game_pad
        pad.tick()

        # if pad.button_escape:
        #     running = False

        if current_mode == ModeType.TITLE:
            selected_item = title_mode.tick()
            if selected_item == mode_title.MenuType.EXIT:
                running = False
            elif selected_item == mode_title.MenuType.PLAY:
                play_mode = mode_play.initialize()
                current_mode = ModeType.PLAY
        elif current_mode == ModeType.PLAY:
            result = play_mode.tick()
            if result == mode_play.PlayResult.END:
                current_mode = ModeType.TITLE
        pg.display.flip()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
