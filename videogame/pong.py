"""made to hold ball and paddle class in which pongscene calls to access these items """
import pygame
#creating the paddle class and ball class sprites
class Paddle(pygame.sprite.Sprite):
    """paddle is for the player and the ai paddle"""
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 100))
        self.image.fill((255, 255, 255))  # white
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 6

    def move(self, up=True):
        """move the paddle which only is constrained to the x axis by y
          can move freely through the height of the screeen"""
        if up:
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

        # Keep paddle on screen
        self.rect.y = max(0, min(self.rect.y, 480 - self.rect.height))


class Ball(pygame.sprite.Sprite):
    """ball is the single ball used within the game 
    accounting for bouncing and creating the ball """
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = pygame.Vector2(5, 5)

    def update(self):
        """updates allowing boundcing off the topo and bottom of the the borders"""
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        if self.rect.top <= 0 or self.rect.bottom >= 480:
            self.velocity.y *= -1

    def reset(self):
        """resets balls location in center of 640 480 pixel screen and its velocity"""
        self.rect.center = (320, 240)
        self.velocity = pygame.Vector2(5, 5)
