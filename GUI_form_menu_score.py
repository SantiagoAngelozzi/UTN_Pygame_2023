import pygame
from pygame.locals import *
from constantes import *
from GUI_form import Form
from GUI_button import Button
from GUI_label import Label
from sql import sql

class FormMenuScore(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.lista_puntajes = sql.devolver_puntaje()

        self.title = Label(master=self,x=100,y=100,w=400,text="puntaje usuarios",color_border=None,font="Verdana",font_size=50,font_color=C_YELLOW_2)
        self.puesto_1 = Label(master=self,x=100,y=200,w=400,text=f"{self.lista_puntajes[0]}",color_border=None,font="Verdana",font_size=30,font_color=C_WHITE)
        self.puesto_2 = Label(master=self,x=100,y=250,w=400,text=f"{self.lista_puntajes[1]}",color_border=None,font="Verdana",font_size=30,font_color=C_WHITE)
        self.puesto_3 = Label(master=self,x=100,y=300,w=400,text=f"{self.lista_puntajes[2]}",color_border=None,font="Verdana",font_size=30,font_color=C_WHITE)
        self.puesto_4 = Label(master=self,x=100,y=350,w=400,text=f"{self.lista_puntajes[3]}",color_border=None,font="Verdana",font_size=30,font_color=C_WHITE)
        self.puesto_5 = Label(master=self,x=100,y=400,w=400,text=f"{self.lista_puntajes[4]}",color_border=None,font="Verdana",font_size=30,font_color=C_WHITE)
           
        self.button_menu = Button(master=self,x=0,y=0,w=140,h=50,color_background=None,color_border=None,image_background="UTN_Pygame_2023\images\set_gui_01\Comic_Border\Buttons\Button_M_02.png",on_click=self.on_click_boton3,on_click_param="form_menu_A",text="volver",font="Verdana",font_size=30,font_color=C_WHITE)
       
        self.lista_widget = [self.puesto_1,self.puesto_2,self.puesto_3,self.puesto_4,self.puesto_5,self.title,self.button_menu]
    
    def on_click_boton3(self, parametro):
        self.set_active(parametro)
        

    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)
    
    def draw(self): 
        super().draw()
        

        
        for aux_widget in self.lista_widget:    
            aux_widget.draw()