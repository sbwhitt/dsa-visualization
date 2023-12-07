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

    def on_execute(self) -> None:
        self.on_init()

        while self.running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()

        self.on_cleanup()

    def on_init(self) -> None:
        pass

    def on_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.running = False

    def on_loop(self) -> None:
        #if not self.g.bfs_done: self.g.update_bfs()
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
