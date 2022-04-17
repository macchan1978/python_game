from __future__ import annotations
from collections import defaultdict
import time
from objects import *
import pygame as pg
import os
import numpy as np
# define a main function


class GamePad:
    def __init__(self):
        self.keyUp = False
        self.keyRight = False
        self.keyDown = False
        self.keyLeft = False
        self.buttonSpace = False
        pass

    def processEvent(self, event: pg.Event):
        isKeyDown = event.type == pg.KEYDOWN
        if event.type in [pg.KEYDOWN, pg.KEYUP]:
            if event.key == pg.K_RIGHT:
                self.keyRight = isKeyDown
            if event.key == pg.K_LEFT:
                self.keyLeft = isKeyDown
            if event.key == pg.K_UP:
                self.keyUp = isKeyDown
            if event.key == pg.K_DOWN:
                self.keyDown = isKeyDown
            if event.key == pg.K_SPACE:
                self.buttonSpace = isKeyDown


def main():
    print(f'current dir : [{os.getcwd()}]')

    # initialize the pygame module
    pg.init()
    clock = pg.time.Clock()
    # load and set the logo
    pg.display.set_caption("minimal program")

    # create a surface on screen that has the size of 240 x 180
    screen = pg.display.set_mode((800, 600))
    myfont = pg.font.SysFont("", 25)
    dispText = myfont.render("info", True, (0, 128, 0))
    # define a variable to control the main loop
    running = True

    player = Player(pos=PosF(200, 200))

    bullets: list[Bullet] = []
    enemies: list[Enemy] = []
    tpc = [time.perf_counter(), 0]
    counter = 0

    gamePad = GamePad()
    while running:
        clock.tick(60)

        for event in pg.event.get():
            gamePad.processEvent(event)
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False

        if counter % 100 == 10:
            enemies.append(Enemy(PosF(100,100)))


        player.play(gamePad, bullets)
        player.tick()

        for b in bullets:
            b.tick()

        # 当たり判定の計算。O(n^2)だがまあ気にしない。
        for e in enemies:
            e.tick()
            for b in bullets:
                if b.isLive() and e.rect.colliderect(b.rect):
                    e.hit()
                    b.hit()
                    #TODO : 当たったら音を鳴らしたい。


        bullets = [b for b in bullets if b.isLive()]
        enemies = [e for e in enemies if e.isLive()]

        


        screen.fill((200, 200, 200))
        player.render(screen)
        for b in bullets:
            b.render(screen)
        for e in enemies:
            e.render(screen)

        # 処理時間
        tpc[1] = time.perf_counter()
        tpcMs = 1000*(tpc[1]-tpc[0])
        dispText = myfont.render(f'{tpcMs:.3g}', False, (255, 255, 255))
        tpc[0] = tpc[1]
        screen.blit(dispText, (10, 10))

        pg.display.flip()
        counter += 1


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
