import pygame
import os
WIDTH = 1200
HEIGHT = 600

class player():
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('GamePy/pig.png.jpg')
        self.rect = pygame.Rect(100,100,100,100)
    
        


pygame.init()

game_window = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('Jogo')

gameloop = True
def draw():
    game_window.fill([255,255,0])



while gameloop:
    draw()
    player()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
    pygame.display.update()