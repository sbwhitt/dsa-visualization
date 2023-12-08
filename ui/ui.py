from typing import Literal
from graph.graph import Graph
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

    def _update_graph(self, mouse_pos: tuple[int, int], graph: Graph) -> None:
        for _, v in graph.verts.items():
            v.update()
            if v.contains(mouse_pos):
                self.active = v

    def update(self, mouse_pos: tuple[int, int], graph: Graph) -> None:
        self.active = None
        for el in self.elements:
            if el.contains(mouse_pos):
                self.active = el
        self._update_graph(mouse_pos, graph)

    def _render_graph(self, surf: Surface, font: Font, graph: Graph) -> None:
        for k, v in graph.edges.items():
            for vert in v:
                graph.get_edge(graph.verts[k], vert).render(surf)
        for _, v in graph.verts.items():
            v.render(surf, font)

    def render(self, surf: Surface, font: Font, graph: Graph) -> None:
        self._render_graph(surf, font, graph)

        for el in self.elements:
            el.render(surf, font)

        if self.active:
            self.active.render_active(surf)

    def click(self, button: Literal['left', 'middle', 'right']) -> None:
        if self.active:
            if button == 'left': self.active.left_click()
            elif button == 'middle': self.active.middle_click()
            elif button == 'right': self.active.right_click()

    def add_elements(self, elements: list[ClickableElement]) -> None:
        self.elements = elements + self.elements

    def delete_element(self, el: ClickableElement) -> None:
        self.elements.remove(el)
