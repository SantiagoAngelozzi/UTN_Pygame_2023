import pygame
from constantes import *
from auxiliar import Auxiliar

class Platform:
    def __init__(self,x,y,width,height,type=0) -> None:
        self.image_list = Auxiliar.getSurfaceFromSeparateFiles("UTN_Pygame_2023/images/Tiles/{0}.png",1,16,flip=False,w=width,h=height)
        self.image = self.image_list[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        
        

    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
        screen.blit(self.image,self.rect)