import pygame.freetype as ft
from settings import *


class Text:
    def __init__(self, app):
        self.app = app
        self.font = ft.Font(FONT_PATH)

    def draw(self):
        self.font.render_to(self.app.screen, (WIN_W * 0.595, WIN_H * 0.02),
                            text='TETRIS', fgcolor='white',
                            size=TILE_SIZE * 1.65, bgcolor='black')

        self.font.render_to(self.app.screen, (WIN_W * 0.70, WIN_H * 0.22),
                            text='next', fgcolor='orange',
                            size=TILE_SIZE * 1.4, bgcolor='black')

        self.font.render_to(self.app.screen, (WIN_W * 0.68, WIN_H * 0.67),
                            text='score', fgcolor='orange',
                            size=TILE_SIZE * 1.4, bgcolor='black')

        self.font.render_to(self.app.screen, (WIN_W * 0.70, WIN_H * 0.8),
                            text=f'{self.app.tetris.score}', fgcolor='white',
                            size=TILE_SIZE * 1.8)
