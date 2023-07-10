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
from GUI_form_menu_win import FormMenuWin
from GUI_form_menu_gameover import FormMenuGameOver
from GUI_form_menu_instrucciones import FormMenuInstrucciones
from GUI_form_menu_settings import FormMenuSettings
from GUI_form_menu_score import FormMenuScore

flags = DOUBLEBUF 
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
pygame.init()
clock = pygame.time.Clock()
nivel_json = Auxiliar.leer_archivo("UTN_Pygame_2023/niveles.json")
pygame.mixer.init()
pygame.mixer.music.load("UTN_Pygame_2023\sonido\La canción de Yoshi bailando -TACA A XERECA PRA MIM  sub español.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

form_menu_A = FormMenuA(name="form_menu_A",master_surface = screen,x=700,y=200,w=700,h=700,color_background=(0,0,0),color_border=(255,0,255),active=True)
form_menu_lvl = FormLvlSelect(name="form_level_select",master_surface = screen,x=700,y=200,w=700,h=700,color_background=(0,0,0),color_border=(255,0,255),active=False)
form_menu_B = FormMenuB(name="form_menu_B",master_surface = screen,x=700,y=200,w=700,h=700,color_background=(0,0,0),color_border=(255,0,255),active=False)
form_menu_win = FormMenuWin(name="form_menu_win",master_surface = screen,x=700,y=200,w=700,h=700,color_background=(0,0,0),color_border=(255,0,255),active=False)
form_menu_die = FormMenuGameOver(name="form_menu_die",master_surface = screen,x=700,y=200,w=700,h=700,color_background=(0,0,0),color_border=(255,0,255),active=False)
form_menu_instrucciones = FormMenuInstrucciones(name="form_menu_instrucciones",master_surface = screen,x=700,y=200,w=700,h=700,color_background=(0,0,0),color_border=(255,0,255),active=False)
form_menu_settings = FormMenuSettings(name="form_menu_settings",master_surface = screen,x=700,y=200,w=700,h=700,color_background=(0,0,0),color_border=(255,0,255),active=False)
form_menu_score = FormMenuScore(name="form_menu_score",master_surface = screen,x=700,y=200,w=700,h=700,color_background=(0,0,0),color_border=(255,0,255),active=False)

form_game_L1 = FormGameLevel1(name="form_game_L1",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),active=False,nivel_json=nivel_json)
form_game_L2 = FormGameLevel2(name="form_game_L2",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),active=False,nivel_json=nivel_json)
form_game_L3 = FormGameLevel3(name="form_game_L3",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),active=False,nivel_json=nivel_json)

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