import pygame
import sys
from time import sleep
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, sets, screen, ship, stats, sb, aliens, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(sets, screen, ship, bullets)
    elif event.key == pygame.K_p and not stats.game_active:
        start_game(sets, screen, stats, sb, ship, aliens, bullets)
    elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(sets, screen, stats, sb, play_button, ship, aliens, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, sets, screen, ship, stats, sb, aliens, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(sets, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def update_screen(sets, screen, stats, sb, ship, aliens, bullets, play_button):
    screen.fill(sets.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()


def update_bullets(sets, screen, stats, sb, ship, aliens, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        check_bullet_alien_collisions(sets, screen, stats, sb, ship, aliens, bullets)


def fire_bullet(sets, screen, ship, bullets):
    if len(bullets) < sets.bullets_allowed:
        new_bullet = Bullet(sets, screen, ship)
        bullets.add(new_bullet)


def create_fleet(sets, screen, ship, aliens):
    alien = Alien(sets, screen)
    number_aliens_x = get_number_aliens_x(sets, alien.rect.width)
    number_rows = get_number_rows(sets, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(sets, screen, aliens, alien_number, row_number)


def get_number_aliens_x(sets, alien_width):
    avaiable_space_x = sets.screen_width - (2 * alien_width)
    number_aliens_x = int(avaiable_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(sets, screen, aliens, alien_number, row_number):
    alien = Alien(sets, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + (2 * alien_width * alien_number)
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + (2 * alien.rect.height * row_number)
    aliens.add(alien)


def get_number_rows(sets, ship_height, alien_height):
    available_space_y = (sets.screen_heigth - (3 * alien_height) - ship_height)
    numbers_rows = int(available_space_y / (2 * alien_height))
    return numbers_rows


def update_aliens(sets, stats, sb, screen, ship, aliens, bullets):
    check_fleet_edges(sets, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(sets, stats, sb, screen, ship, aliens, bullets)
    check_aliens_bottom(sets, stats, sb, screen, ship, aliens, bullets)


def check_fleet_edges(sets, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(sets, aliens)
            break


def change_fleet_direction(sets, aliens):
    for alien in aliens.sprites():
        alien.rect.y += sets.fleet_drop_speed
    sets.fleet_direction *= -1


def check_bullet_alien_collisions(sets, screen, stats, sb, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += sets.alien_points * len(aliens)
            sb.prep_score()
            check_high_score(stats, sb)
    if len(aliens) == 0:
        bullets.empty()
        sets.increase_speed()
        stats.level += 1
        sb.prep_level()
        create_fleet(sets, screen, ship, aliens)


def ship_hit(sets, stats, sb, screen, ship, aliens, bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        create_fleet(sets, screen, ship, aliens)
        ship.center_ship()
        sleep(3)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(sets, stats, sb, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(sets, stats, sb, screen, ship, aliens, bullets)
            break


def check_play_button(sets, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        start_game(sets, screen, stats, sb, ship, aliens, bullets)


def start_game(sets, screen, stats, sb, ship, aliens, bullets):
    sets.initialize_dynamic_settings()
    stats.reset_stats()
    stats.game_active = True
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    sb.prep_ships()
    aliens.empty()
    bullets.empty()
    create_fleet(sets, screen, ship, aliens)
    ship.center_ship()
    pygame.mouse.set_visible(False)


def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
