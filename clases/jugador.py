import pygame
from clases import disparo

# Clase nave
class Nave(pygame.sprite.Sprite):
    # Inicializar clase (Constructor)
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagenNave = pygame.image.load('resources/img/nave.png')
        self.naveDestruida = pygame.image.load('resources/img/explosionNave.png')
        
        # Tomar el cuadrado que ocupa la imagen
        self.rect = self.imagenNave.get_rect()
        
        # Posición inicial de la nave
        self.rect.centerx = 350
        self.rect.centery = 445
        self.velocidad = 25
        self.vida = True
        self.disparosHechos = []
        
        # Sonidos
        self.sodinoDisparo = pygame.mixer.Sound('resources/sounds/disparo.wav')
        
    # Método para el movimineto
    def mover(self):
        if self.vida == True:
            if self.rect.left <= 10:
                self.rect.left = 10
            elif self.rect.right >= 690:
                self.rect.right = 690
       
    # Método para el disparo         
    def disparo(self, x, y):
        if self.vida == True:
            #print("Disparo✨")
            misil = disparo.Misil(x, y)
            self.disparosHechos.append(misil)
            self.sodinoDisparo.play()
        
    # Método para mostar la nave
    def mostrar(self, superficie):
        if self.vida == True:
            superficie.blit(self.imagenNave, self.rect)
        else:
            superficie.blit(self.naveDestruida, self.rect)