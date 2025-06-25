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

    
    color_texto= (0, 0, 0)
    salir_rect = pygame.Rect(150,400,100,20)
    ver_puntaje_rect = pygame.Rect(150,370,100,20)
    jugar_rect = pygame.Rect(150,340,100,20)
    nivel_rect = pygame.Rect(150,310,100,20)

    fuente = pygame.font.SysFont('Arial', 24)
    
    texto_nivel = fuente.render("Nivel", True, color_texto)
    texto_jugar = fuente.render("Jugar", True, color_texto)
    texto_puntaje = fuente.render("Ver Puntaje", True, color_texto)    
    texto_salir = fuente.render("Salir", True, color_texto)
    
    
    
    dificultad = 0
    opciones = ["Nivel","Jugar","Ver Puntajes","Salir"]
    opcion = 0

    while True:
        for evento in pygame.event.get():
            
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_DOWN:
                    if opcion == 3:
                        opcion = 0
                        print(opciones[opcion])
                    else:
                        opcion = opcion + 1
                        print(opciones[opcion])

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    if opcion == 0:
                        opcion = 3
                        print(opciones[opcion])
                    else:
                        opcion = opcion -1
                        print(opciones[opcion])

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    print(opciones[opcion])
                    match opciones[opcion]:
                        case "Nivel":
                            print("Seleccionar dificultad")
                        case "Jugar":
                            print("Jugar")
                        case "Ver Puntajes":
                            print("Ver puntajes")

                        case "Salir":
                            print("Salir")
                            pygame.quit()
                            quit()



        pantalla.blit(fondo, (0, 0))
        pygame.draw.rect(pantalla, (230, 230, 230), nivel_rect)        
        pygame.draw.rect(pantalla, (230, 230, 230), jugar_rect)        
        pygame.draw.rect(pantalla, (230, 230, 230), ver_puntaje_rect)  
        pygame.draw.rect(pantalla, (50, 50, 50), salir_rect)  

        pantalla.blit(texto_nivel, (nivel_rect.centerx - texto_nivel.get_width()//2, nivel_rect.centery - texto_nivel.get_height()//2))
        pantalla.blit(texto_jugar, (jugar_rect.centerx - texto_jugar.get_width()//2, jugar_rect.centery - texto_jugar.get_height()//2))
        pantalla.blit(texto_puntaje, (ver_puntaje_rect.centerx - texto_puntaje.get_width()//2, ver_puntaje_rect.centery - texto_puntaje.get_height()//2))
        pantalla.blit(texto_salir, (salir_rect.centerx - texto_salir.get_width()//2, salir_rect.centery - texto_salir.get_height()//2))
        
        
        

        pygame.display.flip()

        #for i in range(1, 10):
        #    y = i * alto_celda
        #    pygame.draw.line(pantalla, (255, 255, 255), (0, y), (ancho, y), 2)


        #for j in range(1, 10):
        #    x = j * ancho_celda
        #    pygame.draw.line(pantalla, (255, 255, 255), (x, 0), (x, alto), 2)

    
    
        pygame.display.update()