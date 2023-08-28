import os

class GameStats:
    def __init__(self,ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.high_score = self.load_high_score()

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1


    def save_high_score(self):
        with open("high.txt","w") as file:
            file.write(str(self.high_score))

    def load_high_score(self):
        if os.path.exists("high.txt"):
            with open("high.txt", "r") as file:
                return int(file.read())
        else:
            return 0

