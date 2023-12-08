from pygame.surface import Surface
from pygame.font import Font
from ui.button import Button
from ui.clickable import ClickableElement
from utils.events import *

class UI:
    def __init__(self, win_size: tuple[int, int]) -> None:
        self.elements: list[ClickableElement] = [
            Button(BFS_START, 'bfs', (win_size[0]-150, 25)),
            Button(DFS_START, 'dfs', (win_size[0]-150, 125))
        ]
        self.active = None

    def update(self, mouse_pos: tuple[int, int]) -> None:
        self.active = None
        for el in self.elements:
            el.update()
            if el.contains(mouse_pos):
                self.active = el

    def render(self, surf: Surface, font: Font) -> None:
        for el in self.elements:
            el.render(surf, font)
        if self.active:
            self.active.render_active(surf)

    def click(self) -> None:
        if self.active:
            self.active.click()

    def add_elements(self, elements: list[ClickableElement]) -> None:
        self.elements += elements
