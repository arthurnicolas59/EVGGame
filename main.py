import pygame, sys
from states.game_state import GameState
import asyncio

# pygame setup
pygame.init()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

#music
pygame.mixer.music.load('assets/sound/Tryo-Greenwashing-_Clip-officiel_.ogg')
pygame.mixer.music.play(1, start=5)

game = GameState(screen)

async def main():
    while True:
        game.state_manager()
        clock.tick(60)  # limits FPS to 60
        await asyncio.sleep(0)

asyncio.run(main())


