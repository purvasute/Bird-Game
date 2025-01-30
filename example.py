import sys
import pygame
from setting import Setting
from bird import Bird

class Blue():
    def __init__(self):
        pygame.init()
        self.setting = Setting()

        self.screen = pygame.display.set_mode((
            self.setting.screen_width, self.setting.screen_height))
        pygame.display.set_caption("Blue game")

        self.bird = Bird(self)

    def run_game(self):
        while True:
            for events in pygame.event.get():
                if events == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.setting.bg_color)
            self.bird.blitme()

            pygame.display.flip()

if __name__ == '__main__':
    bsg = Blue()
    bsg.run_game()


