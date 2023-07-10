from pygame.locals import *
from GUI_label import Label
from GUI_form import Form
from GUI_button import Button
from GUI_textbox import TextBox
from sql import *
from constantes import *
from GUI_form_nivel_3 import FormGameLevel3

class FormMenuB(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.puntaje = FormGameLevel3.obtener_puntaje_total

        self.boton1 = Button(master=self,x=0,y=150,w=200,h=40,color_background=C_GREEEN_2,color_border=C_YELLOW_2,on_click=self.on_click_boton1,on_click_param="form_menu_A",text="volver",font="Verdana",font_size=30,font_color=C_BLACK)
        self.boton2 = Button(master=self,x=0,y=200,w=200,h=40,color_background=C_PINK,color_border=C_RED,on_click=self.on_click_boton2,on_click_param="",text="AGREGAR",font="Verdana",font_size=30,font_color=C_BLACK)
        self.boton3 = Button(master=self,x=0,y=250,w=200,h=40,color_background=C_PINK,color_border=C_RED,on_click=self.on_click_boton3,on_click_param="",text="CREAR",font="Verdana",font_size=30,font_color=C_BLACK)
        self.boton4 = Button(master=self,x=0,y=300,w=200,h=40,color_background=C_PINK,color_border=C_RED,on_click=self.on_click_boton4,on_click_param="",text="MOSTRAR",font="Verdana",font_size=30,font_color=C_BLACK)
       
        self.instrucciones = Label(master=self,x=0,y=0,w=300,h=50,color_background=None,color_border=None,image_background=None,text="ingresa nombre ->",font='Arial',font_size=30,font_color=C_RED)
        self.txt1 = TextBox(master=self,x=300,y=0,w=240,h=40,color_background=None,color_border=None,image_background="UTN_Pygame_2023\images\set_gui_01\Comic_Border\Buttons\Button_XL_08.png",text="aqui",font="Verdana",font_size=30,font_color=C_BLACK)
        self.name = self.txt1
        self.lista_widget = [self.boton1,self.boton2,self.boton3,self.boton4,self.txt1,self.instrucciones]

    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def on_click_boton2(self, parametro):
        insertar_linea(self.name, self.puntaje)
        
    def on_click_boton3(self, parametro):
        crear_tabla()
        
    def on_click_boton4(self, parametro):
        leer_tabla()
        
    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()