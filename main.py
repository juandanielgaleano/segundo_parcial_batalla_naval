import pygame


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
nivel_rect = pygame.Rect(150,400,100,20)
jugar_rect = pygame.Rect(150,370,100,20)
ver_puntaje_rect = pygame.Rect(150,340,100,20)
salir_rect = pygame.Rect(150,310,100,20)
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    pantalla.blit(fondo, (0, 0))
    pygame.draw.rect(pantalla,(127,240,10),nivel_rect)
    pygame.draw.rect(pantalla,(240,240,10),jugar_rect)
    pygame.draw.rect(pantalla,(100,240,10),ver_puntaje_rect)
    pygame.draw.rect(pantalla,(20,240,10),salir_rect)
    pygame.display.flip()

    #for i in range(1, 10):
     #   y = i * alto_celda
      #  pygame.draw.line(pantalla, (255, 255, 255), (0, y), (ancho, y), 2)

    
    #for j in range(1, 10):
     #   x = j * ancho_celda
      #  pygame.draw.line(pantalla, (255, 255, 255), (x, 0), (x, alto), 2)

    
    
    pygame.display.update()