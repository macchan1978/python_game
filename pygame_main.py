from __future__ import annotations

import os

import mode_play
from objects import *


def main():
    print(f'current dir : [{os.getcwd()}]')

    pg.init()
    pg.display.set_caption("minimal program")
    clock = pg.time.Clock()
    game_context.initialize()

    play_mode = mode_play.initialize()

    running = True
    while running:
        clock.tick(60)

        pad = game_context.game_pad
        pad.tick()
        if pad.button_escape:
            running = False

        play_mode.tick()
        pg.display.flip()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
