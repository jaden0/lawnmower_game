import numpy as np
import pygame


class Grass(object):
    def __init__(self, width, height):
        self.whitespace = 50
        self.width = width
        self.height = height - self.whitespace
        self.resolution = 200
        self.color = ((0, 0, 0), (22, 128, 48), (128, 199, 30))  # no grass, uncut, cut
        self.grass = np.ones((self.resolution, self.resolution))
        print(self.grass)

        self.box_width = self.width / self.resolution
        self.box_height = self.height / self.resolution
        self.box_centers = []
        self.box_corners = []
        for i in range(0, self.resolution):
            self.box_centers.append(
                [
                    (
                        (i + 0.5) * self.box_width,
                        (j + 0.5) * self.box_height + self.whitespace,
                    )
                    for j in range(0, self.resolution)
                ]
            )
            self.box_corners.append(
                [
                    (i * self.box_width, j * self.box_height)
                    for j in range(0, self.resolution)
                ]
            )

    def get_square(self, pos):
        i = np.floor(pos[0] / self.box_width)
        j = np.floor((pos[1] - self.whitespace) / self.box_height)
        return [int(i), int(j)]

    def cut(self, i, j):
        self.grass[i][j] = 2

    def draw(self, win):
        for i in range(0, self.resolution):
            for j in range(0, self.resolution):
                pygame.draw.rect(
                    win,
                    self.color[int(self.grass[i][j])],
                    (
                        i * self.box_width,
                        j * self.box_height + self.whitespace,
                        self.box_width,
                        self.box_height,
                    ),
                )
                # pygame.draw.rect(win,(0,0,0),(i*self.box_width,j*self.box_height,self.box_width,self.box_height),2)
