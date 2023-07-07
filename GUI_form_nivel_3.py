from constantes import *
from GUI_button import Button
from GUI_progressbar import ProgressBar
from player import Player
from enemigo import Enemigo
from plataforma import Platform
from background import Background
from botin import Botin
from GUI_form import Form
from GUI_label import Label

class FormGameLevel3(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active,nivel_json):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.levels = nivel_json
        self.player_1 = self.generate_player()
    
        # --- GUI WIDGET --- 
        self.button_menu = Button(master=self,x=0,y=0,w=140,h=50,color_background=None,color_border=None,image_background="UTN_Pygame_2023\images\set_gui_01\Comic_Border\Buttons\Button_M_02.png",on_click=self.on_click_boton1,on_click_param="form_menu_A",text="MENU",font="Verdana",font_size=30,font_color=C_WHITE)
        
        self.text_score = Label(master=self,x=375,y=0,w=200,h=50,color_background=None,color_border=None,image_background=None,text=f'SCORE: {str(self.player_1.score)}',font='Arial',font_size=30,font_color=C_RED)
       
        self.pb_lives = ProgressBar(master=self,x=150,y=0,w=240,h=50,color_background=None,color_border=None,image_background="UTN_Pygame_2023\images\set_gui_01\Comic_Border\Bars\Bar_Background01.png",image_progress="UTN_Pygame_2023\images\set_gui_01\Comic_Border\Bars\Bar_Segment05.png",value = 5, value_max=5)
        self.widget_list = [self.button_menu,self.text_score,self.pb_lives]
        
        # --- GAME ELEMNTS --- 
        self.static_background = Background(x=0,y=0,width=w,height=h,path="UTN_Pygame_2023/images/locations/all.png")

        self.enemies_list = []
        self.generate_enemies()
        
        self.platform_list = []
        self.generate_platform()

        self.botin_lista = []
        self.generate_botin()

    def generate_player(self):
        data_player = self.levels[2]["player"]
        player = Player(x=data_player["x"],y=data_player["y"],speed_walk=data_player["speed_walk"],speed_run=data_player["speed_run"],
                        gravity=data_player["gravity"],jump_power=data_player["jump_power"],frame_rate_ms=data_player["frame_rate_ms"],
                        move_rate_ms=data_player["move_rate_ms"],jump_height=data_player["jump_height"])
        return player

    def generate_enemies(self):
        data_enemies = self.levels[2]["enemies"]
        for enemy in data_enemies:
            self.enemies_list.append(Enemigo(x=enemy["x"],y=enemy["y"],speed_walk=enemy["speed_walk"],speed_run=enemy["speed_run"],
                            gravity=enemy["gravity"],jump_power=enemy["jump_power"],frame_rate_ms=enemy["frame_rate_ms"],
                            move_rate_ms=enemy["move_rate_ms"],jump_height=enemy["jump_height"]))
        
    def generate_platform(self):
        data_platforms = self.levels[2]["platforms"]
        for platform in data_platforms:
            self.platform_list.append(Platform(x=platform["x"],y=platform["y"],height=platform["height"],width=platform["width"],type=platform["type"]))

    def generate_botin(self):
        data_botin = self.levels[2]["botin"]
        for botin in data_botin:
            self.botin_lista.append(Botin(x=botin["x"],y=botin["y"],frame_rate_ms=botin["frame_rate_ms"]))

    def on_click_boton1(self, parametro):
        self.set_active(parametro)


    def update(self, lista_eventos,keys,delta_ms):
        
        
        for aux_widget in self.widget_list:
            aux_widget.update(lista_eventos)

        for enemy_element in self.enemies_list:
            enemy_element.update(delta_ms,self.platform_list,self.player_1)
            
        for loot_element in self.botin_lista:
            loot_element.update(delta_ms,self.player_1)
            

        self.text_score._text = f'SCORE: {str(self.player_1.score)}'
        self.player_1.events(delta_ms,keys)
        self.player_1.update(delta_ms,self.platform_list,self.enemies_list,self.botin_lista)

        self.pb_lives.value = self.player_1.lives 

        if self.player_1.score >= 3:
            self.reiniciar_nivel()
            self.set_active("form_menu_win")
                
        if self.player_1.lives < 1:
            self.reiniciar_nivel()
            self.set_active("form_menu_die")
            
    def on_click_boton1(self, parametro):
        print("entro")
        self.reiniciar_nivel()
        self.set_active(parametro) 
           
            
        
    def reiniciar_nivel(self):
        self.player_1 = self.generate_player()
        self.boss = None
        self.platform_list = []
        self.enemies_list = []
        self.bullet_list = []
        self.proyectile_list = []
        self.proyectile_enemy_list = []   
        self.botin_lista = []
        self.generate_enemies()
        self.generate_platform()
        self.generate_botin()

        
    def draw(self): 
        super().draw()
        self.static_background.draw(self.surface)


        for aux_widget in self.widget_list:    
            aux_widget.draw()

        for plataforma in self.platform_list:
            plataforma.draw(self.surface)

        for enemy_element in self.enemies_list:
            enemy_element.draw(self.surface)
        
        self.player_1.draw(self.surface)
            
        for loot_element in self.botin_lista:
            loot_element.draw(self.surface)