import pygame
import utils.colors as colors
from utils.events import *
from graph.graph import Graph
from ui.ui import UI

win_size = (960, 720)

class App:
    def __init__(self) -> None:
        self.running = True
        self.surf = pygame.display.set_mode(
            win_size, pygame.SCALED | pygame.RESIZABLE | pygame.DOUBLEBUF)
        self.font = self._init_font()
        self.g = Graph()
        self.clock = pygame.time.Clock()
        self.ui = UI(win_size)

    def on_execute(self) -> None:
        self.on_init()

        while self.running:
            dt = self.clock.tick_busy_loop(60)
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
        elif event.type == pygame.KEYDOWN:
            self.handle_key(event.key)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.handle_mouse()
        elif event.type == BFS_START:
            self.g.set_bfs()
        elif event.type == DFS_START:
            self.g.set_dfs()
        elif event.type == VERT_SELECT:
            self.g.verts[event.label].bind(pygame.mouse.get_pos)
        elif event.type == VERT_DELETE:
            self.g.delete_vertex(event.label)

    def handle_key(self, key: int) -> None:
        if key == pygame.K_ESCAPE:
            self.running = False
        elif key == pygame.K_r:
            self.g.start_alg()

    def handle_mouse(self) -> None:
        # mouse buttons: 0 == left, 1 == middle, 2 == right
        buttons = pygame.mouse.get_pressed()
        if buttons[0]:
            self.ui.click('left')
        elif buttons[1]:
            self.ui.click('middle')
        elif buttons[2]:
            self.ui.click('right')

    def on_loop(self) -> None:
        self.g.update()
        self.ui.update(pygame.mouse.get_pos(), self.g)
        return

    def on_render(self) -> None:
        self.surf.fill(colors.BLACK)

        self.ui.render(self.surf, self.font, self.g)

        pygame.display.flip()

    def on_cleanup(self) -> None:
        pass

    def _init_font(self) -> pygame.font.Font:
        pygame.font.init()
        return pygame.font.Font(pygame.font.get_default_font(), 16)
