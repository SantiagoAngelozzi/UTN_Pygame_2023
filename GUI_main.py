import pygame
from pygame.locals import *
import sys
from constantes import *
from auxiliar import *
from GUI_form import Form
from GUI_form_menu_levels import FormLvlSelect
from GUI_form_menu_A import FormMenuA
from GUI_form_menu_B import FormMenuB 
from GUI_form_nivel_1 import FormGameLevel1
from GUI_form_nivel_2 import FormGameLevel2
from GUI_form_nivel_3 import FormGameLevel3

flags = DOUBLEBUF 
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
pygame.init()
clock = pygame.time.Clock()
nivel_json = Auxiliar.leer_archivo("niveles.json")
music_path = "UTN_Pygame_2023\sonido\La canción de Yoshi bailando -TACA A XERECA PRA MIM  sub español.mp3"

form_menu_lvl = FormLvlSelect(name="form_level_select",master_surface = screen,x=300,y=200,w=500,h=400,color_background=(0,255,255),color_border=(255,0,255),active=True)
form_menu_B = FormMenuB(name="form_menu_B",master_surface = screen,x=300,y=200,w=500,h=400,color_background=(0,255,255),color_border=(255,0,255),active=False)
form_menu_A = FormMenuA(name="form_menu_A",master_surface = screen,x=300,y=200,w=500,h=400,color_background=(255,255,0),color_border=(255,0,255),active=True)

form_game_L1 = FormGameLevel1(name="form_game_L1",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),active=False,nivel_json=nivel_json)
form_game_L2 = FormGameLevel2(name="form_game_L2",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),active=False,nivel_json=nivel_json)
form_game_L3 = FormGameLevel3(name="form_game_L3",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),active=False,nivel_json=nivel_json)

Auxiliar.generar_musica(music_path,0.1)

while True:     
    
    
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    delta_ms = clock.tick(FPS)

    aux_form_active = Form.get_active()
    if(aux_form_active != None):
        aux_form_active.update(lista_eventos,keys,delta_ms)
        aux_form_active.draw()
    pygame.display.flip()