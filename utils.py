from pygame import rect

def get_rect_outline(rect: rect.Rect) -> list[tuple]:
    '''Returns pygame rect vertices minus offset for rendering outline'''
    return [
        rect.topleft,
        rect.bottomleft,
        rect.bottomright,
        rect.topright
    ]
