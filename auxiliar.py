import json
import pygame

pygame.mixer.init()
class Auxiliar:
    @staticmethod
    def getSurfaceFromSpriteSheet(path,columnas,filas,flip=False, step = 1,scale=1):
        lista = []
        surface_imagen = pygame.image.load(path)
        fotograma_ancho = int(surface_imagen.get_width()/columnas)
        fotograma_alto = int(surface_imagen.get_height()/filas)
        fotograma_ancho_scaled = int(fotograma_ancho*scale)
        fotograma_alto_scaled = int(fotograma_alto*scale)
        x = 0
        
        for fila in range(filas):
            for columna in range(0,columnas,step):
                x = columna * fotograma_ancho
                y = fila * fotograma_alto
                surface_fotograma = surface_imagen.subsurface(x,y,fotograma_ancho,fotograma_alto)
                if(scale != 1):
                    surface_fotograma = pygame.transform.scale(surface_fotograma,(fotograma_ancho_scaled, fotograma_alto_scaled)).convert_alpha() 
                if(flip):
                    surface_fotograma = pygame.transform.flip(surface_fotograma,True,False).convert_alpha() 
                lista.append(surface_fotograma)
        return lista

    @staticmethod
    def getSurfaceFromSeparateFiles(path_format,from_index,quantity,flip=False,step = 1,scale=1,w=0,h=0,repeat_frame=1):
        lista = []
        for i in range(from_index,quantity+from_index):
            path = path_format.format(i)
            surface_fotograma = pygame.image.load(path)
            fotograma_ancho_scaled = int(surface_fotograma.get_rect().w * scale)
            fotograma_alto_scaled = int(surface_fotograma.get_rect().h * scale)
            if(scale == 1 and w != 0 and h != 0):
                surface_fotograma = pygame.transform.scale(surface_fotograma,(w, h)).convert_alpha()
            if(scale != 1):
                surface_fotograma = pygame.transform.scale(surface_fotograma,(fotograma_ancho_scaled, fotograma_alto_scaled)).convert_alpha() 
            if(flip):
                surface_fotograma = pygame.transform.flip(surface_fotograma,True,False).convert_alpha() 
            
            for i in range(repeat_frame):
                lista.append(surface_fotograma)
        return lista
    
    def leer_archivo(path: str):
        '''
        Esta función lee un archivo json y lo devuelve como una lista.
        ------------
        Parametro:
        path: tipo string -> es la ruta en donde se encuentra el archivo JSON a leer.
        ------------
        Retorna: 
        lista_jugadores: tipo list[dict] -> una lista que posee el contenido del archivo JSON.
        '''
        with open(path, 'r') as archivo:
            diccionario = json.load(archivo)
            lista_niveles = diccionario["niveles"]
        return lista_niveles

    def generar_musica(path: str, volumen: float):
        '''
        Función que se encarga de generar una música de fondo para mi juego
        Recibe el path donde se ubique mi música y el volumen de la misma
        '''
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(volumen)


    def generar_sonido(path: str, volumen: float):
        '''
        Función que se encarga de generar un sondi
        Recibe el path en donde se encuentra ese sonido y el volumen del mismo
        Retorna el sonido para esperar a que se ejecute
        '''
        sonido = pygame.mixer.Sound(path)
        sonido.set_volume(volumen)
        return sonido