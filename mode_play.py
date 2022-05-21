import time
from enum import Enum, auto

from pygame.font import SysFont

import defs
from map_generator import GameMap
from objects import *


# noinspection PyArgumentList
class PlayResult(Enum):
    PLAYING = auto()
    END = auto()


class PlayMode:
    def __init__(self):
        self.font = pg.font.SysFont("", 25)
        self.map = GameMap()

#        self.player = Player(pos=PosF(200, 200))

        self.bullets: list[Bullet] = []
        self.enemies: list[Enemy] = []
        self.walls: list[Wall] = []
        for y, line in enumerate(self.map.map):
            for x, cell in enumerate(line):
                if cell == 0:
                    pass
                elif cell == 1:
                    self.walls.append(Wall(PosF((x+0.5)*defs.cell_width, (y+0.5)*defs.cell_width)))
                elif cell == 2:
                    self.player = Player(PosF((x+0.5)*defs.cell_width, (y+0.5)*defs.cell_width))
                elif cell == 3:
                    self.enemies.append(Enemy(PosF((x+0.5)*defs.cell_width, (y+0.5)*defs.cell_width)))

        self.tpc_start = time.perf_counter()
        self.tpc = [time.perf_counter(), 0]
        self.total_sec = 30
        self.counter = 0
        self.score = 0

    def tick(self) -> PlayResult:
        screen = game_context.get_screen()
        pad = game_context.get_pad()

        self.counter += 1

        self.player.play(self.bullets)
        self.player.tick()

        for b in self.bullets:
            b.tick()

        # 当たり判定の計算。O(n^2)だがまあ気にしない。
        for e in self.enemies:
            e.tick()
            for b in self.bullets:
                if b.is_live() and e.rect.colliderect(b.rect):
                    e.hit()
                    b.hit()
        self.score += sum(e.get_score() for e in self.enemies if e.is_destroyed())

        if any(e.is_destroyed() for e in self.enemies):
            game_context.get_sound().play(game_context.SoundType.DESTROY)

        self.bullets = [b for b in self.bullets if b.is_live()]
        self.enemies = [e for e in self.enemies if e.is_live()]

        screen.fill((200, 200, 200))
        self.player.render(screen)
        for b in self.bullets:
            b.render(screen)
        for e in self.enemies:
            e.render(screen)
        for w in self.walls:
            w.render(screen)

        # 処理時間
        self.tpc[1] = time.perf_counter()
        tpc_ms = 1000 * (self.tpc[1] - self.tpc[0])
        self.tpc[0] = self.tpc[1]
        play_sec = int(self.tpc[1] - self.tpc_start)
        rest_sec = self.total_sec - play_sec

        disp_frame_rate = self.font.render(f'{tpc_ms:.3g}', False, (255, 255, 255))
        disp_rest_sec = self.font.render(f'rest : {rest_sec}', False, (255, 255, 255))
        disp_score = self.font.render(f'Score : {self.score}', False, (255, 255, 255))
        screen.blit(disp_frame_rate, (10, 10))
        screen.blit(disp_rest_sec, (10, 30))
        screen.blit(disp_score, (10, 50))

        # TODO : ゲーム終了
        if rest_sec <= 0 or pad.button_escape:
            return PlayResult.END
        return PlayResult.PLAYING

    pass


instance: PlayMode = None


def initialize() -> PlayMode:
    global instance
    instance = PlayMode()
    return instance
