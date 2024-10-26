from configuration import *
import pygame

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(WIN_WIDTH, WIN_HEIGHT)
        self.clock = pygame.time.Clock()
        self.caption = pygame.display.set_caption(GAME_NAME)
        self.running = True
        # self.icon = pygame.image.load()

    def createTileMap(self):
        pass

    def create(self):
        pass

    def update(self):
        pass

    def events(self):
        pass

    def draw(self):
        pass

    def main(self):
        self.screen.blit()
        pygame.display.update()

game = Game()
game.create()

while game.running:
    game.main()

pygame.quit()
quit()