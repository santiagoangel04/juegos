# MemoryBC

Es un juego muy simple de memoria, donde ganas al obtener 8 puntos o 8 parejas, 
este juego fue desarrollado de manera veloz, dado las circunstacias, de manera que los que busca es dirversion y fortalecimiento cerebral.Cada letra está presente dos veces en el tablero, y el jugador debe seleccionarlas para formar parejas. Si las selecciones coinciden, las cartas permanecen descubiertas. Si no coinciden, se ocultan nuevamente después de un breve período.

este juego esta desarrollado con python y su libreria pygame

```
pip install pygame 
```
## Como puedo jugar
1. Ejecuta el programa.
2. Haz clic en dos cartas para intentar formar una pareja.
3. Si las cartas coinciden, se mantendrán descubiertas y sumarás puntos.
4. Si no coinciden, se ocultarán después de 1 segundo.
5. Gana cuando descubras todas las parejas.

## Generación de Cartas
```
def create_letters():
    letters = list("ABCDEFGH") * 2  # Dos de cada letra
    random.shuffle(letters)
    return letters
```
## Pausa
```
if pause:
    current_time = pygame.time.get_ticks()
    if current_time - pause_start_time >= 1000:  # 1000 ms = 1 segundo
        if first_selection is not None and second_selection is not None:
            revealed[first_selection] = False
            revealed[second_selection] = False
        first_selection = None
        second_selection = None
        pause = False
```
## Condición de Victoria
```
if score >= 8:
    draw_victory_screen()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Reiniciar juego
                    main()
                elif event.key == pygame.K_q:  # Salir
                    pygame.quit()
                    sys.exit()
    continue
```
## Dibujo del Tablero
```
def draw_board(revealed, letters, score):
    screen.fill(WHITE)
    for i in range(len(letters)):
        x = (i % 4) * 150 + 50
        y = (i // 4) * 150 + 50
        if revealed[i]:
            pygame.draw.rect(screen, BLACK, (x, y, 100, 100), 2)
            pygame.draw.rect(screen, WHITE, (x + 2, y + 2, 96, 96))
            font = pygame.font.Font(None, 74)
            text = font.render(letters[i], True, BLACK)
            screen.blit(text, (x + 25, y + 10))
        else:
            pygame.draw.rect(screen, GRAY, (x, y, 100, 100))
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Puntuación: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
```
## Pantalla de Victoria
Cuando el jugador gana, aparece una pantalla con las opciones de reiniciar o salir.