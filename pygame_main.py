from __future__ import annotations

import os
import time

from objects import *


# define a main function


class GamePad:
    def __init__(self):
        self.keyUp = False
        self.keyRight = False
        self.keyDown = False
        self.keyLeft = False
        self.buttonSpace = False
        pass

    def process_event(self, event: pg.Event):
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


def main():
    print(f'current dir : [{os.getcwd()}]')

    # initialize the pygame module
    pg.init()
    clock = pg.time.Clock()
    # load and set the logo
    pg.display.set_caption("minimal program")

    # create a surface on screen that has the size of 240 x 180
    screen = pg.display.set_mode((800, 600))
    my_font = pg.font.SysFont("", 25)
    # define a variable to control the main loop
    running = True

    the_player = Player(pos=PosF(200, 200))

    bullets: list[Bullet] = []
    enemies: list[Enemy] = []
    tpc = [time.perf_counter(), 0]
    counter = 0

    game_pad = GamePad()
    while running:
        clock.tick(60)

        for event in pg.event.get():
            game_pad.process_event(event)
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False

        if counter % 100 == 10:
            enemies.append(Enemy(PosF(100, 100)))

        the_player.play(game_pad, bullets)
        the_player.tick()

        for b in bullets:
            b.tick()

        # 当たり判定の計算。O(n^2)だがまあ気にしない。
        for e in enemies:
            e.tick()
            for b in bullets:
                if b.is_live() and e.rect.colliderect(b.rect):
                    e.hit()
                    b.hit()
                    # TODO : 当たったら音を鳴らしたい。

        bullets = [b for b in bullets if b.is_live()]
        enemies = [e for e in enemies if e.is_live()]

        screen.fill((200, 200, 200))
        the_player.render(screen)
        for b in bullets:
            b.render(screen)
        for e in enemies:
            e.render(screen)

        # 処理時間
        tpc[1] = time.perf_counter()
        tpc_ms = 1000 * (tpc[1] - tpc[0])
        disp_text = my_font.render(f'{tpc_ms:.3g}', False, (255, 255, 255))
        tpc[0] = tpc[1]
        screen.blit(disp_text, (10, 10))

        pg.display.flip()
        counter += 1


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
