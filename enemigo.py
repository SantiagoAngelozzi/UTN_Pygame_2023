import pygame
from constantes import *
from auxiliar import Auxiliar

class Enemigo():
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100) -> None:
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("UTN_Pygame_2023\images/caracters/enemigo/npc_dustbunny__x1_walk_png_1354831139.png", 8, 1)
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("UTN_Pygame_2023\images/caracters/enemigo/npc_dustbunny__x1_walk_right_png_1354831141.png", 9, 1,)
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet("UTN_Pygame_2023\images/caracters/enemigo/npc_dustbunny__x1_talk_png_1354831143.png",9, 6 )
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet("UTN_Pygame_2023\images/caracters/enemigo/npc_dustbunny__x1_talk_png_1354831143.png",9, 6)
        self.sound_die = Auxiliar.generar_sonido("UTN_Pygame_2023\sonido\Muerte (juego arcade) - Efecto de sonido [Para descargar].mp3", 1)        


        self.contador = 0
        self.frame = 0
        self.lives = 1
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_superior = pygame.Rect(self.rect.x, self.rect.y - 10, self.rect.width, 10)
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.is_jump = False
        self.is_fall = False
        self.is_live = True

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 
        self.interval_time_jump = interval_time_jump
   
    def change_x(self,delta_x):
        self.rect_superior.x += delta_x
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x

    def change_y(self,delta_y):
        self.rect_superior.y += delta_y
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y

    def do_movement(self,delta_ms,plataform_list,player):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0

            if(not self.is_on_plataform(plataform_list)):
                if(self.move_y == 0):
                    self.is_fall = True
                    self.change_y(self.gravity)
            else:
                self.is_fall = False
                self.change_x(self.move_x)
                if self.contador <= 50:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l
                    self.contador += 1 
                elif self.contador <= 100:
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                    self.contador += 1
                else:
                    self.contador = 0
            if self.check_collition(player) == True:
                self.lives -= 1
                print(f"vidas: {self.lives}")
                if self.lives == 0:
                    self.sound_die.play()
                    self.is_live = False

    def is_on_plataform(self,plataform_list):
        retorno = False
        
        if(self.ground_collition_rect.bottom >= 950):
            retorno = True     
        else:
            for plataforma in  plataform_list:
                if(self.ground_collition_rect.colliderect(plataforma.ground_collition_rect)):
                    retorno = True
                    break       
        return retorno          

    def check_collition(self,player):
            retorno = False
            if self.rect_superior.colliderect(player.rect_ground_collition):
                retorno = True
            return retorno

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0

    def update(self,delta_ms,plataform_list,player):
        self.do_movement(delta_ms,plataform_list,player)
        self.do_animation(delta_ms) 


    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.rect_superior)
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
        if self.is_live == True:
            self.image = self.animation[self.frame]
            screen.blit(self.image,self.rect)
        

        
    