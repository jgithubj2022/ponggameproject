"scene file containing pongscene which contains the operations and scene of the game"
import pygame
import pygame.mixer
from .pong import Paddle, Ball
from .rgbcolors import black
from . import assets

class Scene:
    """Base class for scenes."""
    def __init__(self, screen, background_color=(0, 0, 0)):
        self._screen = screen
        self._background_color = background_color
        self._is_valid = True
    def start_scene(self):
        """start the scene"""

    def process_event(self, event):
        """process keyclicks or events related to pygames event calls """
        if event.type == pygame.QUIT:
            self._is_valid = False

    def update_scene(self):
        """update scene used for me to update ball position """

    def draw(self):
        """draw the scene regarding endscene and pongs scene"""
        self._screen.fill(self._background_color)

    def end_scene(self):
        """end the current scene"""

    def frame_rate(self):
        """in game.py helps manage framerate as 60"""
        return 60

    def is_valid(self):
        """checks validity of the scene"""
        return self._is_valid

class PongScene(Scene):
    """pong scene holds all the function calls for pong"""
    def __init__(self, screen):
        super().__init__(screen, background_color=black)
        self.clock = pygame.time.Clock()
        # load paddle hit sound
        hit_sound_path = assets.get("paddlehit")
        self.hit_sound = pygame.mixer.Sound(hit_sound_path)

        self.paddle_left = Paddle(30, 240)
        self.paddle_right = Paddle(610, 240)
        self.ball = Ball(320, 240)

        self.all_sprites = pygame.sprite.Group(
            self.paddle_left, self.paddle_right, self.ball
        )
        self.player_score = 0
        self.ai_score = 0
        self.font = pygame.font.SysFont("Arial", 80)
        #end game game over
        self.game_over = False

    def update_scene(self):
        self.ball.update()

        # right paddle is based on reactionary movement (it just follows balsl y)
        if self.ball.rect.centery < self.paddle_right.rect.centery:
            self.paddle_right.move(True)
        elif self.ball.rect.centery > self.paddle_right.rect.centery:
            self.paddle_right.move(False)
        # collision with paddles
        #make if collided with ai paddle or myself it will play the sound

        if self.ball.rect.colliderect(self.paddle_left.rect) or \
        self.ball.rect.colliderect(self.paddle_right.rect):
            self.ball.velocity.x *= -1
            self.hit_sound.play()  # play sound
        if not self.game_over:
            #if ball hits left or right wall increment score depending on the player
            if self.ball.rect.left <= 0:
                self.ai_score += 1
                self.ball.reset()
            elif self.ball.rect.right >= 640:
                self.player_score += 1
                self.ball.reset()
                #all of this is only if the game isnt over it shall account for point gain

        # ball reset reset if it hits left or right wall.
        if self.ball.rect.left <= 0 or self.ball.rect.right >= 640:
            self.ball.reset()
        #end game at 11 potsn
        if self.player_score == 11 or self.ai_score == 11:
            self.game_over = True
    def process_event(self, event):
        super().process_event(event)
        if self.game_over and event.type == pygame.MOUSEBUTTONDOWN:
            self.player_score = 0
            self.ai_score = 0
            self.ball.reset()
            self.game_over = False

        if not self.game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.paddle_left.move(True)
            if keys[pygame.K_s]:
                self.paddle_left.move(False)


    def draw(self):
        super().draw()
        # draw all game objects
        self.all_sprites.draw(self._screen)

        # ender and draw the score
        score_text = self.font.render(f"{self.player_score}  {self.ai_score}",
                                      True, (255, 255, 255))
        text_rect = score_text.get_rect(center=(self._screen.get_width() // 2, 240))
        #240 pixels from top and 2 centers the divisoin of the screens width
        #screen si 480 by 640pixels so div that sot he text is centerd
        self._screen.blit(score_text, text_rect)

        if self.game_over:
            game_over_font = pygame.font.SysFont("Arial", 80)
            game_over_text = game_over_font.render("GAME OVER!", True, (255, 0, 0))
            game_over_rect = game_over_text.get_rect(center=(self._screen.get_width() //
                                                             2, self._screen.get_height() // 2))
            self._screen.blit(game_over_text, game_over_rect)
        # flip the display after everything has been drawn
        pygame.display.flip()
