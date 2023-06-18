import pygame
import pygame_menu
import csv
import src.const as const

def save_result(points, nickname, menu):
    with open('data/leaderboard.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([points, nickname])
    menu.disable()

def run_background_theme(music_file: str) -> None:
    """
    This function runs the background theme.
    """
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1)


def create_menu(theme, points):
    """
    This function creates a menu from given theme.
    """
    menu = pygame_menu.Menu('', const.WINDOW_WIDTH, const.WINDOW_HEIGHT, theme=theme)
    
    menu.add.label('Congratulations you died', font_color=(255, 255, 255))
    menu.add.vertical_margin(30)
    menu.add.label(f'Score {points}', font_color=(255, 255, 255))
    menu.add.label('Enter your nickname', font_color=(255, 255, 255))
    menu.add.vertical_margin(10)
    menu.add.text_input('', onreturn=lambda nickname : save_result(points, nickname, menu), maxwidth = 10)

    return menu

def end_game(points):

    surface = pygame.display.set_mode((const.WINDOW_WIDTH, const.WINDOW_HEIGHT))

    theme = pygame_menu.Theme(
                background_color=(0, 0, 0, 0), # transparent background
                title_font_shadow=True,
                title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE,
                widget_font=pygame_menu.font.FONT_8BIT,
                widget_font_size=30)

    myimage = pygame_menu.baseimage.BaseImage(
        image_path="assets/end-screen.jpg",
        drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
    )
    theme.background_color = myimage

    run_background_theme('assets/end-screen-music.mp3')

    menu = create_menu(theme, points)
    menu.mainloop(surface)
