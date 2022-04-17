from __future__ import annotations
from collections import defaultdict
from objects import *
import pygame as pg
import os
import numpy as np
# define a main function


def main():
    print(f'current dir : [{os.getcwd()}]')

    # initialize the pygame module
    pg.init()
    clock = pg.time.Clock()
    # load and set the logo
    pg.display.set_caption("minimal program")

    # create a surface on screen that has the size of 240 x 180
    screen = pg.display.set_mode((800, 600))

    # define a variable to control the main loop
    running = True
    counter = 0
    counterAdd = 5
    speed = 5

    player = Player(pos=PosF(200, 200))

    vec = np.array((0, 0))
    bullets: list[Bullet] = []
    vec = None
    while running:
        shot = False
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    vec = np.array((speed, 0))
                if event.key == pg.K_LEFT:
                    vec = np.array((-speed, 0))
                if event.key == pg.K_UP:
                    vec = np.array((0, -speed))
                if event.key == pg.K_DOWN:
                    vec = np.array((0, speed))
                if event.key == pg.K_SPACE:
                    shot = True
                if event.key == pg.K_ESCAPE:
                    running = False
            if event.type == pg.KEYUP:
                if event.key in [pg.K_RIGHT, pg.K_LEFT, pg.K_UP, pg.K_DOWN]:
                    vec = np.array((0, 0))
                    vec = None

        counter += counterAdd
        if counter > 500 or counter < 0:
            counterAdd = -counterAdd
        print(f'counter : {counter}')

        if vec is not None:
            player.move(VecF(vec[0], vec[1]))
        if shot:
            player.shot(bullets)
        player.tick()

        for b in bullets:
            b.tick()
        bullets = [b for b in bullets if b.isLive()]

        screen.fill((255, 255, 255))
        # MEMO : rectは半透明を使えない。
        pg.draw.rect(screen, color=(128, 0, 0), rect=[
                     10, 10, 100+counter, 50+counter])
        player.render(screen)
        for b in bullets:
            b.render(screen)
        # pg.draw.ellipse(screen, color=(100, 100, 255),
        #                 rect=[pos[0], pos[1], 30, 30])
        pg.display.flip()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
