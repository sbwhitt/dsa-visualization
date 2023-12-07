import pygame
import utils.colors as colors
from graph.graph import Graph

win_size = (960, 720)

class App:
    def __init__(self) -> None:
        self.running = True
        self.surf = pygame.display.set_mode(
            win_size, pygame.SCALED | pygame.RESIZABLE | pygame.DOUBLEBUF)
        self.font = self._init_font()
        self.g = Graph()
        self.clock = pygame.time.Clock()

    def on_execute(self) -> None:
        self.on_init()

        while self.running:
            dt = self.clock.tick_busy_loop(60)
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop(dt)
            self.on_render()

        self.on_cleanup()

    def on_init(self) -> None:
        pass

    def on_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == pygame.KEYDOWN:
            self.handle_key(event.key)

    def handle_key(self, key: int) -> None:
        if key == pygame.K_ESCAPE:
            self.running = False
        elif key == pygame.K_r:
            self.g.restart_bfs()


    def on_loop(self, dt: int) -> None:
        self.g.update(dt)
        return

    def on_render(self) -> None:
        self.surf.fill(colors.BLACK)

        self.g.render(self.surf, self.font)

        pygame.display.flip()

    def on_cleanup(self) -> None:
        pass

    def _init_font(self) -> pygame.font.Font:
        pygame.font.init()
        return pygame.font.Font(pygame.font.get_default_font(), 16)
