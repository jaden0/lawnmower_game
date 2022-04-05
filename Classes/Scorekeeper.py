import pygame
import time
import numpy as np


# noinspection SpellCheckingInspection
class Scorekeeper(object):
    def __init__(self,starting_seconds):
        self.score = 0
        self.score_color = (34, 123, 210)
        self.end_time = time.time() + starting_seconds

    def calculate(self, grass):
        cut_grass = grass.grass == 2
        uncut_grass = grass.grass == 1
        self.score = (
            np.count_nonzero(cut_grass)
            / (np.count_nonzero(uncut_grass) + np.count_nonzero(cut_grass))
            * 100
        )

    def draw_score(self, win):
        font = pygame.font.SysFont("comicsa nsms", 30)
        text = font.render("Grass cut: %.1f%%" % self.score, False, self.score_color)
        win.blit(
            text,
            (win.get_width() - text.get_width() * 1.2, -text.get_height() / 2 + 25),
        )

    def draw_final_score(self, win):
        font = pygame.font.SysFont("comicsa nsms", 30)
        text = font.render(
            "Total grass cut: %.1f%%" % self.score, False, self.score_color
        )
        win.blit(
            text,
            (
                win.get_width() / 2 - text.get_width() / 2,
                win.get_height() / 2 - text.get_height() / 2 + 50,
            ),
        )

    def draw_timer(self, win):
        font = pygame.font.SysFont("comicsa nsms", 30)
        color = (self.score_color, (255, 0, 0))[self.end_time - time.time() < 10]
        text = font.render(
            "Remaining Time: %.1f seconds" % (self.end_time - time.time()), False, color
        )
        win.blit(text, (25, -text.get_height() / 2 + 25))

    def start_timer(self, wait_time):
        self.end_time = time.time() + wait_time

    def game_over(self):
        if self.end_time - time.time() < 0:
            return True
