import pygame
from constantes import *
from auxiliar import Auxiliar

class Background:
    def __init__(self, x, y,width, height,  path, path_music):
        self.image = pygame.image.load(path).convert()
        self.image = pygame.transform.scale(self.image,(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.musica_fondo = Auxiliar.generar_musica(path_music, 0.1)


    def draw(self,screen):
        screen.blit(self.image,self.rect)
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)

    
