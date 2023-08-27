class Settings:
    #A class to store all settings

    def __init__(self):
        """Initialize The game settings and behaviour"""
        #Screen Settings
        self.width = 1400
        self.height = 900
        self.bg_color = (137,207,240)
        self.ship_speed = 6.5 
        self.bullet_color = (0,0,0)
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_speed = 4