import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from games_stat import GameStats
from button import Button
from scoreboard import ScoreBoard

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
        

        
        # self.bullet_width =2
        # self.bullet_speed = 3
        # self.bullet_height = 15
        # self.bullet_color = (255,255,255)

        #to run the game in windowed screen
        
        # #to run the game in full screeen
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        self.create_fleet()

        pygame.display.set_caption("Alien Invasion Game")
        self.stats = GameStats(self)
        self.sb = ScoreBoard(self)

        self.ship =Ship(self)
        self.game_active = False
        self.play_button = Button(self, "Click Here or press P to play")

    def run_game(self):
        #Start the main loop for game
        while True:
            #Watch for keyboard and mouse events
            self.check_events()
            if self.game_active:

                
                self.ship.update()
                self.update_bullets()
                self.update_aliens()
            
            self.update_screen()
            self.clock.tick(144)
            

    def update_screen(self):
            #Update images on screen and flip to new screen
            
            self.screen.fill(self.settings.bg_color)
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.ship.blitme()
            self.aliens.draw(self.screen)
            self.sb.show_score()
            if not self.game_active:
                self.play_button.draw_button()    
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

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.check_play_button(mouse_pos)

            
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
        elif event.key == pygame.K_p:
            self.game_active = True
    

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

        self.check_bullet_alien_collisions()

        #check for any bullets
    def check_bullet_alien_collisions(self):
        collissions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)

        if collissions:
            for aliens in collissions.values():
                self.stats.score += self.settings.alien_points * len(aliens)

            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            self.bullets.empty()
            self.create_fleet()
            self.settings.increase_speed()
            #increase level
            self.stats.level += 1
            self.sb.prep_level()

    def create_fleet(self):
        alien = Alien(self)
        # self.aliens.add(alien)
        alien_width, alien_height = alien.rect.size
        #creating a alien and adding until space filled
        current_x, current_y = alien_width, alien_height +50

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

        #look for collisssions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.ship_hit()
        
        self.check_aliens_bottom()

    def check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self.change_fleet_direction()
                break

    def change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def ship_hit(self):

        if self.stats.ships_left>0:

            self.stats.ships_left -= 1
            self.sb.prep_ships()

            self.bullets.empty()
            self.aliens.empty()
        
            self.create_fleet()
            self.ship.center_ship()

            sleep(0.5)

        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.height:
                self.ship_hit()
                break

    def check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            self.game_active = True

            self.bullets.empty()
            self.aliens.empty()

            self.create_fleet()
            self.ship.center_ship()
            #hide mouse cursor
            pygame.mouse.set_visible(False)


    

if __name__ == '__main__':
    #Run the game instance 
    game=AlienInvasion()
    game.run_game()

