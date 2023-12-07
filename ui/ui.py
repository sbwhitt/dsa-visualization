from pygame.surface import Surface
from pygame.font import Font
from ui.button import Button
from utils.events import *

class UI:
    def __init__(self, win_size: tuple[int, int]) -> None:
        self.elements = [
            Button(BFS_EVENT, 'bfs', (win_size[0]-150, 25)),
            Button(DFS_EVENT, 'dfs', (win_size[0]-150, 125))
        ]
        self.active = None

    def update(self, mouse_pos: tuple[int, int]) -> None:
        self.active = None
        for el in self.elements:
            if el.rect.contains(mouse_pos[0], mouse_pos[1], 1, 1):
                self.active = el
                break

    def render(self, surf: Surface, font: Font) -> None:
        for el in self.elements:
            el.render(surf, font)
        if self.active:
            self.active.render_outline(surf)

    def click(self) -> None:
        if self.active:
            self.active.click()
