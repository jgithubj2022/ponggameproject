"""Game objects to create PyGame based games."""

import warnings
import pygame
from .scene import PongScene

def display_info():
    """Print out information about the display driver and video information."""
    print(f'The display is using the "{pygame.display.get_driver()}" driver.')
    print("Video Info:")
    print(pygame.display.Info())


# If you're interested in using abstract base classes, feel free to rewrite
# these classes.
# For more information about Python Abstract Base classes, see
# https://docs.python.org/3.8/library/abc.html


# pylint: disable=too-few-public-methods
class VideoGame:
    """Base class for creating PyGame games."""

    def __init__(
        self,
        window_width=800,
        window_height=800,
        window_title="My Awesome Game",
    ):
        """Initialize a new game with the given window size and window title."""
        pygame.init()
        self._window_size = (window_width, window_height)
        self._clock = pygame.time.Clock()
        self._screen = pygame.display.set_mode(self._window_size)
        self._title = window_title
        pygame.display.set_caption(self._title)
        self._game_is_over = False
        if not pygame.font:
            warnings.warn("Fonts disabled.", RuntimeWarning)
        if not pygame.mixer:
            warnings.warn("Sound disabled.", RuntimeWarning)
        else:
            pygame.mixer.init()
        self._scene_manager = None
class PongGame(VideoGame):
    """ponggame class which runs pong scenes scene data and also controls the
      funciotn calls such as updating the scene and initializing the 
      window size and window descriptions"""
    def __init__(self):
        super().__init__(window_width=640, window_height=480, window_title="Pong Again!")
        self._scene = PongScene(self._screen)

    def run(self):
        """run function to start the scene while checking if
          valid with ym scene.py scene class' function"""
        self._scene.start_scene()

        while self._scene.is_valid():
            for event in pygame.event.get():
                self._scene.process_event(event)

            self._scene.update_scene()
            self._scene.draw()
            self._clock.tick(self._scene.frame_rate())

        self._scene.end_scene()
