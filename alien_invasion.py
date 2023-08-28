import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    #Overall class to manage game assets and behaviour

    def __init__(self):
        """Initialize the game"""
        pygame.init()

        self.bullets = pygame.sprite.Group()

        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.aliens = pygame.sprite.Group()
        
        self.screen = pygame.display.set_mode((self.settings.width,self.settings.height))
        

        self.create_fleet()
        # self.bullet_width =2
        # self.bullet_speed = 3
        # self.bullet_height = 15
        # self.bullet_color = (255,255,255)

        #to run the game in windowed screen
        
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
            self.update_bullets()
            self.update_aliens()
            
            print(len(self.bullets))

    def update_screen(self):
            #Update images on screen and flip to new screen
            self.screen.fill(self.settings.bg_color)
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.ship.blitme()
            self.aliens.draw(self.screen)

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
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
     
    def update_bullets(self):
        self.bullets.update()

        #get rid of bullets that has disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def create_fleet(self):
        alien = Alien(self)
        # self.aliens.add(alien)
        alien_width, alien_height = alien.rect.size
        #creating a alien and adding until space filled
        current_x, current_y = alien_width, alien_height

        while current_y < (self.settings.height - 5* alien_height):

            while current_x < (self.settings.width - 2*alien_width):
                self.create_alien(current_x,current_y)
                current_x += (2 * alien_width )

            current_x = alien_width
            current_y += 2 * alien_height
            # new_alien = Alien(self)
            # new_alien.x = current_x
            # new_alien.rect.x = current_x
            # self.aliens.add(new_alien)
            # current_x += (2 * alien_width ) 
                
    def create_alien(self, x_position, y_position):
        #Create an alien
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def update_aliens(self):
        self.check_fleet_edges()
        self.aliens.update()
        

    def check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self.change_fleet_direction()
                break

    def change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

if __name__ == '__main__':
    #Run the game instance 
    game=AlienInvasion()
    game.run_game()

