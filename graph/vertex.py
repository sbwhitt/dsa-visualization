from pygame import draw
from pygame.surface import Surface
from pygame.font import Font
from pygame.color import Color
import utils.colors as colors

class Vertex:
    def __init__(self,
                 label: str,
                 pos: tuple[int, int] = (0, 0),
                 radius: int = 20,
                 color: Color = colors.RED) -> None:
        self.pos = pos
        self.label = label
        self.radius = radius
        self.color = color

    def render(self, surf: Surface, font: Font) -> None:
        draw.circle(surf, self.color, self.pos, self.radius)
        surf.blit(font.render(self.label, True, colors.WHITE), (self.pos[0]-4, self.pos[1]-8))

    def get_pos(self) -> tuple[int, int]:
        return self.pos
