"""
This file contains all the constant values that are used in other packages.
"""

# Window parameters
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_NAME = 'Space survivors'

# Music
MAIN_MENU_MUSIC = 'assets/main-menu-music.mp3'
GAME_MUSIC = 'assets/game-music.mp3'
END_SCREEN_MUSIC = 'assets/end-screen-music.mp3'
MUSIC_VOLUME = 0.05
EFFECT_VOLUME = 0.1

# Player parameters
DEFAULT_PLAYER_SIZE = (50, 50)
DEFAULT_PLAYER_POSITION = (0, 0)
DEFAULT_PLAYER_SPEED = 3.5
DEFAULT_PLAYER_ROTATE = 2
DEFAULT_PLAYER_HP = 1000

# Enemy parameters
DEFAULT_ENEMY_SIZE = (50, 50)
DEFAULT_ENEMY_SPEED = 3
DEFAULT_ENEMY_HP = 600

# Player bullet parameters
DEFAULT_PLAYER_BULLET_SIZE = (10, 10)
DEFAULT_PLAYER_BULLET_SPEED = 8
DEFAULT_PLAYER_BULLET_DAMAGE = 50

# Enemy bullet parameters
DEFAULT_ENEMIES_BULLET_SIZE = (10, 10)
DEFAULT_ENEMIES_BULLET_SPEED = 10
DEFAULT_ENEMIES_BULLET_DAMAGE = 20

# Enemy generation parameters
DEFAULT_ENEMY_LIMIT = 125
ENEMY_GENERATION_DISTANCE = 500
ENEMY_MAX_DISTANCE = 600
GENERATION_TIME = 500   # In milliseconds

# Graphics
PLAYER_IMAGE = 'assets/player-model.png'
ENEMY_IMAGE = 'assets/enemy-model.png'
MAIN_MENU_BACKGROUND = 'assets/main-menu-background.jpg'
GAME_BACKGROUND = 'assets/game-background.png'
END_SCREEN_BACKGROUND = 'assets/end-screen-background.jpg'
PLAYER_BULLET_IMAGE = 'assets/player-bullet.png'
ENEMY_BULLET_IMAGE = 'assets/enemy-bullet.png'

# Other
KILL_POINTS = 100
COLLISION_DAMAGE = 5
