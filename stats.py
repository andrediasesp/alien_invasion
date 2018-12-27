class GameStats():
    """GameStats for the Alien Invasion - Star Wars Edition."""
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        # Initilize game in inactive state
        self.game_active = False

    def reset_stats(self):
        """Initialize Game Stats"""
        self.ships_left = self.ai_settings.ship_limit
        # Start Alien Invasion in an active state.
        self.game_active = False
