from pygame.rect import Rect

def get_rect_outline(rect: Rect) -> list[tuple]:
    '''Returns pygame rect vertices minus offset for rendering outline'''
    return [
        rect.topleft,
        rect.bottomleft,
        rect.bottomright,
        rect.topright
    ]

def get_rect_from_circle(center: tuple[int, int], radius: int) -> Rect:
    return Rect(center[0] - radius, center[1] - radius, radius*2, radius*2)
