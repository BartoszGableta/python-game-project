from src import window
import pygame
import pygame_menu
from typing import Callable

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


def start_game() -> None:
    """
    This function stops the current background music and runs the game loop.
    """

    pygame.mixer.music.stop()
    window.create_window()

def create_sound(sound_file: str, volume: float) -> Callable[[None], None]:
    """
    This function creates a function that plays given sound.
    """
    sound = pygame.mixer.Sound(sound_file)
    sound.set_volume(volume)

    def play_sound() -> None:
        sound.play()

    return play_sound

def run_background_theme(music_file: str) -> None:
    """
    This function runs the background theme.
    """
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

def create_menu(theme: pygame_menu.Theme) -> pygame_menu.Menu:
    """
    This function creates a menu from given theme.
    """
    menu = pygame_menu.Menu('', WINDOW_WIDTH, WINDOW_HEIGHT, theme=theme)

    play_button_sound = create_sound('assets/click-sound.wav', 0.1)
    
    menu.add.button('Play', start_game, onselect=play_button_sound)
    menu.add.button('Leaderboard', pygame_menu.events.EXIT, onselect=play_button_sound)
    menu.add.button('Exit', pygame_menu.events.EXIT, onselect=play_button_sound)

    return menu

def main() -> None:
    """
    This function runs the menu.
    """

    pygame.init()

    surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    theme = pygame_menu.Theme(background_color=(0, 0, 0, 0), # transparent background
                title_font_shadow=True,
                title_background_color=(4, 47, 126),
                title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE,
                widget_font=pygame_menu.font.FONT_8BIT,
                widget_font_size=50)

    myimage = pygame_menu.baseimage.BaseImage(
    image_path="assets/main-menu2.jpg",
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
    )
    theme.background_color = myimage

    run_background_theme('assets/main-menu-music.mp3')

    menu = create_menu(theme)
    menu.mainloop(surface)


if __name__ == '__main__':
    main()
