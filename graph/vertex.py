from ui.clickable import ClickableElement
from pygame import draw
from pygame.surface import Surface
from pygame.font import Font
from pygame.color import Color
from pygame.event import post, Event
from utils.helpers import get_rect_from_circle
from utils.events import *
import utils.colors as colors

class Vertex(ClickableElement):
    def __init__(self,
                 label: str,
                 pos: tuple[int, int] = (10, 10),
                 radius: int = 20,
                 color: Color = colors.RED) -> None:
        self.pos = pos
        self.label = label
        self.radius = radius
        self.color = color
        self.dist = -1
        self.visited = False

    def render(self, surf: Surface, font: Font) -> None:
        draw.circle(surf, self.color, self.pos, self.radius)
        surf.blit(font.render(self.label, True, colors.WHITE), (self.pos[0]-4, self.pos[1]-8))

    def render_active(self, surf: Surface) -> None:
        draw.arc(surf, colors.WHITE, get_rect_from_circle(self.pos, self.radius), 0, 360)

    def start_bfs(self) -> None:
        self.dist = 0
        self.color = colors.GREEN

    def start_dfs(self) -> None:
        self.visited = True
        self.color = colors.GREEN

    def contains(self, mouse_pos: tuple[int, int]) -> bool:
        return get_rect_from_circle(self.pos, self.radius).contains(mouse_pos[0], mouse_pos[1], 1, 1)

    def click(self) -> None:
        post(Event(VERT_SELECT, dict={'label': self.label}))
