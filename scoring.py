import pygame.font

class Scoreboard():
    """Scoreboard Class for the Star Wars Alien Invasion Game."""
    def __init__(self, ai_settings,screen,stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings for scoring information.
        self.text_color = (255,215,0)
        self.font = pygame.font.SysFont("starjedi", 20)
        self.prep_score()
        self.prep_level()

    def prep_score(self):
        """Turn the score into a rendered image."""
        score_str = str(self.stats.score)
        self.score_image = self.font.render('Points: ' + str(score_str), True, self.text_color,self.ai_settings.bg_image)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)

    def prep_level(self):
        self.level_image = self.font.render('Level: ' + str(self.stats.game_lvl), True,self.text_color, self.ai_settings.bg_image)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
