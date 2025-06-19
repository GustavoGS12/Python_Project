import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    pygame.init()
    sets = Settings()
    screen = pygame.display.set_mode((sets.screen_width, sets.screen_heigth))
    pygame.display.set_caption("Alien Invasion")
    stats = GameStats(sets)
    sb = Scoreboard(sets, screen, stats)
    ship = Ship(sets, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(sets, screen, ship, aliens)
    play_button = Button(sets, screen, "Play")
    while True:
        gf.check_events(sets, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(sets, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(sets, stats, sb, screen, ship, aliens, bullets)
        gf.update_screen(sets, screen, stats, sb, ship, aliens, bullets, play_button)



run_game()
