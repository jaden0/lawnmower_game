import pygame
from Classes.Lawnmower import Lawnmower
from Classes.Grass import Grass
from Classes.Scorekeeper import Scorekeeper
from Classes.Blackbox import Blackbox


class Game(object):
    def __init__(self):
        self.game_width = 800
        self.game_height = 650
        self.win = pygame.display.set_mode((self.game_width, self.game_height))
        self.clock = pygame.time.Clock()
        self.lawnmower = Lawnmower(500, 300)
        self.grass = Grass(self.game_width, self.game_height)
        self.scorekeeper = Scorekeeper()
        self.obstructions = [Blackbox(200,300,100,20),Blackbox(575,500,10,120)]
        pygame.init()

    def cut(self):
        self.lawnmower.cut(self.grass)

    def collision(self, object, obstructions):
        is_collision = False
        for obstruction in obstructions:
            for i in range(0,4):
                if object.hitbox.is_hit(obstruction.hitbox.corners[i]):
                    is_collision = True
                if obstruction.hitbox.is_hit(object.hitbox.corners[i]):
                    is_collision = True
        return( is_collision )


    def move(self, object, instruction):
        object.update_hitbox(instruction)
        if not self.collision(object,self.obstructions):
            object.update()
        else:
            object.reset()

    def draw(self):
        self.win.fill((255, 255, 255))
        self.grass.draw(self.win)
        self.lawnmower.draw(self.win)
        self.scorekeeper.calculate(self.grass)
        self.scorekeeper.draw_score(self.win)
        self.scorekeeper.draw_timer(self.win)
        for obstruction in self.obstructions:
            obstruction.draw(self.win)
        pygame.display.update()

    def game_over(self):
        self.win.fill((255, 255, 255))
        font = pygame.font.SysFont("comicsa nsms", 30)
        text = font.render("Game Over", False, (0, 0, 0))
        self.win.blit(
            text,
            (
                self.win.get_width() / 2 - text.get_width() / 2,
                self.win.get_height() / 2 - text.get_height() / 2,
            ),
        )
        self.scorekeeper.draw_final_score(self.win)
        pygame.display.update()

    def tick(self):
        self.clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            return False
        if keys[pygame.K_UP]:
            #self.lawnmower.move(0)
            self.move(self.lawnmower,0)
        if keys[pygame.K_DOWN]:
            #self.lawnmower.move(1)
            self.move(self.lawnmower,1)
        if keys[pygame.K_LEFT]:
            #self.lawnmower.move(2)
            self.move(self.lawnmower,2)
        if keys[pygame.K_RIGHT]:
            #self.lawnmower.move(3)
            self.move(self.lawnmower,3)

        if keys[pygame.K_t]:
            self.scorekeeper.start_timer(50)

        self.cut()
        #if not self.scorekeeper.game_over():

        self.draw()
        #else:
        #    self.game_over()



        return True
