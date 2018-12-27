import pygame
import ai_functions as af
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from stats import GameStats
from playbutton import Button

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    # Initialize Settings
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.width,ai_settings.height),pygame.RESIZABLE)
    # Set game window caption
    pygame.display.set_caption("Alien Invasion - Star Wars Edition")
    # Play Button
    play_button = Button(ai_settings, screen, "Play")
    # Initilize Game Stats for every Player
    stats = GameStats(ai_settings)
    # Initialize Game's Ship
    ship = Ship(ai_settings,screen)
    # Store ship bullets
    bullets = Group()
    # Store empire fleet
    fleet = Group()
    # Send empire ships to the game
    af.create_fleet(ai_settings,screen,fleet,ship)
    # Start the main loop for the game - User actions control the flow of the game
    while True:
        # Check Events
        af.check_events(ai_settings, screen, ship, bullets,stats,play_button,fleet)
        if stats.game_active:
            # Check movement
            ship.update_position()
            # Update bullets position and remove ones past screen
            af.update_bullets(ai_settings,screen,ship,bullets,fleet)
            # Update Fleet position
            af.update_empire_ship(ship,ai_settings, fleet,bullets,stats,screen)
        # Refresh Screen
        af.refresh_screen(ai_settings,screen,ship,fleet,bullets,play_button,stats)

if __name__ == "__main__":
    run_game()
