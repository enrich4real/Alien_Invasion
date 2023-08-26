import pygame

class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        #initialize the ship and it's starting position

        self.screen = ai_game.screen()
        self.screen_rect = ai_game.screen.get_rect()
        
        #Load the ship image
         
        ship.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #start the ship at bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        #Deploy the ship
        self.screen.blit(self.image, self.rect)
        