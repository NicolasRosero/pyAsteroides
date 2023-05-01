#Importar pygame y las clases necesarias
import pygame, sys
from pygame.locals import *
from random import randint

#Inicalizar pygame
pygame.init()

#Creación de una ventana para el juego
ventana = pygame.display.set_mode((700, 500))

# Establecer título a la ventana
pygame.display.set_caption('Asteroides☄️')

# Establecer colo de fono de la ventada con rgb
colorFondo = (250, 126, 16)

# Colores de los objetos
colorFigurasEstandar = (169, 167, 165)
colorCuadro1 = (149, 60, 60)
colorTexto = (0, 0, 0)
colorTextoTiempo = (64, 64, 64)

# Variables
velocidad = 10
direccion = True
posX1, posY1 = randint(40, 700), randint(40, 500)
posX2, posY2 = randint(40, 700), randint(40, 500)
lados = 40
cadenaAlerta = "Sin novedades"
cadenaTiempo = "Tiempo:"

# Establecar las propietades del texto
tamaño = 15
fuente = pygame.font.SysFont("Consolas", tamaño)

# Configurar el texto
texto = fuente.render(cadenaAlerta, True, colorTexto)
textoTiempoLeyenda = fuente.render(cadenaTiempo, True, colorTextoTiempo)

# Bucle que mantiene la ventana abierta y donde se puede hacer todo sjsjj
while True:
    # Agregar los objetos a la ventana 
    # Establecer el colo de fondo
    ventana.fill(colorFondo)
    
    # Mostrar texto
    ventana.blit(texto, (15, 15))
    ventana.blit(textoTiempoLeyenda, (530, 15))
    
    #Obtener el tiempo y mostrarlo
    tiempo = pygame.time.get_ticks() / 1000
    textoTiempo = fuente.render(str(int(tiempo)), True, colorTextoTiempo)
    ventana.blit(textoTiempo, (600, 15))
    
    cuadro1 = pygame.draw.rect(ventana, colorFigurasEstandar, (posX1, posY1, lados, lados))
    cuadro2 = pygame.draw.rect(ventana, colorCuadro1, (posX2, posY2, lados, lados))
    
    # Eventos de movimiento por el mause
    posX1, posY1 = pygame.mouse.get_pos()
    posX1 = posX1 - (lados / 2)
    posY1 = posY1 - (lados / 2)
    
    # Limites del movimiento de los cuadros
    # Cuadro 1
    if posX1 <= 40: 
        posX1 = 40
    elif posX1 >= 620:
        posX1 = 620
        
    if posY1 <= 40:
        posY1 = 40
    elif posY1 >= 420:
        posY1 = 420
    
    # Cuadro 2
    if posX2 <= 40: 
        posX2 = 40
    elif posX2 >= 620:
        posX2 = 620
        
    if posY2 <= 40:
        posY2 = 40
    elif posY2 >= 420:
        posY2 = 420
        
    # Detección de choque entre cuadros
    if cuadro1.colliderect(cuadro2):
        #print(f"🤯 Alerta, colisión en X = {posX1} : Y =  {posY1}")
        posX2, posY2 = randint(40, 700), randint(40, 500)
        cuadro2.left = posX2-(lados/2)
        cuadro2.top = posY2-(lados/2)
        # Imprimir el aviso en pantalla
        cadenaAlerta = f"Alerta, colisión en X = {posX1} : Y = {posY1}"
        texto = fuente.render(cadenaAlerta, True, colorTexto)
        
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