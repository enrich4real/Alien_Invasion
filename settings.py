class Settings:
    #A class to store all settings

    def __init__(self):
        """Initialize The game settings and behaviour"""
        #Screen Settings
        self.width = 1280
        self.height = 720
        self.bg_color = (137,207,240)
        # self.ship_speed = 6.5 
        # self.ship_limit = 3
        self.bullet_color = (0,0,0)
        self.bullet_width = 4
        self.bullet_height = 15
        # self.bullet_speed = 6
        self.bullet_allowed = 6
        # self.alien_speed = 0.5
        self.fleet_drop_speed = 10
        # self.fleet_direction = 1
        self.ship_limit = 3

        self.speedup_scale = 1.2
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 6.5
        self.bullet_speed = 6
        self.alien_speed = 0.5
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)