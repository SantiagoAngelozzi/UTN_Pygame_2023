import pygame
from pygame.locals import *
from constantes import *
from GUI_form import Form
from GUI_button import Button
from GUI_label import Label

class FormMenuInstrucciones(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)
        
        self.boton1 = Button(master=self,x=0,y=0,w=140,h=50,color_background=None,color_border=None,image_background="UTN_Pygame_2023\images\set_gui_01\Comic_Border\Buttons\Button_M_02.png",on_click=self.on_click_boton1,on_click_param="form_menu_A",text="VOLVER",font="Verdana",font_size=30,font_color=C_WHITE)
        self.instrucciones_title = Label(master=self,x=200,y=0,w=300,h=50,color_background=None,color_border=None,image_background=None,text="INSTRUCCIONES",font='Arial',font_size=30,font_color=C_RED)
        self.instrucciones_1 = Label(master=self,x=0,y=100,w=700,h=50,color_background=None,color_border=None,image_background=None,text="*CONTROLES: movimiento (W/A/S/D), salto (SPACE).",font='Arial',font_size=20,font_color=C_RED)
        self.instrucciones_2 = Label(master=self,x=0,y=200,w=700,h=50,color_background=None,color_border=None,image_background=None,text="*Debes recoger todo el botin esparcido por el mapa para ganar.",font='Arial',font_size=20,font_color=C_RED)
        self.instrucciones_3 = Label(master=self,x=0,y=300,w=700,h=50,color_background=None,color_border=None,image_background=None,text="*Tienes un total de 5 vidas, si la barra de vida llega a 0 pierdes.",font='Arial',font_size=20,font_color=C_RED)
        self.instrucciones_4 = Label(master=self,x=0,y=400,w=700,h=50,color_background=None,color_border=None,image_background=None,text="*Tienes 30 segundos para ganar.",font='Arial',font_size=20,font_color=C_RED)
        self.lista_widget = [self.boton1, self.instrucciones_title, self.instrucciones_1,self.instrucciones_2,self.instrucciones_3,self.instrucciones_4]
        
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