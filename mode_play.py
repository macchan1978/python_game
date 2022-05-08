import time

from pygame.font import SysFont

from objects import *


class PlayMode:
    def __init__(self):
        self.font = pg.font.SysFont("", 25)
        # define a variable to control the main loop
        self.running = True

        self.player = Player(pos=PosF(200, 200))

        self.bullets: list[Bullet] = []
        self.enemies: list[Enemy] = []
        self.tpc_start = time.perf_counter()
        self.tpc = [time.perf_counter(), 0]
        self.total_sec = 30
        self.counter = 0
        self.score = 0

    def tick(self):
        screen = game_context.get_screen()

        self.counter += 1
        if self.counter % 100 == 10:
            self.enemies.append(Enemy(PosF(100, 100)))

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
        if rest_sec <= 0:
            pass
        pass

    pass


instance: PlayMode = None


def initialize() -> PlayMode:
    global instance
    instance = PlayMode()
    return instance
