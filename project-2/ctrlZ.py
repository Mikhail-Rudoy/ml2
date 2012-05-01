import pygame, sys, random

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((250, 400))
clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
blockSelectionColor = (0, 155, 255)
lineSelectionColor = (0, 200, 0)
spaceSelectionColor = (0, 155, 255)

def colorBoard(brd, locs, clrs):
    random.shuffle(locs)
    for (r, c) in locs:
        if random.choice([1, 0]):
            brd[r][c] = random.choice(clrs)
        else:
            neigbors = [brd[r + ro][c + co] for (ro, co) in [(-1, 0), (1, 0), (0, 1), (0, -1)] \
                                            if r + ro < 16 and r + ro > -5 \
                                            if c + co < 10 and c + co >= 0 \
                                            if brd[r + ro, c + co]]
            if len(neighbors):
                brd[r][c] = random.choice(neighbors)
            else:
                brd[r][c] = random.choice(clrs)
        

pygame.display.set_caption("Ctrl-Z")

paused = 0
pauseText = pygame.font.Font(None, 35).render("Press \"p\" to unpause", True, white)

screen.fill(white)
screen.blit(pygame.image.load("title.gif").convert(), (0, 90))
screen.blit(pygame.font.Font(None, 40).render("By Mikhail Rudoy", True, black), (7, 210))
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

while pygame.event.poll().type != pygame.NOEVENT:
    pass

pygame.mixer.music.load("song.wav")
pygame.mixer.music.play(-1)
if not music:
    pygame.mixer.music.pause()

board = {}
for i in range(-4, 16):
    board[i] = [(50, 100, 0), (100, 0, 50)] + [None] * 8
selected = []
piece = [None, None, None, None]
path = []
numPieces = 0
moveDelay = 30
ticks = 30
colorRange = 2
colors = [(r, g, b) for r in range(0, 255, 50) \
                    for g in range(0, 255, 50) \
                    for b in range(0, 255, 50) \
                    if r != g and g != b and r != b]
random.shuffle(colors)
colors = colors[:10]


screen.fill(white)
tmp = []
for loc in selected:
    if loc != None:
        r, c = loc
        if r == int(r):
            pygame.draw.rect(screen, blockSelectionColor, (25 * c, 25 * r, 25, 25))
        else:
            tmp.append(loc)
for loc in tmp:
    r, c = loc
    pygame.draw.rect(screen, lineSelectionColor, (0, 25 * int(r) + 22, 250, 6))
for loc in tmp:
    r, c = loc
    pygame.draw.rect(screen, spaceSelectionColor, (25 * c, 25 * int(r) + 20, 25, 10))
del tmp
for loc in piece:
    if loc != None:
        r, c, col = loc
        pygame.draw.rect(screen, col, (25 * c, 25 * r, 25, 25))
del loc
for r in range(16):
    for c in range(10):
        if board[r][c]:
            pygame.draw.rect(screen, board[r][c], (5 + 25 * c, 5 + 25 * r, 15, 15))
pygame.display.update()
clock.tick(40)

beep = pygame.mixer.Sound("Buzzer.ogg")
mousePressed = False
spacePressed = False

while True:
    if paused:
        if paused == 1:
            screen.fill(black)
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
                    screen.fill(white)
                    tmp = []
                    for loc in selected:
                        if loc != None:
                            r, c = loc
                            if r == int(r):
                                pygame.draw.rect(screen, blockSelectionColor, (25 * c, 25 * r, 25, 25))
                            else:
                                tmp.append(loc)
                    for loc in tmp:
                        r, c = loc
                        pygame.draw.rect(screen, lineSelectionColor, (0, 25 * int(r) + 22, 250, 6))
                    for loc in tmp:
                        r, c = loc
                        pygame.draw.rect(screen, spaceSelectionColor, (25 * c, 25 * int(r) + 20, 25, 10))
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
                        if not selected:
                            selected = [loc]
                        else:
                            dr, dc =  r - selected[0][0], c - selected[0][1]
                            if (abs(dr) <= 0.500001 and dc == 0) or \
                               (abs(dr) == 1 and dc == 0 and not [1 for (ro, co) in selected \
                                                                if int(2 * ro) == r + selected[0][0] and \
                                                                   co != c]) or \
                               (abs(dc) == 1 and dr == 0):
                                selected = [loc] + [itm for itm in selected if itm != loc]
                                if len(selected) == 5:
                                    itm = selected[4]
                                    selected = selected[:4]
                                    if itm[0] == int(itm[0]):
                                        pygame.draw.rect(screen, white, (25 * itm[1], 25 * itm[0], 25, 25))
                                        if board[itm[0]][itm[1]]:
                                            pygame.draw.rect(screen, board[itm[0]][itm[1]], (5 + 25 * itm[1], 5 + 25 * itm[0], 15, 15))
                                        pygame.display.update((25 * itm[1], 25 * itm[0], 25, 25))
                                    else:
                                        pygame.draw.rect(screen, white, (0, 25 * int(itm[0]) + 20, 250, 10))
                                        pygame.display.update((0, 25 * int(itm[0]) + 20, 250, 10))
            else:
                loc = ((y - 10) / 25 + 0.5, x / 25)
                r, c = loc
                if not selected:
                    if spacePressed and \
                       not [1 for i in range(int(r) + 1, 16) \
                              if board[i] == [None,] * 10]:
                        selected = [loc]
                else:
                    dr, dc = r - selected[0][0], c - selected[0][1]
                    if (abs(dc) == 1 and dr == 0) or \
                       (abs(dr) == 0.5 and \
                         dc == 0 and \
                         (r in [ro for (ro, co) in selected] or \
                          (spacePressed and \
                           not [c1 for (r1, c1) in selected \
                                   for (r2, c2) in selected \
                                   if c1 == c2 \
                                   if int(r) in [r1, r2] \
                                   if int(r) + 1 in [r1, r2] \
                                   if c1 != c \
                                   if not c1 in [co for (ro, co) in selected \
                                                    if ro == r]]))):
                        spacePressed = 0
                        selected = [loc] + [itm for itm in selected if itm and itm != loc]
                        if len(selected) == 5:
                            itm = selected[4]
                            selected = selected[:4]
                            if itm[0] == int(itm[0]):
                                pygame.draw.rect(screen, white, (25 * itm[1], 25 * itm[0], 25, 25))
                                if board[itm[0]][itm[1]]:
                                    pygame.draw.rect(screen, board[itm[0]][itm[1]], (5 + 25 * itm[1], 5 + 25 * itm[0], 15, 15))
                                pygame.display.update((25 * itm[1], 25 * itm[0], 25, 25))
                            else:
                                pygame.draw.rect(screen, white, (0, 25 * int(itm[0]) + 20, 250, 10))
                                pygame.display.update((0, 25 * int(itm[0]) + 20, 250, 10))
        elif selected:
            already = [itm for itm in selected if itm and itm[0] == int(itm[0])]
            notyet = [itm for itm in selected if itm and itm[0] != int(itm[0])]
            if (len(notyet) == 0 and len(already) != 4) or \
               (len(already) > 0 and [1 for (r, c) in already \
                                        if board[r][c] != \
                                           board[already[0][0]][already[0][1]]]) or \
               (not [(r + 1, c) for (r, c) in already \
                                if not (r + 1, c) in selected \
                                if (r + 1 == 16 or \
                                    board[r + 1][c])] and \
                not [(int(r) + 1, c) for (r, c) in notyet \
                                     if not (int(r) + 1, c) in selected \
                                     if (int(r) + 1 == 16 or \
                                         board[int(r) + 1][c])] and \
                not (len(notyet) + len(already) < 4 and \
                     len(notyet) > 1 and \
                     not [r for (r, c) in notyet \
                            if r != notyet[0][0]])):
                for itm in already:
                    pygame.draw.rect(screen, white, (25 * itm[1], 25 * itm[0], 25, 25))
                    if board[itm[0]][itm[1]]:
                        pygame.draw.rect(screen, board[itm[0]][itm[1]], (5 + 25 * itm[1], 5 + 25 * itm[0], 15, 15))
                    pygame.display.update((25 * itm[1], 25 * itm[0], 25, 25))
                for itm in notyet:
                    pygame.draw.rect(screen, white, (0, 25 * int(itm[0]) + 20, 250, 10))
                    pygame.display.update((0, 25 * int(itm[0]) + 20, 250, 10))
                beep.play()
                selected = []
                
        if spacePressed:
            spacePressed = spacePressed - 1

        if ticks:
            ticks = ticks - 1
        else:
            ticks = moveDelay
            old, piece = piece, [(r + path[0][0], c + path[0][0], col) for (r, c, col) in piece]
            for (r, c, col) in old:
                pygame.draw.rect(screen, black, (25 * c, 25 * r, 25, 25))
                if board[r][c]:
                    pygame.draw.rect(screen, board[r][c], (5 + 25 * c, 5 + 25 * r, 15, 15))
                pygame.display.update((25 * c, 25 * r, 25, 25))
            path = path[1:]
            if not [1 for (r, c, col) in piece if r >= 0]:
                numPieces = numPieces + 1
                if moveDelay > 4 and numPieces % 2 == 0:
                    moveDelay = moveDelay - 1
                if colorRange < len(colors) and numPieces % 6 == 0:
                    colorRange = colorRange + 1
                if mousePressed:
                    selected = []
                    break
                if len(selected) == 1 and selected[0][0] != int(selected[0][0]):
                    r, c = selected[0]
                    locs = [(ro + int(r) - 3, co) for ro in range(4) for co in range(10) if co != c]
                    newBoard = {}
                    for i in range(-4, int(r) - 3):
                        newBoard[i] = board[i + 4]
                    for i in range(int(r) - 3, int(r) + 1):
                        newBoard[i] = [None] * 10
                    for i in range(int(r) + 1, 16):
                        newBoard[i] = board[i]
                        
                    colorBoard(newBoard, locs, colors[:colorRange])
                    board = newBoard
                    col = random.choice(colors[:colorRange])
                    piece = [(ro, c, col) for ro in range(int(r) - 3, int(r) + 1)]
                    path = generatePath(board, piece)
                    if path == -1 or board[-1] != [None] * 10:
                        break
                elif len(selected) == 2 and len([1 for (r, c) in selected if int(r) == r]) == 1:
                    c = selected[0][1]
                    r0 = selected[0][0]
                    r1 = selected[1][0]
                    if int(r0) == r0:
                        r0, r1 = r1, r0
                    if r1 < r0:
                        r1 = r1 - 3
                    newBoard = {}
                    for i in range(-4, int(r0) - 2):
                        newBoard[i] = board[i + 3]
                    for i in range(int(r0) - 2, int(r0) + 1):
                        newBoard[i] = [None] * 10
                    for i in range(int(r0) + 1, 16):
                        newBoard[i] = board[i]
                    
                    locs = [(ro + int(r0) - 2, co) for ro in range(3) for co in range(10) if co != c]
                    
                    colorBoard(newBoard, locs, colors[:colorRange])
                    board = newBoard
                    col = board[r1][c]
                    board[r1][c] = None
                    piece = [(r1, c, col)] + [(ro, c, col) for ro in range(int(r) - 2, int(r) + 1)]
                    path = generatePath(board, piece)
                    if path == -1 or board[-1] != [None] * 10:
                        break
                elif len(selected) == 2 and len([1 for (r, c) in selected if int(r) == r]) == 0:
                    r = selected[0][0]
                    c0 = selected[0][1]
                    c1 = selected[1][1]
                    
                    newBoards = [{}, {}, {}]
                    
                    for i in range(-4, int(r) - 1):
                        newBoards[0][i] = board[i + 2]
                    for i in range(int(r) - 1, int(r) + 1):
                        newBoards[0][i] = [None] * 10
                    for i in range(int(r) + 1, 16):
                        newBoards[0][i] = board[i]
                    locs = [(ro + int(r) - 1, co) for ro in range(2) for co in range(10) if co != c0 and co != c1]
                    colorBoard(newBoards[0], locs, colors[:colorRange])
                    
                    for i in range(-4, int(r) - 2):
                        newBoards[1][i] = board[i + 3]
                    for i in range(int(r) - 2, int(r) + 1):
                        newBoards[1][i] = [None] * 10
                    for i in range(int(r) + 1, 16):
                        newBoards[1][i] = board[i]
                    locs = [(ro + int(r) - 2, co) for ro in range(3) for co in range(10) if co != c0 and not (ro == r and co == c1)]
                    colorBoard(newBoards[1], locs, colors[:colorRange])

                    for i in range(-4, int(r) - 2):
                        newBoards[2][i] = board[i + 3]
                    for i in range(int(r) - 2, int(r) + 1):
                        newBoards[2][i] = [None] * 10
                    for i in range(int(r) + 1, 16):
                        newBoards[2][i] = board[i]
                    locs = [(ro + int(r) - 2, co) for ro in range(3) for co in range(10) if co != c1 and not (ro == r and co == c0)]
                    colorBoard(newBoards[2], locs, colors[:colorRange])
                    

                #
                #
                #
                #
                #
                #
                #
                #
                #
                #
                #
                #
                #
                #
                #
                #
                #
                #
                #
                #
                #

                    
                
        tmp = []
        for loc in selected:
            if loc != None:
                r, c = loc
                if r == int(r):
                    pygame.draw.rect(screen, blockSelectionColor, (25 * c, 25 * r, 25, 25))
                    if board[r][c]:
                        pygame.draw.rect(screen, board[r][c], (5 + 25 * c, 5 + 25 * r, 15, 15))
                    pygame.display.update((25 * c, 25 * r, 25, 25))
                else:
                    tmp.append(loc)
        for loc in tmp:
            r, c = loc
            pygame.draw.rect(screen, lineSelectionColor, (0, 25 * int(r) + 22, 250, 6))
        for loc in tmp:
            r, c = loc
            pygame.draw.rect(screen, spaceSelectionColor, (25 * c, 25 * int(r) + 20, 25, 10))
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
                        pygame.draw.rect(screen, white, (25 * itm[1], 25 * itm[0], 25, 25))
                        if board[itm[0]][itm[1]]:
                            pygame.draw.rect(screen, board[itm[0]][itm[1]], (5 + 25 * itm[1], 5 + 25 * itm[0], 15, 15))
                        pygame.display.update((25 * itm[1], 25 * itm[0], 25, 25))
                    for itm in notyet:
                        pygame.draw.rect(screen, white, (0, 25 * int(itm[0]) + 20, 250, 10))
                        pygame.display.update((0, 25 * int(itm[0]) + 20, 250, 10))
                    selected = []
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
