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
        elif event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        else:
            if music:
                pygame.mixer.music.fadeout(1500)
            else:
                pygame.time.wait(1500)
            break
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if music:
            pygame.mixer.music.fadeout(1500)
        else:
            pygame.time.wait(1500)
        break
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
    board.append([None, None, None, None, None, None, None, None, None, None])
selected = [None, None, None, None]
neighbors = {}
for r in range(18):
    for c in range(10):
        neighbors[(25 * c, 395 - 25 * r, 25, 10)] = [(25 * c - 25, 395 - 25 * r, 25, 10), (25 * c + 25, 395 - 25 * r, 25, 10), (5 + 25 * c, 380 - 25 * r, 15, 15), (5 + 25 * c, 405 - 25 * r, 15, 15)]
    if ((x % 25) + 10) / 15 == 1:
        return (5 + 25 * r, 380 - 25 * r, 15, 15)
mousePressed = False
spacePressed = False

screen.fill((255, 255, 255))
for loc in selected:
    if loc != None:
        r, c = loc
        pygame.draw.rect(screen, (0, 155, 255), (25 * c, 25 * r, 25, 25))
for r in range(16):
    for c in range(10):
        if board[r][c] != None:
            pygame.draw.rect(screen, board[r][c], (5 + 25 * c, 5 + 25 * r, 15, 15))
pygame.display.update()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mousePressed = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mousePressed = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    spacePressed = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = 0
                    screen.fill((255, 255, 255))
                    for loc in selected:
                        if loc != None:
                            r, c = loc
                            pygame.draw.rect(screen, (0, 155, 255), (25 * c, 25 * r, 25, 25))
                    for r in range(16):
                        for c in range(10):
                            if board[r][c] != None:
                                pygame.draw.rect(screen, board[r][c], (5 + 25 * c, 5 + 25 * c, 15, 15))
                    pygame.display.update()
                    clock.tick(40)
                    break
                elif event.key == pygame.K_SPACE:
                    spacePressed = True
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
        changes = []
        if mousePressed:
            x, y = pygame.mouse.get_pos()
            loc = getCellLocation(x, y)
            if loc != None and (loc[2] == 15 or spacePressed):
                if selected[0] = None:
                    selected[0] = loc
                    changes.appned(loc)
                    
        else:
            pass
        while True:
            event = pygame.event.poll()
            if event.type == pygame.NOEVENT:
                break
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mousePressed = True
##                    for loc in selected:
##                        if loc == None:
##                            break;
##                        r, c = loc
##                        if r.imag != 0:
##                            r = r.real
##                            changes.append((0, 395 - 25 * r, 250, 10))
##                        else:
##                            changes.append((25 * c, 375 - 25 * r, 25, 25))
                    selected = [None, None, None, None]
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mousePressed = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    spacePressed = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = 1
                    break
                elif event.key == pygame.K_SPACE:
                    spacePressed = True
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
        pygame.display.update(changes)
        changes = []
        clock.tick(40)

def getCellLocation(x, y):
    r, c = (400 - y) / 25, x / 25
    if (400 - y) % 25 <= 5:
        return (25 * c, 395 - 25 * r, 25, 10)
    if (400 - y) % 25 >= 20:
        return (25 * c, 370 - 25 * r, 25, 10)
    if ((x % 25) + 10) / 15 == 1:
        return (5 + 25 * r, 380 - 25 * r, 15, 15)
    return None
