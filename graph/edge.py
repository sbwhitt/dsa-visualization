from pygame import draw
from pygame.surface import Surface
from pygame.color import Color
import utils.colors as colors

def render_edge(
        surf: Surface,
        start: tuple[int, int],
        end: tuple[int, int],
        color: Color = colors.WHITE,
        width: int = 2) -> None:
    draw.line(surf, color, start, end, width)
