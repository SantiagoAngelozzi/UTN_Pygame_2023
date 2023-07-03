from constantes import *
from GUI_button import Button
from GUI_progressbar import ProgressBar
from player import Player
from enemigo import Enemigo
from plataforma import Platform
from background import Background
from botin import Botin
from GUI_form import Form

class FormGameLevel3(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        # --- GUI WIDGET --- 
        self.boton1 = Button(master=self,x=0,y=0,w=140,h=50,color_background=None,color_border=None,image_background="UTN_Pygame_2023\images\set_gui_01\Comic_Border\Buttons\Button_L_02.png",on_click=self.on_click_boton1,on_click_param="form_menu_A",text="pause",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton2 = Button(master=self,x=200,y=0,w=140,h=50,color_background=None,color_border=None,image_background="UTN_Pygame_2023\images\set_gui_01\Comic_Border\Buttons\Button_M_02.png",on_click=self.on_click_boton1,on_click_param="form_level_select",text="niveles",font="Verdana",font_size=30,font_color=C_WHITE)
        
        self.pb_lives = ProgressBar(master=self,x=400,y=0,w=240,h=50,color_background=None,color_border=None,image_background="UTN_Pygame_2023/images\set_gui_01\Comic_Border\Bars\Bar_Background01.png",image_progress="UTN_Pygame_2023\images\set_gui_01\Comic_Border\Bars\Bar_Segment05.png",value = 5, value_max=5)
        self.widget_list = [self.boton1,self.pb_lives,self.boton2]
        # --- GAME ELEMNTS --- 
        self.static_background = Background(x=0,y=0,width=w,height=h,path="UTN_Pygame_2023/images/locations/all.png", path_music ="UTN_Pygame_2023/sonido\La canción de Yoshi bailando -TACA A XERECA PRA MIM  sub español.mp3")
        
        self.player_1 = Player(x=0,y=650,speed_walk=7,speed_run=29,gravity=10,jump_power=20,frame_rate_ms=20,move_rate_ms=10,jump_height=150)

        self.lista_enemigos = []
        self.lista_enemigos.append(Enemigo(600,600,4,20,10,0,1,1,0))
        self.lista_enemigos.append(Enemigo(1000,500,4,20,10,0,1,1,0))
        self.lista_enemigos.append(Enemigo(900,900,4,20,10,0,1,1,0))
        
        self.lista_plataformas = []
        self.lista_plataformas.append(Platform(0,800,100,50,13))
        self.lista_plataformas.append(Platform(100,800,100,50,14))
        self.lista_plataformas.append(Platform(200,800,100,50,15))
        self.lista_plataformas.append(Platform(400,700,100,50,13))
        self.lista_plataformas.append(Platform(500,700,100,50,14))
        self.lista_plataformas.append(Platform(600,700,100,50,15))
        self.lista_plataformas.append(Platform(800,600,100,50,13))
        self.lista_plataformas.append(Platform(900,600,100,50,14))
        self.lista_plataformas.append(Platform(1000,600,100,50,15))
        self.lista_plataformas.append(Platform(0,950,2000,250,1))

        self.lista_botin = []
        self.lista_botin.append(Botin(525,615,20))
        self.lista_botin.append(Botin(900,880,20))
        self.lista_botin.append(Botin(900,515,20))
      
    def on_click_boton1(self, parametro):
        self.set_active(parametro)
    
    def on_click_boton2(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.widget_list:
            aux_widget.update(lista_eventos)

        for enemy_element in self.lista_enemigos:
            enemy_element.update(delta_ms,self.lista_plataformas,self.player_1)
        
        for botin in self.lista_botin:
            botin.update(delta_ms,self.player_1)
            

        self.player_1.events(delta_ms,keys)
        self.player_1.update(delta_ms,self.lista_plataformas,self.lista_enemigos,self.lista_botin)


        self.pb_lives.value = self.player_1.lives 
    
    def draw(self): 
        super().draw()
        self.static_background.draw(self.surface)

        for aux_widget in self.widget_list:    
            aux_widget.draw()

        for botin in self.lista_botin:
            botin.draw(self.surface)

        for plataforma in self.lista_plataformas:
            plataforma.draw(self.surface)

        for enemy_element in self.lista_enemigos:
            enemy_element.draw(self.surface)
        
        
            self.player_1.draw(self.surface)