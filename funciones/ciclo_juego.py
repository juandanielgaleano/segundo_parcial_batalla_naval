import pygame

def iniciar_ciclo():

    pygame.init()
    ancho = 800
    alto = 600
    pantalla = pygame.display.set_mode((ancho, alto))
    fondo = pygame.image.load("resources\water.png")
    fondo = pygame.transform.scale(fondo,(800,600))
    pygame.display.set_icon(pygame.image.load("resources\ship.png"))
    pygame.display.set_caption("BATALLA NAVAL")
    ancho_celda = ancho // 10
    alto_celda = alto // 10
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

        pantalla.blit(fondo, (0, 0))
        pygame.display.flip()

        for i in range(1, 10):
            y = i * alto_celda
            pygame.draw.line(pantalla, (255, 255, 255), (0, y), (ancho, y), 2)

        
        for j in range(1, 10):
            x = j * ancho_celda
            pygame.draw.line(pantalla, (255, 255, 255), (x, 0), (x, alto), 2)

    
    
        pygame.display.update()