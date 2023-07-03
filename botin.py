import pygame
from constantes import *
from auxiliar import Auxiliar

class Botin:
    def __init__(self,x,y,frame_rate_ms) -> None:
        self.stay = Auxiliar.getSurfaceFromSpriteSheet("UTN_Pygame_2023\images/botin/PC Computer - Cuphead Dont Deal With the Devil - Coin Overworld.png", 4, 4)
        self.stay_scalada = [pygame.transform.scale(img, (70, 70)) for img in self.stay]  # Escalar la imagen del sprite
        self.sound_botin = Auxiliar.generar_sonido("UTN_Pygame_2023\sonido\ytmp3free.cc_efecto-de-sonido-moneda-de-mario-hd-youtubemp3free.org.mp3",1)
        
        self.frame = 0
        self.live = 1

        self.animation = self.stay_scalada
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.botin_agarrado = False
        self.is_jump = False
        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.y_start_jump = 0
        self.rect_ground_collition = pygame.Rect(self.rect.x + self.rect.w / 3, self.rect.y + self.rect.h - GROUND_RECT_H, self.rect.w / 3, GROUND_RECT_H)

    def do_sound(self,player):
        if self.check_player_collition(player) == True:
            self.live -= 1
            self.botin_agarrado = True
            if self.live == 0:
                self.sound_botin.play()

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0
    
    def check_player_collition(self, player):
        retorno = False
        if self.rect.colliderect(player.rect):
            retorno = True
        return retorno
    
    def update(self,delta_ms,player):
        self.do_animation(delta_ms)
        self.do_sound(player)
    
    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,C_BLACK,self.rect)
            pygame.draw.rect(screen,C_GREEN,self.rect_ground_collition)
        if self.botin_agarrado == False:
            self.image = self.animation[self.frame]
            screen.blit(self.image,self.rect)
    
