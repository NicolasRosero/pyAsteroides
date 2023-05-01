#Importar pygame y las clases necesarias
import pygame, sys
from pygame.locals import *
from random import randint

#Inicalizar pygame
pygame.init()

#Creación de una ventana para el juego
ventana = pygame.display.set_mode((700, 400))

# Establecer título a la ventana
pygame.display.set_caption('Asteroides☄️')

# Establecer colo de fono de la ventada con rgb
colorFondo = (250, 126, 16)

# Color del rectángulo
color = (169, 167, 165)

# Cargar una imagen
imagen = pygame.image.load("resources/img/eddie.png")

# Bucle que mantiene la ventana abierta
while True:
    # Agregar los objetos a la ventana 
    # Establecer el colo de fondo
    ventana.fill(colorFondo)
    
    # Agregar la imaben a la ventana
    ventana.blit(imagen, (10, 40))
    
    # Establacer posiciones aleatorias
    for i in range(10):
        posX, posY = randint(1, 600), randint(1, 300)
        pygame.draw.rect(ventana, color, (posX, posY, 20, 40))
    
    # Bucle para recorrer cada evento que suceda dentro del juego
    for evento in pygame.event.get():
        # Validar si se presiona X de la ventana
        if evento.type == QUIT:
            # Detener todo
            pygame.quit()
            
            # Cerrar la ventana
            sys.exit()
        
        # Mantener actualizada la ventana
        pygame.display.update()