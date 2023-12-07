from pygame.event import Event
from pygame.event import post
from pygame.surface import Surface
from pygame.font import Font
from pygame import draw
from pygame.rect import Rect
from utils.helpers import get_rect_outline
import utils.colors as colors

class Button:
    def __init__(
            self,
            event: int,
            label: str,
            pos: tuple[int, int],
            size: tuple[int, int] = (80, 60)) -> None:
        self.event = Event(event)
        self.label = label
        self.rect = Rect(pos[0], pos[1], size[0], size[1])
        self.hover = False

    def render(self, surf: Surface, font: Font) -> None:
        draw.rect(surf, colors.RED, self.rect)
        surf.blit(font.render(self.label, True, colors.WHITE), (self.rect.left + 10, self.rect.top + 10))

    def render_outline(self, surf: Surface) -> None:
        draw.lines(surf, colors.WHITE, True, get_rect_outline(self.rect))

    def click(self) -> None:
        post(self.event)
