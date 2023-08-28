import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #a class to represent single alien

    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #LOad the alien image
        self.image = pygame.image.load("images/alien.bmp")
        self.image = pygame.transform.scale(self.image,[60,60])
        self.rect = self.image.get_rect() 

        #start each new alien near the top
        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height 

        #store alien's position
        self.x=float(self.rect.x)

    def update(self):
        #move alien right
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edge(self):
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <=0)