import pygame

class Misil(pygame.sprite.Sprite):
    # Constructor de la clase
    def __init__(self, posX, posY):
        pygame.sprite.Sprite.__init__(self)
        
        # Obtener la imagen del misil
        self.imagenMisil = pygame.image.load('resources/img/misil.png')
        
        # Tomar el cuadro que ocupa la imagen
        self.rect = self.imagenMisil.get_rect()
        self.velocidad = 2
        
        # Ubicar el misil según la posición de la nave
        self.rect.top = posY
        self.rect.left = posX
        
    # Método para el recorrido del misil
    def recorridoMisil(self):
        self.rect.top = self.rect.top - self.velocidad
        
    # Método para mostrar el misil
    def mostrarMisil(self, superficie):
        superficie.blit(self.imagenMisil, self.rect)