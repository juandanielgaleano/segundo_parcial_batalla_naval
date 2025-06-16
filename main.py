import pygame


pygame.init()

pantalla = pygame.display.set_mode((800, 600))
fondo = pygame.image.load("resources\water.png")
fondo = pygame.transform.scale(fondo,(800,600))
pygame.display.set_icon(pygame.image.load("resources\ship.png"))
pygame.display.set_caption("BATALLA NAVAL")

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()

    pantalla.blit(fondo, (0, 0))
    pygame.display.flip()

    
    
    pygame.display.update()