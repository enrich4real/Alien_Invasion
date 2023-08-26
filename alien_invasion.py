import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    #Overall class to manage game assets and behaviour

    def __init__(self):
        """Initialize the game"""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.width,self.settings.height))
        pygame.display.set_caption("Alien Invasion Game")

        self.ship =Ship(self)

    def run_game(self):
        #Start the main loop for game
        while True:
            #Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            #Makes the most recently drawn screen visible
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    #Run the game instance 
    game=AlienInvasion()
    game.run_game()

