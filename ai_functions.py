import sys
import pygame
import ship
from canon import Canon
from empire import Empire
from time import sleep


def keydown_events(ai_settings,screen,event,ship,bullets):
    if event.key == pygame.K_RIGHT:
        # Move rebellions ship to the right
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        fire_canon(ai_settings,screen,ship,bullets)
    if event.key == pygame.K_q:
        sys.exit()

def keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets,stats,play_button,fleet,sb):
    """ Watch for keyboard and mouse events """
    for event in pygame.event.get():
        # When trying to exit the game's window, a QUIT type event is detected by pygame
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keydown_events(ai_settings,screen,event,ship,bullets)
        elif event.type == pygame.KEYUP:
            keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y,ai_settings, screen, ship, fleet,bullets,sb)

def check_play_button(stats, play_button, mouse_x, mouse_y,ai_settings, screen, ship, fleet,bullets,sb):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset Game Settings
        ai_settings.dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        # Reset Level and Score
        sb.prep_score()
        sb.prep_level()
        # Empty Groups
        fleet.empty()
        bullets.empty()
        # Create new fleet and center rebellion ship
        create_fleet(ai_settings,screen,fleet,ship)
        ship.center_ship()

def refresh_screen(ai_settings,screen,ship,fleet,bullets,play_button,stats,sb):
    """Redraw the screen during each pass through the loop - With bg color or with a bg image"""
    # screen.fill(ai_settings.bg_color)
    screen.blit(ai_settings.bg_image, (0,0))
    # Draw bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # Draw Ship
    ship.blitme()
    # Draw Empire Fleet
    fleet.draw(screen)
    # Draw the score information.
    sb.show_score()
    # Set Button if game inactive
    if not stats.game_active:
        play_button.draw_button()
    # Make the most recently drawn screen visible.
    pygame.display.flip()

def update_bullets(ai_settings,screen,ship,bullets,fleet,stats,sb):
    """ Update bullets """
    # Update bullet positions.
    bullets.update()
    # Remove bullets past screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # Check for any bullets that have hit aliens
    check_canon_collision(ai_settings,screen,fleet,ship,bullets,stats,sb)

def check_canon_collision(ai_settings,screen,fleet,ship,bullets,stats,sb):
    # groupcollide(group1, group2, dokill1, dokill2, collided = None) -> Sprite_dict
    collisions = pygame.sprite.groupcollide(bullets, fleet, True, True)
    if collisions:
        for e_ship in collisions.values():
            stats.score += ai_settings.scoring_points * len(e_ship)
            sb.prep_score()
    # If there's no empire ships, create a new one
    if len(fleet) == 0:
        bullets.empty()
        ai_settings.increase_gamespeed()
        # Increase game Level
        stats.game_lvl += 1
        sb.prep_level()
        # Create a new empire fleet
        create_fleet(ai_settings,screen,fleet,ship)

def fire_canon(ai_settings,screen,ship,bullets):
    # Limit number of shots fired to the number declared in the settings file
    if len(bullets) < ai_settings.nr_bullets:
        bullet = Canon(ai_settings,screen,ship)
        bullets.add(bullet)

def get_number_ships(ai_settings,ship_width):
    """Calculate the number of ships in a screen row"""
    av_space = ai_settings.width - 2 * ship_width
    nr_ships = int(av_space / (2 * ship_width))
    return nr_ships

def create_fleet(ai_settings,screen,fleet,ship):
    """Create an empire fleet."""
    empire_ship = Empire(ai_settings,screen)
    # Calculate available Space
    empire_ship_width = empire_ship.rect.width
    # Calculate the number of empire ships in a screen row
    nr_ships = get_number_ships(ai_settings,empire_ship_width)
    nr_rows = get_number_rows(ai_settings,ship.rect.height,empire_ship.rect.height)
    #Create a row of empire ships
    for row_number in range(nr_rows):
        for ship_nr in range(nr_ships):
            empire_ship = Empire(ai_settings,screen)
            empire_ship.x = empire_ship_width + 2 * empire_ship_width * ship_nr
            empire_ship.rect.x = empire_ship.x
            empire_ship.rect.y = empire_ship.rect.height + 2 * empire_ship.rect.height * row_number
            fleet.add(empire_ship)

def get_number_rows(ai_settings, ship_height, empire_height):
    """Determine the number of rows of ships that fit on the screen."""
    available_space_y = (ai_settings.height - (3 * empire_height) - ship_height)
    number_rows = int(available_space_y / (2 * empire_height))
    return number_rows

def check_fleet_edges(ai_settings,fleet):
    """Respond appropriately if any empire ship have reached an edge."""
    for empire_ship in fleet.sprites():
        if empire_ship.check_edges():
            change_fleet_direction(ai_settings, fleet)
            break

def change_fleet_direction(ai_settings, fleet):
    """Drop the entire fleet and change the fleet's direction."""
    for empire_ship in fleet.sprites():
        empire_ship.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_empire_ship(ship,ai_settings, fleet,bullets,stats,screen):
    """ Check if the fleet is at an edge, and then update the postions of all ships in the fleet."""
    check_fleet_edges(ai_settings, fleet)
    fleet.update()
    # Test empire and rebellion ships collision
    # spritecollideany(sprite, group, collided = None)
    if pygame.sprite.spritecollideany(ship, fleet):
        empire_hit(ai_settings, stats, screen, ship, fleet, bullets)
    check_ship_bottom(ai_settings, stats, screen, ship, fleet, bullets)

def empire_hit(ai_settings, stats, screen, ship, fleet, bullets):
    """Respond to ship being hit by alien."""
    if stats.ships_left > 0:
        # Decrement ships_left.
        stats.ships_left -= 1
        # Empty the list of empire ships and bullets.
        fleet.empty()
        bullets.empty()
        #Create a new fleet and center the ship.
        create_fleet(ai_settings,screen,fleet,ship)
        ship.center_ship()
        # Pause.
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_ship_bottom(ai_settings, stats, screen, ship, fleet, bullets):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for empire_ship in fleet.sprites():
        if empire_ship.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break
