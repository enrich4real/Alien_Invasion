import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    #Overall class to manage game assets and behaviour

    def __init__(self):
        """Initialize the game"""
        pygame.init()

        self.bullets = pygame.sprite.Group()

        self.clock = pygame.time.Clock()
        self.settings = Settings()
        # self.bullet_width =2
        # self.bullet_speed = 3
        # self.bullet_height = 15
        # self.bullet_color = (255,255,255)

        #to run the game in windowed screen
        self.screen = pygame.display.set_mode((self.settings.width,self.settings.height))

        #to run the game in full screeen
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion Game")

        self.ship =Ship(self)

    def run_game(self):
        #Start the main loop for game
        while True:
            #Watch for keyboard and mouse events
            self.check_events()
            self.update_screen()
            self.clock.tick(144)
            self.ship.update()
            self.bullets.update()

    def update_screen(self):
            #Update images on screen and flip to new screen
            self.screen.fill(self.settings.bg_color)
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.ship.blitme()

            #Makes the most recently drawn screen visible
            pygame.display.flip()
            

    def check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    self.check_keydown_events(event)
                        
                elif event.type == pygame.KEYUP:
                    self.check_keyup_events(event)

            
    def check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            #Move the ship right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet() 

    def check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
         
    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
     
                

if __name__ == '__main__':
    #Run the game instance 
    game=AlienInvasion()
    game.run_game()

