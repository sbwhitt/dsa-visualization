import pygame
import utils as utils

win_size = (960, 720)

class App:
    def __init__(self) -> None:
        self.running = True
        self.surf = pygame.display.set_mode(
            win_size, pygame.SCALED | pygame.RESIZABLE | pygame.DOUBLEBUF)

    def on_execute(self) -> None:
        self.on_init()

        while self.running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()

        self.on_cleanup()

    def on_init(self) -> None:
        pass

    def on_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.QUIT:
            self.running = False

    def on_loop(self) -> None:
        pass

    def on_render(self) -> None:
        self.surf.fill(pygame.Color(0, 0, 0))
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.lines(
            self.surf,
            pygame.Color(255, 0, 0),
            True,
            utils.get_rect_outline(pygame.rect.Rect(mouse_pos[0], mouse_pos[1], 100, 100))
        )

        pygame.display.flip()

    def on_cleanup(self) -> None:
        pass
