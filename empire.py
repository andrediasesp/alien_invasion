import pygame
from pygame.sprite import Sprite

class Empire(Sprite):
    """Empire Fleet class."""
    def __init__(self,ai_settings,screen ):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Load an emprie ship
        self.image = pygame.image.load("C:\\Users\\andre.dias\\OneDrive\\Programming\\Python\\AlienInvasion\\empire.bmp")
        self.rect  = self.image.get_rect()
        # Locate the empire ship at the top left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Locate the ship
        self.x = float(self.rect.x)

    def blit_empire(self):
        """Draw the empire ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Check if an empire ship has gone into an edge """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        if self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right."""
        self.x += (self.ai_settings.empire_ship_speed * self.ai_settings.fleet_direction)
        self.rect.x = self.x
