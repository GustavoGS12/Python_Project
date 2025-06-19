class GameStats():

    def __init__(self, sets):
        self.sets = sets
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        self.ships_left = self.sets.ship_limit
        self.score = 0
        self.level = 1

 