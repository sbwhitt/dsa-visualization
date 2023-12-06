from pygame import draw
from pygame.surface import Surface
from pygame.color import Color
from graph.vertex import Vertex
import utils.colors as colors

class Edge:
    def __init__(self, start: Vertex, end: Vertex, color: Color = colors.WHITE) -> None:
        self.start = start
        self.end = end
        self.color = color

    def render(self, surf: Surface) -> None:
        draw.line(surf, self.color, self.start.get_pos(), self.end.get_pos(), width=2)
