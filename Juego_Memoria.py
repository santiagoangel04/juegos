#Esta version sus parejas son hechas con letras de la A a la H
#Si desea ver la version con imagenes, dirijase a la carpeta
#"Juego con imagenes" y ejecute ese script de python que se
#Encuentra en esa carpeta
import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Configuracion de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Juego de Memoria")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Letras para las cartas
def create_letters():
    letters = list("ABCDEFGH") * 2  # Dos de cada letra
    random.shuffle(letters)
    return letters

# Funcion para dibujar la pantalla de victoria
def draw_victory_screen():
    screen.fill(WHITE)
    font = pygame.font.Font(None, 74)
    victory_text = font.render("¡Ganaste!", True, BLACK)
    restart_text = font.render("Presiona R para reiniciar", True, BLACK)
    quit_text = font.render("Presiona Q para salir", True, BLACK)

    screen.blit(victory_text, (width // 2 - victory_text.get_width() // 2, height // 3))
    screen.blit(restart_text, (width // 2 - restart_text.get_width() // 2, height // 2))
    screen.blit(quit_text, (width // 2 - quit_text.get_width() // 2, height // 1.5))
    pygame.display.flip()

# Funcion para dibujar las cartas
def draw_board(revealed, letters, score):
    screen.fill(WHITE)
    for i in range(len(letters)):
        x = (i % 4) * 150 + 50
        y = (i // 4) * 150 + 50
        if revealed[i]:
            # Dibuja el contorno negro
            pygame.draw.rect(screen, BLACK, (x, y, 100, 100), 2)  # Contorno de 2 píxeles
            pygame.draw.rect(screen, WHITE, (x + 2, y + 2, 96, 96))  # Fondo de la carta
            font = pygame.font.Font(None, 74)
            text = font.render(letters[i], True, BLACK)
            screen.blit(text, (x + 25, y + 10))
        else:
            pygame.draw.rect(screen, GRAY, (x, y, 100, 100))
    
    # Mostrar puntuacion
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Puntuación: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()

# Bucle principal del juego
def main():
    letters = create_letters()
    revealed = [False] * len(letters)
    first_selection = None
    second_selection = None
    score = 0
    pause = False
    pause_start_time = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not pause:
                mouse_x, mouse_y = event.pos
                card_index = (mouse_x // 150) + (mouse_y // 150) * 4

                if not revealed[card_index]:
                    revealed[card_index] = True

                    if first_selection is None:
                        first_selection = card_index
                    elif second_selection is None:
                        second_selection = card_index

                        # Verificar si hay pareja
                        if letters[first_selection] == letters[second_selection]:
                            score += 1
                            # Mantener las cartas descubiertas
                            first_selection = None
                            second_selection = None
                        else:
                            pause = True
                            pause_start_time = pygame.time.get_ticks()

            # Manejo de la pausa que se hace para que el usuario pueda ver
            # las cartas por 1 segundo y despues de cubran de nuevo dado
            # el caso haya seleccionado una pareja erronea
            if pause:
                current_time = pygame.time.get_ticks()
                if current_time - pause_start_time >= 1000:  # 1000 ms = 1 segundo
                    # Ocultar las cartas si no son una pareja
                    if first_selection is not None and second_selection is not None:
                        revealed[first_selection] = False
                        revealed[second_selection] = False
                    
                    # Reiniciar selecciones
                    first_selection = None
                    second_selection = None
                    # Reiniciar la pausa
                    pause = False

        # Comprobar si se ha ganado, el tablero permite llegar hasta 8 puntos
        # Por lo que solo es necesario comprobar si es mayor o igual a 8 para ganar
        if score >= 8:
            draw_victory_screen()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:  # Reiniciar juego
                            main()  # Reiniciar la funcion principal
                        elif event.key == pygame.K_q:  # Salir
                            pygame.quit()
                            sys.exit()
            continue

        draw_board(revealed, letters, score)

# Iniciar el juego
main()
