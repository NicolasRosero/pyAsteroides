import  pygame, sys
from pygame.locals import *
from random import randint
import time

# Importación de clases propias
from clases import jugador
from clases import asteroide

# Tamaño de la pantalla
alto = 500
ancho = 700

# Arreglo para los asteroides
listaAsteroides = []

# Comprobar si estamos en juego
estadoJugando = True

# Marcador de puntaje
puntos = 0

# Colores para las fuentes
colorFuenteMarcador = (255, 255, 255)
coloTextoGameOver = (255, 0, 0)

# Método para mostrar los asteroides dentro de la ventana principal
def lazarAsteroides(x, y):
    roca = asteroide(x, y)
    listaAsteroides.append(roca)

def gameOver():
    global estadoJugando
    estadoJugando = False
    for asteroides in listaAsteroides:
        listaAsteroides.remove(asteroides)

# Función principal para inicializar el juego
def asteroides():
    # Inicializar pygame
    pygame.init()
    
    # Sonidos
    sonidoExplosionNave = pygame.mixer.Sound('resources/sounds/explosionNave.mp3')
    sonidoExplosionAsteroide = pygame.mixer.Sound('resources/sounds/explosionAsteroide.wav')
    
    # Fuentes para los textos
    fuenteMarcador = pygame.font.SysFont("Consolas", 17)
    
    # Creación de la ventana y su tamaño
    ventana = pygame.display.set_mode((ancho, alto))
    
    # Título del juego
    pygame.display.set_caption('Asteroides')
    #Establecer icono
    icono = pygame.image.load('resources/img/IconoVentana.png')
    pygame.display.set_icon(icono)
    
    # Objetos y flujo del juego
    # Establacer el fondo
    fondo = pygame.image.load('resources/img/fondo.jpg')
    
    # Traer al jugador
    nave = jugador.Nave()
    
    # Contador de los asteroides
    contador = 0
    
    # Ejecución de la ventana y ciclo del juego
    while True:
        # Cargar el fondo primero
        ventana.blit(fondo, (0,0))
        
        # Agregar la nave a la ventana
        nave.mostrar(ventana)
        nave.mover()
        
        # Texto del marcador
        global puntos
        textoMarcador = fuenteMarcador.render(f"Puntos: {str(puntos)}", True, colorFuenteMarcador)
        ventana.blit(textoMarcador, (15, 15))
        
        # Tiempo de juego
        tiempo = time.time() * 3
        
        # Crear asteroides
        if tiempo - contador > 1:
            contador = tiempo
            posXA = randint(-50, 700)
            lazarAsteroides(posXA, -700)
            
        # Comprobar si hay asteroides
        if len(listaAsteroides) > 0:
            for x in listaAsteroides:
                if estadoJugando == True:
                    x.mostrarAsteroide(ventana)
                    x.recorridoAsteroide()
                if x.rect.top > 720:
                    listaAsteroides.remove(x)
                else:
                    # Validar si el asteroide da a la nave y destruir
                    if x.rect.colliderect(nave):
                        listaAsteroides.remove(x)
                        sonidoExplosionNave.play()
                        nave.vida = False
                        gameOver()
        
        # Comprobar si se ha hecho un disparo
        if len(nave.disparosHechos) > 0:
            for x in nave.disparosHechos:
                x.mostrarMisil(ventana)
                x.recorridoMisil()
                # Validar si el asteroide supera el limite de la pantalla
                if x.rect.top < -10:
                    nave.disparosHechos.remove(x)
                else:
                    # Validar si el misil da al asteride y destruir
                    for asteroides in listaAsteroides:
                        if x.rect.colliderect(asteroides.rect):
                            sonidoExplosionAsteroide.play()
                            listaAsteroides.remove(asteroides)
                            nave.disparosHechos.remove(x)
                            puntos += 1
        
        for evento in pygame.event.get():
            # Validar si se presiona la X de la ventana para cerrar el juego
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == KEYDOWN:
                if estadoJugando == True:
                    if evento.key == K_LEFT:
                        nave.rect.left -= nave.velocidad
                    elif evento.key == K_RIGHT:
                        nave.rect.right += nave.velocidad
                    elif evento.key == K_SPACE:
                        x, y = nave.rect.center
                        nave.disparo((x - 10 ), (y - 30))
        
        # Validar si aún se sigue jugando
        if estadoJugando == False:
            fuenteGameOver = pygame.font.SysFont("Consolas", 40)
            textoGameOver = fuenteGameOver.render("Fin del juego", True, coloTextoGameOver)
            ventana.blit(textoGameOver, (220, 204))
            pygame.mixer.fadeout(1000)
         
        # Mantener actualizadoel juego                
        pygame.display.update()

# Llamado a la función asteroides para ejecutar el juego
asteroides()
