from pygame.locals import *
from constantes import *
from GUI_form import Form
from GUI_button import Button
from GUI_label import Label

class FormMenuWin(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)
        
        self.boton1 = Button(master=self,x=0,y=0,w=140,h=50,color_background=None,color_border=None,image_background="UTN_Pygame_2023\images\set_gui_01\Comic_Border\Buttons\Button_M_02.png",on_click=self.on_click_boton3,on_click_param="form_menu_A",text="VOLVER",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton2 = Button(master=self,x=0,y=100,w=500,h=50,color_background=None,color_border=None,image_background="UTN_Pygame_2023\images\set_gui_01\Comic_Border\Buttons\Button_M_02.png",on_click=self.on_click_boton3,on_click_param="form_menu_B",text="GUARDAR PUNTAJE",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton3 = Button(master=self,x=0,y=200,w=500,h=50,color_background=None,color_border=None,image_background="UTN_Pygame_2023\images\set_gui_01\Comic_Border\Buttons\Button_M_02.png",on_click=self.on_click_boton3,on_click_param="form_level_select",text="JUGAR",font="Verdana",font_size=30,font_color=C_WHITE)
        self.text_win = Label(master=self,x=100,y=0,w=400,h=50,color_background=None,color_border=None,image_background=None,text='YOU WIN!!!',font='Arial',font_size=30,font_color=C_RED)

        self.lista_widget = [self.boton1, self.boton2,self.text_win,self.boton3]
        
    def on_click_boton3(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()