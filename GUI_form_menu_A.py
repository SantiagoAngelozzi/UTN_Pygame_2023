import pygame
from pygame.locals import *
from constantes import *
from GUI_form import Form
from GUI_button import Button

class FormMenuA(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)
        
        self.boton1 = Button(master=self,x=20,y=0,w=140,h=50,color_background=None,color_border=None,image_background="UTN_Pygame_2023\images\set_gui_01\Comic_Border\Buttons\Button_M_02.png",on_click=self.on_click_boton1,on_click_param="form_level_select",text="NIVELES",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton2 = Button(master=self,x=20,y=100,w=140,h=50,color_background=None,color_border=None,image_background="UTN_Pygame_2023\images\set_gui_01\Comic_Border\Buttons\Button_M_02.png",on_click=self.on_click_boton1,on_click_param="",text="SETTING",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton3 = Button(master=self,x=20,y=200,w=140,h=50,color_background=None,color_border=None,image_background="UTN_Pygame_2023\images\set_gui_01\Comic_Border\Buttons\Button_M_02.png",on_click=self.on_click_boton2,on_click_param="",text="QUIT",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton4 = Button(master=self,x=20,y=300,w=300,h=50,color_background=None,color_border=None,image_background="UTN_Pygame_2023\images\set_gui_01\Comic_Border\Buttons\Button_M_02.png",on_click=self.on_click_boton1,on_click_param="form_menu_instrucciones",text="INSTRUCCIONES",font="Verdana",font_size=30,font_color=C_WHITE)
        

        self.lista_widget = [self.boton4,self.boton3,self.boton2,self.boton1]
        
    def on_click_boton1(self, parametro):
        self.set_active(parametro)
    
    def on_click_boton2(self):
        pygame.quit()

    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()