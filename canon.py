import pygame
from pygame.sprite import Sprite

class Canon(Sprite):
    """Canon Class for our ship"""

    def __init__(self, ai_settings,screen,ship):
        super().__init__()
        self.screen = screen
        # We create a canon bullet rect at the top left corner of the screen and then adjust its position
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        # Location the canon blast at the center position of our ship at at the top of its rect
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # Canon blast y position along the screen
        self.y = float(self.rect.y)
        # blast color - lightsaber blue
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move the Bullet up the screen """
        self.y -= self.speed_factor
        # Update blast rect position
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
