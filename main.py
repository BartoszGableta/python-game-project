import pygame
import pygame_menu
from src import window, end_screen, const
from typing import Callable


def start_game() -> None:
    """
    This function stops the current background music and runs the game loop.
    """

    pygame.mixer.music.stop()
    points = window.create_window()
    print(points)
    end_screen.end_game(points)
    run_background_theme('assets/main-menu-music.mp3')

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
    pygame.mixer.music.set_volume(const.MUSIC_VOLUME)
    pygame.mixer.music.play(-1)

def create_menu(theme: pygame_menu.Theme) -> pygame_menu.Menu:
    """
    This function creates a menu from given theme.
    """
    menu = pygame_menu.Menu('', const.WINDOW_WIDTH, const.WINDOW_HEIGHT, theme=theme)

    play_button_sound = create_sound('assets/click-sound.wav', const.EFFECT_VOLUME)
    
    selection_effect = pygame_menu.widgets.HighlightSelection(border_width=0)

    menu.add.button('Play', start_game, onselect=play_button_sound, selection_effect=selection_effect)
    menu.add.button('Leaderboard', pygame_menu.events.EXIT, onselect=play_button_sound, selection_effect=selection_effect)
    menu.add.button('Exit', pygame_menu.events.EXIT, onselect=play_button_sound, selection_effect=selection_effect)

    return menu

def main() -> None:
    """
    This function runs the menu.
    """

    pygame.init()

    pygame.display.set_caption(const.WINDOW_NAME)

    surface = pygame.display.set_mode((const.WINDOW_WIDTH, const.WINDOW_HEIGHT))

    theme = pygame_menu.Theme(
                background_color=(0, 0, 0, 0), # transparent background
                title_font_shadow=True,
                title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE,
                widget_font=pygame_menu.font.FONT_8BIT,
                widget_font_size=50)

    myimage = pygame_menu.baseimage.BaseImage(
        image_path=const.MAIN_MENU_BACKGROUND,
        drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
    )
    theme.background_color = myimage

    run_background_theme(const.MAIN_MENU_MUSIC)

    menu = create_menu(theme)
    menu.mainloop(surface)


if __name__ == '__main__':
    main()
