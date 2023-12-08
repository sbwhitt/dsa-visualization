from pygame.surface import Surface
from pygame.font import Font

class ClickableElement:
    def update(self) -> None:
        pass

    def render(self, surf: Surface, font: Font) -> None:
        pass

    def render_active(self, surf: Surface) -> None:
        pass

    def contains(self, mouse_pos: tuple[int, int]) -> bool:
        pass

    def click(self) -> None:
        pass
