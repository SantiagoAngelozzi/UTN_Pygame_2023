from pygame.locals import *
from constantes import *
from GUI_form import Form
from GUI_button import Button
from GUI_textbox import TextBox

class FormLvlSelect(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)
        self.is_selected = None
        self.lvl1_btn = Button(master=self,x=20,y=20,w=140,h=50,color_background=None,color_border=None,image_background="UTN_Pygame_2023\images\set_gui_01\Comic_Border\Buttons\Button_M_02.png",on_click=self.click_lvl1,on_click_param="form_game_L1",text='Nivel 1',font="Verdana",font_size=30,font_color=C_WHITE)
        self.lvl2_btn = Button(master=self,x=20,y=100,w=140,h=50,color_background=None,color_border=None,image_background="UTN_Pygame_2023\images\set_gui_01\Comic_Border\Buttons\Button_M_02.png",on_click=self.click_lvl2,on_click_param="form_game_L2",text='Nivel 2',font="Verdana",font_size=30,font_color=C_WHITE)
        self.lvl3_btn = Button(master=self,x=20,y=200,w=140,h=50,color_background=None,color_border=None,image_background="UTN_Pygame_2023\images\set_gui_01\Comic_Border\Buttons\Button_M_02.png",on_click=self.click_lvl3,on_click_param="form_game_L3",text='Nivel 3',font="Verdana",font_size=30,font_color=C_WHITE)
        self.txt1 = TextBox(master=self,x=200,y=50,w=240,h=50,color_background=None,color_border=None,image_background="UTN_Pygame_2023\images\set_gui_01\Comic_Border\Buttons\Button_XL_08.png",text="seleccione un nivel",font="Verdana",font_size=30,font_color=C_BLACK)                                                                                                                                             
        self.lista_widget = [self.lvl1_btn,self.lvl2_btn,self.lvl3_btn,self.txt1]
    
    
    def click_lvl1(self,parametro):
        self.set_active(parametro)
        self.selected_lvl = 1
        
    
    def click_lvl2(self, parametro):
        self.set_active(parametro)
        self.selected_lvl = 2
        
    
    def click_lvl3(self, parametro):
        self.set_active(parametro)
        self.selected_lvl = 3
        
    
    def update(self, lista_eventos,keys,delta_ms):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()