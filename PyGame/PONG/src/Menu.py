import pygame
from .pong import PongGame

pygame.init()
pygame.mixer.init()


def Inicio():
    Tamano = (800, 450)
    ventana = pygame.display.set_mode(Tamano)

    ImgInicio = pygame.image.load("/assets/Presentation.jpg")

    # Redimensionar la imagen al tamaño de la ventana
    ImgInicio = pygame.transform.scale(ImgInicio, Tamano)

    ventana.blit(ImgInicio, (0, 0))

    pygame.display.flip()
    pygame.time.delay(1200)

    Menu()


#OPCION 1 MENU
def Menu():
    Tamano = (800, 450)
    ventana = pygame.display.set_mode(Tamano)
    ImgInicio = pygame.image.load("/assets/Menu.jpg")
    ventana.blit(ImgInicio, (0, 0))
    running = True

    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # ACTIVAR BOTONES
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                
                if pos[0] > 162 and pos[0] < 555 and pos[1] > 151 and pos[1] < 228:
                    print("Entra JUGAR")
                    Jugar()
                    running = False

        pygame.display.flip()

    pygame.quit()

def Ayuda():
    Tamano = (800, 450)
    ventana = pygame.display.set_mode(Tamano)
    ImgAyuda = pygame.image.load("/assets/Help.jpg")
    ventana.blit(ImgAyuda, (0, 0))
    running = True

    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)

                # BOTON VOLVER
                #if pos[0] > X1  and pos[0] < X2 and pos[1] > Y1 and pos[1] < Y2:
                    #Menu()
                    #running = False

        pygame.display.flip()


def Jugar():
    #AQUI VA EL CÓDIGO DEL JUEGO COMPLETO
    PongGame(800, 500)

    #CUANDO EL JUEGO TERMINE, DEBE LLAMAR A MENU()


if __name__ == '__main__':
    Inicio()