import pygame
import pygame_menu
import csv

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


def save_result(points, nickname, menu):
    with open('data/leaderboard.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([points, nickname])
    menu.disable()

def create_menu(theme, points):
    """
    This function creates a menu from given theme.
    """
    menu = pygame_menu.Menu('', WINDOW_WIDTH, WINDOW_HEIGHT, theme=theme)

    #play_button_sound = create_sound('assets/click-sound.wav', 0.1)
    
    menu.add.label('Congratulations you died')
    menu.add.label('Enter your nickname')
    menu.add.text_input('', onreturn=lambda nickname : save_result(points, nickname, menu))

    return menu

def end_game(points):

    surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    theme = pygame_menu.Theme(
                background_color=(0, 0, 0, 0), # transparent background
                title_font_shadow=True,
                title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE,
                widget_font=pygame_menu.font.FONT_8BIT,
                widget_font_size=30)

    myimage = pygame_menu.baseimage.BaseImage(
        image_path="assets/main-menu.jpg",
        drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
    )
    theme.background_color = myimage

    #run_background_theme('assets/main-menu-music.mp3')

    menu = create_menu(theme, points)
    menu.mainloop(surface)
