import pygame

class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        #initialize the ship and it's starting position

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        
        #Load the ship image
         
        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.scale(self.image,[60,60])
        self.rect = self.image.get_rect()

        #start the ship at bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        #Deploy the ship
        self.screen.blit(self.image, self.rect)
        #create an instance of the ship

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left>0 :
            self.x -= self.settings.ship_speed

        
        
        #update rect object from self.x
        self.rect.x = self.x
        