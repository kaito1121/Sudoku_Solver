import pygame
class Settings():
    def __init__(self):
        pygame.font.init()
        self.bg_colour = (255,255,255)
        self.font = pygame.font.SysFont("comicsans", 40)
        self.grid_width = 40
        self.thick_bar = 7
        self.thin_bar = 1