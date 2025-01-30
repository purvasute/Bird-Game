import pygame

class Bird():
    def __init__(self, bsp_game):
        self.screen = bsp_game.screen
        self.screen_rect = bsp_game.screen.get_rect()


        self.image = pygame.image.load('bird_small.bmp')
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center


    def blitme(self):
        self.screen.blit(self.image, self.rect)


