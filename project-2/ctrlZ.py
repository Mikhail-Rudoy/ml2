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

board = {}
for i in range(-4, 16):
    board[i] = [(0, 0, 0), None, None, None, None, None, None, None, None, None]
selected = [None]
piece = [None, None, None, None]
path = []

mousePressed = False
spacePressed = False

screen.fill((255, 255, 255))
tmp = []
for loc in selected:
    if loc != None:
        r, c = loc
        if r == int(r):
            pygame.draw.rect(screen, (0, 155, 255), (25 * c, 25 * r, 25, 25))
        else:
            tmp.append(loc)
            pygame.draw.rect(screen, (0, 200, 0), (0, 25 * int(r) + 22, 250, 6))
for loc in tmp:
    r, c = loc
    pygame.draw.rect(screen, (0, 0, 255), (25 * c, 25 * int(r) + 20, 25, 10))
del tmp
for loc in piece:
    if loc != None:
        r, c, col = loc
        pygame.draw.rect(screen, col, (25 * c, 25 * r, 25, 25))
del loc
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = 0
                    screen.fill((255, 255, 255))
                    tmp = []
                    for loc in selected:
                        if loc != None:
                            r, c = loc
                            if r == int(r):
                                pygame.draw.rect(screen, (0, 155, 255), (25 * c, 25 * r, 25, 25))
                            else:
                                tmp.append(loc)
                                pygame.draw.rect(screen, (0, 200, 0), (0, 25 * int(r) + 22, 250, 6))
                    for loc in tmp:
                        r, c = loc
                        pygame.draw.rect(screen, (0, 0, 255), (25 * c, 25 * int(r) + 20, 25, 10))
                    del tmp
                    for loc in piece:
                        if loc != None:
                            r, c, col = loc
                            pygame.draw.rect(screen, col, (25 * c, 25 * r, 25, 25))
                    del loc
                    for r in range(16):
                        for c in range(10):
                            if board[r][c] != None:
                                pygame.draw.rect(screen, board[r][c], (5 + 25 * c, 5 + 25 * r, 15, 15))
                    pygame.display.update()
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
        if mousePressed:
            x, y = pygame.mouse.get_pos()
            if ((y % 25) + 10) / 15 == 1:
                if ((x % 25) + 10) / 15 == 1:
                    loc = (y / 25, x / 25)
                    r, c = loc
                    if board[r][c]:
                        if selected[0] == None:
                            selected[0] = loc
                        else:
                            dr, dc =  r - selected[0][0], c - selected[0][1]
                            if (abs(dr) <= 1.000001 and dc == 0) or (abs(dc) == 1 and dr == 0):
                                selected = [loc] + [itm for itm in selected if itm != loc]
                                if len(selected) == 5:
                                    itm = selected[4]
                                    selected = selected[:4]
                                    if itm[0] == int(itm[0]):
                                        pygame.draw.rect(screen, (255, 255, 255), (25 * itm[1], 25 * itm[0], 25, 25))
                                        if board[itm[0]][itm[1]]:
                                            pygame.draw.rect(screen, board[itm[0]][itm[1]], (5 + 25 * itm[1], 5 + 25 * itm[0], 15, 15))
                                        pygame.display.update((25 * itm[1], 25 * itm[0], 25, 25))
                                    else:
                                        pygame.draw.rect(screen, (255, 255, 255), (0, 25 * int(itm[0]) + 20, 250, 10))
                                        pygame.display.update((0, 25 * int(itm[0]) + 20, 250, 10))
            else:
                loc = ((y - 10) / 25 + 0.5, x / 25)
                r, c = loc
                if selected[0] == None:
                    if spacePressed:
                        selected[0] = loc
                else:
                    dr, dc = r - selected[0][0], c - selected[0][1]
                    if (abs(dc) == 1 and dr == 0) or (abs(dr) == 0.5 and dc == 0 and spacePressed):
                        spacePressed = 0
                        selected = [loc] + [itm for itm in selected if itm and itm != loc]
                        if len(selected) == 5:
                            itm = selected[4]
                            selected = selected[:4]
                            if itm[0] == int(itm[0]):
                                pygame.draw.rect(screen, (255, 255, 255), (25 * itm[1], 25 * itm[0], 25, 25))
                                if board[itm[0]][itm[1]]:
                                    pygame.draw.rect(screen, board[itm[0]][itm[1]], (5 + 25 * itm[1], 5 + 25 * itm[0], 15, 15))
                                pygame.display.update((25 * itm[1], 25 * itm[0], 25, 25))
                            else:
                                pygame.draw.rect(screen, (255, 255, 255), (0, 25 * int(itm[0]) + 20, 250, 10))
                                pygame.display.update((0, 25 * int(itm[0]) + 20, 250, 10))
        else:
            print selected
            already, notyet = [itm for itm in selected if itm and itm[0] == int(itm[0])], [itm for itm in selected if itm and itm[0] != int(itm[0])]
            if (len(notyet) == 0 and len(already) != 4) or (len(already) > 0 and not [board[r][c] for (r, c) in already if board[r][c] != board[already[0][0]][already[0][1]]]):
                for itm in already:
                    pygame.draw.rect(screen, (255, 255, 255), (25 * itm[1], 25 * itm[0], 25, 25))
                    if board[itm[0]][itm[1]]:
                        pygame.draw.rect(screen, board[itm[0]][itm[1]], (5 + 25 * itm[1], 5 + 25 * itm[0], 15, 15))
                    pygame.display.update((25 * itm[1], 25 * itm[0], 25, 25))
                for itm in notyet:
                    pygame.draw.rect(screen, (255, 255, 255), (0, 25 * int(itm[0]) + 20, 250, 10))
                    pygame.display.update((0, 25 * int(itm[0]) + 20, 250, 10))
                pygame.mixer.Sound("Buzzer.mp3").play()
                selected = [None]
                    
        
        if spacePressed:
            spacePressed = spacePressed - 1

        tmp = []
        for loc in selected:
            if loc != None:
                r, c = loc
                if r == int(r):
                    pygame.draw.rect(screen, (0, 155, 255), (25 * c, 25 * r, 25, 25))
                    if board[r][c]:
                        pygame.draw.rect(screen, board[r][c], (5 + 25 * c, 5 + 25 * r, 15, 15))
                    pygame.display.update((25 * c, 25 * r, 25, 25))
                else:
                    tmp.append(loc)
                    pygame.draw.rect(screen, (0, 200, 0), (0, 25 * int(r) + 22, 250, 6))
        for loc in tmp:
            r, c = loc
            pygame.draw.rect(screen, (0, 0, 255), (25 * c, 25 * int(r) + 20, 25, 10))
            pygame.display.update((0, 25 * int(r) + 20, 250, 10))
        del tmp
        for loc in piece:
            if loc != None:
                r, c, col = loc
                pygame.draw.rect(screen, col, (25 * c, 25 * r, 25, 25))
                pygame.display.update((25 * c, 25 * r, 25, 25))
        del loc

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
                    already, notyet = [itm for itm in selected if itm and itm[0] == int(itm[0])], [itm for itm in selected if itm and itm[0] != int(itm[0])]
                    for itm in already:
                        pygame.draw.rect(screen, (255, 255, 255), (25 * itm[1], 25 * itm[0], 25, 25))
                        if board[itm[0]][itm[1]]:
                            pygame.draw.rect(screen, board[itm[0]][itm[1]], (5 + 25 * itm[1], 5 + 25 * itm[0], 15, 15))
                        pygame.display.update((25 * itm[1], 25 * itm[0], 25, 25))
                    for itm in notyet:
                        pygame.draw.rect(screen, (255, 255, 255), (0, 25 * int(itm[0]) + 20, 250, 10))
                        pygame.display.update((0, 25 * int(itm[0]) + 20, 250, 10))
                    selected = [None]
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mousePressed = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = 1
                    break
                elif event.key == pygame.K_SPACE:
                    spacePressed = 30
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
        clock.tick(40)
