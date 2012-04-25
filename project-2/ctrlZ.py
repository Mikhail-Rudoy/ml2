import pygame, sys

pygame.init()
screen = pygame.display.set_mode((250, 400))
clock = pygame.time.Clock()

pygame.display.set_caption("Ctrl-Z")

paused = 0
pauseText = pygame.font.Font(None, 35).render("Press \"p\" to unpause", True, (255, 255, 255))

screen.fill((255, 255, 255))
screen.blit(pygame.image.load("title.gif").convert(), (0, 90))
screen.blit(pygame.font.Font(None, 40).render("By Mikhail Rudoy", True, (0, 0, 0)), (7, 210))
pygame.display.update()

music = True
pygame.mixer.music.load("song.mp3")
pygame.mixer.music.play(-1)

while True:
    event = pygame.event.poll()
    if event.type == pygame.NOEVENT:
        pass
    elif event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_m:
            if music:
                music = False
                pygame.mixer.music.pause()
            else:
                music = True
                pygame.mixer.music.unpause()
        elif event.key == pygame.K_SPACE:
            if music:
                pygame.mixer.music.fadeout(2000)
            else:
                pygame.time.wait(2000)
            break
        elif event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        else:
            continue
    else:
        continue
    clock.tick(4)
    del event

music = True
pygame.mixer.music.load("song.wav")
pygame.mixer.music.play(-1)
if not music:
    pygame.mixer.music.pause()

board = []
for i in range(18):
    board.append([(100, 100, 100), None, None, None, None, None, None, None, None, None])

selected = [(1, 1), None, None, None]

screen.fill((255, 255, 255))
for loc in selected:
    if loc != None:
        r, c = loc
        pygame.draw.rect(screen, (0, 0, 255), (25 * c, 25 * r, 25, 25))
for r in range(16):
    for c in range(10):
        if board[r][c] != None:
            pygame.draw.rect(screen, board[r][c], (5 + 25 * c, 5 + 25 * c, 15, 15))
python.display.update()
clock.tick(40)

while True:
    if paused:
        if paused == 1:
            screen.fill((0, 0, 0))
            screen.blit(pauseText, (1, 170))
            paused = 2
            pygame.display.update()
        while True:
            event = pygame.event.poll()
            if event.type == pygame.NOEVENT:
                break
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = 0
                    screen.fill((255, 255, 255))
                    for loc in selected:
                        if loc != None:
                            r, c = loc
                            pygame.draw.rect(screen, (0, 0, 255), (25 * c, 25 * r, 25, 25))
                    for r in range(16):
                        for c in range(10):
                            if board[r][c] != None:
                                pygame.draw.rect(screen, board[r][c], (5 + 25 * c, 5 + 25 * c, 15, 15))
                    python.display.update()
                    clock.tick(40)
                    break
                elif event.key == pygame.K_m:
                    if music:
                        music = False
                        pygame.mixer.music.pause()
                    else:
                        music = True
                        pygame.mixer.music.unpause()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        del event
        clock.tick(10)
    else:
        screen.fill((255, 255, 255))
        while True:
            event = pygame.event.poll()
            if event.type == pygame.NOEVENT:
                break
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = 1
                    break
                elif event.key == pygame.K_m:
                    if music:
                        music = False
                        pygame.mixer.music.pause()
                    else:
                        music = True
                        pygame.mixer.music.unpause()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        del event
        pygame.display.update()
        clock.tick(40)
