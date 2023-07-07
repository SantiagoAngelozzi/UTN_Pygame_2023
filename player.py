from doctest import FAIL_FAST
import time
import pygame
from constantes import *
from auxiliar import Auxiliar

class Player:
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height) -> None:
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("UTN_Pygame_2023\images\caracters\player\walk.png",15,1)[:12]
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("UTN_Pygame_2023\images\caracters\player\walk.png",15,1,True)[:12]
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet("UTN_Pygame_2023\images\caracters\player\surprise.png",21,1,True)[7:8]
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet("UTN_Pygame_2023\images\caracters\player\surprise.png",21,1,)[7:8]
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet("UTN_Pygame_2023\images\caracters\player\jump.png",33,1,False,2)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet("UTN_Pygame_2023\images\caracters\player\jump.png",33,1,True,2)
        self.sound_jump = Auxiliar.generar_sonido("UTN_Pygame_2023\sonido\Boing Sound Effect  Boing Efecto de Sonido NO COPYRIGHT (HD) [2020].mp3", 1)
        self.sound_hit = Auxiliar.generar_sonido("UTN_Pygame_2023\sonido\Muerte de Minecraft - Sonido.mp3", 1)
        
        self.frame = 0
        self.lives = 5
        self.score = 0
        
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.jump_height = jump_height
        
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.collision_flag = False
        self.is_live = True
        self.is_jump = False
        self.is_fall = False
        

        self.last_collision_time = 0
        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        
        self.rect_ground_collition = pygame.Rect(self.rect.x + self.rect.w / 3, self.rect.y + self.rect.h - GROUND_RECT_H, self.rect.w / 3, GROUND_RECT_H)

    def walk(self,direction):
        if(self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
            self.frame = 0
            self.direction = direction
            if(direction == DIRECTION_R):
                self.move_x = self.speed_walk
                self.animation = self.walk_r
            else:
                self.move_x = -self.speed_walk
                self.animation = self.walk_l
        
    def jump(self,on_off = True):
        if(on_off and self.is_jump == False):
            self.sound_jump.play()
            self.y_start_jump = self.rect.y
            if(self.direction == DIRECTION_R):
                self.move_x = self.speed_walk
                self.move_y = -self.jump_power
                self.animation = self.jump_r
            else:
                self.move_x = -self.speed_walk
                self.move_y = -self.jump_power
                self.animation = self.jump_l
            self.frame = 0
            self.is_jump = True
        if(on_off == False):
            self.is_jump = False
            self.stay()

    def stay(self):
        if(self.animation != self.stay_r and self.animation != self.stay_l):
            if(self.direction == DIRECTION_R):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def do_movement(self,delta_ms,lista_plataformas,lista_enemigos,lista_botin):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            if(abs(self.y_start_jump)- abs(self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0

            self.tiempo_transcurrido_move = 0
            self.add_x(self.move_x)
            self.add_y(self.move_y)
                
            if(self.is_on_platform(lista_plataformas) == False):
                self.add_y(self.gravity)
            elif(self.is_jump): # SACAR
                self.jump(False)
            
            current_time = time.time()  # Obtener el tiempo actual en segundos
            collision_delay = 1  # Retraso en segundos antes de permitir otra colisión
            if self.check_collition(lista_enemigos) == True and current_time - self.last_collision_time > collision_delay:
                self.lives -= 1
                self.sound_hit.play()
                self.last_collision_time = current_time
                print(f"vidas: {self.lives}")
                if self.lives == 0:
                    self.is_live = False
                     
    def is_on_platform(self,lista_plataformas):
        retorno = False
        if(self.rect.y >= GROUND_LEVEL):     
            retorno = True
        else:
            for plataforma in lista_plataformas:
                if(self.rect_ground_collition.colliderect(plataforma.ground_collition_rect)):
                    retorno = True
                    break   
        return retorno
    
    def check_collition(self,lista_enemigos):
        retorno = False
        for enemigo in lista_enemigos:
            if self.rect.colliderect(enemigo.collition_rect) and enemigo.lives == 1:
                retorno = True
        return retorno
    
    def check_botin_collition(self, lista_botin):
        retorno = False
        for botin in lista_botin:
            if self.rect.colliderect(botin.rect) and botin.live == 1:
                retorno = True
        return retorno
        
    def add_x(self,delta_x):
        self.rect.x += delta_x
        self.rect_ground_collition.x += delta_x

    def add_y(self,delta_y):
        self.rect.y += delta_y  
        self.rect_ground_collition.y += delta_y


    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0
           
    def update(self,delta_ms,lista_plataformas,lista_enemigos,lista_botin):
        self.do_movement(delta_ms,lista_plataformas,lista_enemigos,lista_botin)
        self.do_animation(delta_ms)
        
    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,C_BLACK,self.rect)
            pygame.draw.rect(screen,C_GREEN,self.rect_ground_collition)
        if self.is_live == True:
            self.image = self.animation[self.frame]
            screen.blit(self.image,self.rect)

    def events(self,delta_ms,keys):
            if(keys[pygame.K_a] and not keys[pygame.K_d]):
                self.walk(DIRECTION_L)
            if(not keys[pygame.K_LEFT] and keys[pygame.K_d]):
                self.walk(DIRECTION_R)
            if(not keys[pygame.K_a] and not keys[pygame.K_d] and not keys[pygame.K_SPACE]):
                self.stay()
            if(keys[pygame.K_a] and keys[pygame.K_d] and not keys[pygame.K_SPACE]):
                self.stay()   
            if(keys[pygame.K_SPACE]):
                self.jump(True)