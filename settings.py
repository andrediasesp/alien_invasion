import pygame
# Settings for the Alien Invasion Game
class Settings():
    """Settings for the Alien Invasion - Star Wars Game."""
    def __init__(self):
        # Screen Settings
        self.width = 900
        self.height = 600
        # If you don't want an image as your game's background, you can assign a rgb combination to it
        #self.bg_color = (230, 230, 230)
        # Load background image
        self.bg_image = pygame.image.load("C:\\Users\\andre.dias\\OneDrive\\Programming\\Python\\AlienInvasion\\bgstar.bmp")
        # Rebellion Ship speed factor i.e number of pixels shifted by the ship along the screen
        self.ship_speed_factor = 5
        # Blasts info
        self.bullet_speed_factor = 9
        self.bullet_height = 30
        self.bullet_width = 3
        self.bullet_color = 0,191,255
        self.nr_bullets = 3
        # Empire Ship Info
        self.empire_ship_speed = 6
        self.fleet_drop_speed = 16
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        # Number of Rebellion Ships available in the game
        self.ship_limit = 3
