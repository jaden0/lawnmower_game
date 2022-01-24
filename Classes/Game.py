import pygame
from Classes.Lawnmower import Lawnmower
from Classes.Grass import Grass
from Classes.Scorekeeper import Scorekeeper

class Game(object):
    def __init__(self):
        self.game_width = 800
        self.game_height = 650
        self.win = pygame.display.set_mode((self.game_width, self.game_height))
        self.clock = pygame.time.Clock()
        self.lawnmower = Lawnmower(300,300)
        self.grass = Grass(self.game_width, self.game_height)
        self.scorekeeper = Scorekeeper()
        pygame.init()

    def cut(self):
        self.lawnmower.cut(self.grass)

    def draw(self):
        self.win.fill((255,255,255))

        self.grass.draw(self.win)
        self.lawnmower.draw(self.win)
        self.scorekeeper.calculate(self.grass)
        self.scorekeeper.draw_score(self.win)
        self.scorekeeper.draw_timer(self.win)
        pygame.display.update()


    def game_over(self):
        self.win.fill((255,255,255))
        font = pygame.font.SysFont("comicsa nsms", 30)
        text = font.render("Game Over", False, (0,0,0))
        self.win.blit(text, (self.win.get_width()/2 - text.get_width()/2 , self.win.get_height()/2 -text.get_height()/2))
        self.scorekeeper.draw_final_score(self.win)
        pygame.display.update()


    def tick(self):
        self.clock.tick(24)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            return False
        if keys[pygame.K_UP]:
            self.lawnmower.move(0)
        if keys[pygame.K_DOWN]:
            self.lawnmower.move(1)
        if keys[pygame.K_LEFT]:
            self.lawnmower.move(2)
        if keys[pygame.K_RIGHT]:
            self.lawnmower.move(3)

        if keys[pygame.K_t]:
            self.scorekeeper.start_timer(50)

        self.cut()
        if not self.scorekeeper.game_over():
            self.draw()
        else:
            self.game_over()
        return True