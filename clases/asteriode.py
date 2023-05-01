import pygame

class asteroide(pygame.sprite.Sprite):
    # Constructor de la clase
    def __init__(self, posX, posY):
        pygame.sprite.Sprite.__init__(self)
        
        # Obtener la imagen del asteroide
        self.imagenAsteroide = pygame.image.load('resources/img/asteroide.png')
        self.asterodieDestruido = pygame.image.load('resources/img/explosionAsteroide.png')
        
        # Tomar el cuadro de la imagen
        self.rect = self.imagenAsteroide.get_rect()
        self.velocidad = 1
        
        # Posicionar el asteroide
        self.rect.top = posY
        self.rect.left = posX
        
        # Lista de asteroides
        self.listaAsteroides = []
        
    # Método para el movimiento de los asteroides 
    def recorridoAsteroide(self):
        self.rect.top = self.rect.top + self.velocidad
        
    # Método para mostrar el asteroide
    def mostrarAsteroide(self, superfice):
        superfice.blit(self.imagenAsteroide, self.rect)
        
    # Método para mostrar el asteroide destruido