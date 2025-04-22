"""run file for our program calling my ponggame 
function which facilitates my scenes 
"""
#!/usr/bin/env python3
import sys
import pygame

from videogame.game import PongGame

pygame.init()
pygame.mixer.init()

if __name__ == "__main__":
    sys.exit(PongGame().run())
