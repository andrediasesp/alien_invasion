import pygame

class Ship():

    def __init__(self,ai_settings,screen):
        """Initialize the game's Ship and its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings
        # Load the ship image and get its rect.
        self.image = pygame.image.load("starwars.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Decimal value for ship's center
        self.ship_center = float(self.rect.centerx)

        # Check Movement of the Ship
        self.moving_right = False
        self.moving_left  = False

    def update_position(self):
        "Update rebellion's ship based on movement flag"
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.ship_center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.ship_center -= self.ai_settings.ship_speed_factor
        # Update rect object from self.center.
        self.rect.centerx = self.ship_center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.ship_center = self.screen_rect.centerx
