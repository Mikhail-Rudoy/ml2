import pygame, sys, random, heapq, math

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
        if not random.choice([2, 1, 0]):
            brd[r][c] = random.choice(clrs)
        else:
            neighbors = [brd[r + ro][c + co] for (ro, co) in [(-1, 0), (1, 0), (0, 1), (0, -1)] \
                                            if r + ro < 16 and r + ro > -5 \
                                            if c + co < 10 and c + co >= 0 \
                                            if brd[r + ro][c + co]]
            if len(neighbors):
                brd[r][c] = random.choice(neighbors)
            else:
                brd[r][c] = random.choice(clrs)

shapes = [None] * 7
displacement = [None] * 7
startData = [None] * 7

# 
#  / \ / \
#  | | | |
#  \_/ \_/
#     #
#  / \ / \
#  | | | |
#  \_/ \_/
#
shapes[0] = [set([(0, 0), (0, 1), (1, 0), (1, 1)])]
displacement[0] = [(0, 0)]
startData[0] = (-2, 4, 0)

# 
#  / \ / \ / \ / \
#  | | | | | | | |
#  \_/ \_/ \_/ \_/
#         #
# 

# 
#  / \
#  | |
#  \_/
# 
#  / \
#  | |
#  \_/
# #
#  / \
#  | |
#  \_/
# 
#  / \
#  | |
#  \_/
#

# 
#         #
#  / \ / \ / \ / \
#  | | | | | | | |
#  \_/ \_/ \_/ \_/
# 

# 
#  / \
#  | |
#  \_/
# 
#  / \
#  | |
#  \_/
#     #
#  / \
#  | |
#  \_/
# 
#  / \
#  | |
#  \_/
#

shapes[1] = [set([(0, 0), (0, 1), (0, 2), (0, 3)]), \
                 set([(0, 0), (1, 0), (2, 0), (3, 0)]), \
                 set([(0, 0), (0, 1), (0, 2), (0, 3)]), \
                 set([(0, 0), (1, 0), (2, 0), (3, 0)])]
displacement[1] = [(0, 0), (-1, 2), (1, 0), (-1, 1)]
startData[1] = (-1, 3, 0)

#
#  / \ / \ / \
#  | | |#| | |
#  \_/ \_/ \_/
# 
#      / \
#      | |
#      \_/
# 

# 
#      / \
#      | |
#      \_/
# 
#  / \ / \
#  | | |#|
#  \_/ \_/
#     
#      / \
#      | |
#      \_/
# 

# 
#      / \
#      | |
#      \_/
# 
#  / \ / \ / \
#  | | |#| | |
#  \_/ \_/ \_/
# 

# 
#  / \
#  | |
#  \_/
# 
#  / \ / \
#  |#| | |
#  \_/ \_/
#     
#  / \
#  | |
#  \_/
# 

shapes[2] = [set([(0, 0), (0, 1), (0, 2), (1, 1)]), \
                 set([(0, 1), (1, 0), (1, 1), (2, 1)]), \
                 set([(0, 1), (1, 0), (1, 1), (1, 2)]), \
                 set([(0, 0), (1, 0), (1, 1), (2, 0)])]
displacement[2] = [(0, 0), (-1, 0), (-1,  0), (-1, 1)]
startData[2] = (-2, 3, 2)

#
#  / \ / \ / \
#  | | |#| | |
#  \_/ \_/ \_/
# 
#  / \
#  | |
#  \_/
# 

# 
#  / \ / \
#  | | | |
#  \_/ \_/
# 
#      / \
#      |#|
#      \_/
#     
#      / \
#      | |
#      \_/
# 

# 
#          / \
#          | |
#          \_/
# 
#  / \ / \ / \
#  | | |#| | |
#  \_/ \_/ \_/
# 

# 
#  / \
#  | |
#  \_/
# 
#  / \ 
#  |#| 
#  \_/ 
#     
#  / \ / \
#  | | | |
#  \_/ \_/
# 

shapes[3] = [set([(0, 0), (0, 1), (0, 2), (1, 0)]), \
                 set([(0, 0), (0, 1), (1, 1), (2, 1)]), \
                 set([(0, 2), (1, 0), (1, 1), (1, 2)]), \
                 set([(0, 0), (1, 0), (2, 0), (2, 1)])]
displacement[3] = [(0, 0), (-1, 0), (-1, 0), (-1, 1)]
startData[3] = (-2, 3, 2)

#
#  / \ / \ / \
#  | | |#| | |
#  \_/ \_/ \_/
# 
#          / \
#          | |
#          \_/
# 

# 
#      / \
#      | |
#      \_/
# 
#      / \
#      |#|
#      \_/
# 
#  / \ / \
#  | | | |
#  \_/ \_/
# 

# 
#  / \
#  | |
#  \_/
# 
#  / \ / \ / \
#  | | |#| | |
#  \_/ \_/ \_/
# 

#     
#  / \ / \
#  | | | |
#  \_/ \_/
# 
#  / \ 
#  |#| 
#  \_/ 
# 
#  / \
#  | |
#  \_/
# 

shapes[4] = [set([(0, 0), (0, 1), (0, 2), (1, 2)]), \
                 set([(0, 1), (1, 1), (2, 0), (2, 1)]), \
                 set([(0, 0), (1, 0), (1, 1), (1, 2)]), \
                 set([(0, 0), (0, 1), (1, 0), (2, 0)])]
displacement[4] = [(0, 0), (-1, 0), (-1, 0), (-1, 1)]
startData[4] = (-2, 3, 2)

#
#  / \ / \
#  | | |#|
#  \_/ \_/
# 
#      / \ / \
#      | | | |
#      \_/ \_/
# 

# 
#      / \
#      | |
#      \_/
# 
#  / \ / \
#  | | |#|
#  \_/ \_/
# 
#  / \
#  | |
#  \_/
# 

#
#  / \ / \
#  | | | |
#  \_/ \_/
# 
#      / \ / \
#      |#| | |
#      \_/ \_/
#

# 
#      / \
#      | |
#      \_/
# 
#  / \ / \
#  |#| | |
#  \_/ \_/
# 
#  / \
#  | |
#  \_/
# 

shapes[5] = [set([(0, 0), (0, 1), (1, 1), (1, 2)]), \
                 set([(0, 1), (1, 0), (1, 1), (2, 0)]), \
                 set([(0, 0), (0, 1), (1, 1), (1, 2)]), \
                 set([(0, 1), (1, 0), (1, 1), (2, 0)])]
displacement[5] = [(0, 0), (-1, 0), (-1, 0), (-1, 1)]
startData[5] = (-2, 3, 2)

#
#      / \ / \
#      |#| | |
#      \_/ \_/
# 
#  / \ / \
#  | | | |
#  \_/ \_/
# 

# 
#  / \
#  | |
#  \_/
# 
#  / \ / \
#  | | |#|
#  \_/ \_/
# 
#      / \
#      | |
#      \_/
# 

#
#      / \ / \
#      | | | |
#      \_/ \_/
# 
#  / \ / \
#  | | |#|
#  \_/ \_/
# 

# 
#  / \
#  | |
#  \_/
# 
#  / \ / \
#  |#| | |
#  \_/ \_/
# 
#      / \
#      | |
#      \_/
# 

shapes[6] = [set([(0, 1), (0, 2), (1, 0), (1, 1)]), \
                 set([(0, 0), (1, 0), (1, 1), (2, 1)]), \
                 set([(0, 1), (0, 2), (1, 0), (1, 1)]), \
                 set([(0, 0), (1, 0), (1, 1), (2, 1)])]
displacement[6] = [(0, 0), (-1, 0), (-1, 0), (-1, 1)]
startData[6] = (-2, 3, 2)

def generatePath(board, piece):
    global shapes
    minr = piece[0][0]
    minc = piece[0][1]
    col = piece[0][2]
    for (r, c, C) in piece:
        if r < minr:
            minr = r
        if c < minc:
            minc = c
    template = set([(r - minr, c - minc) for (r, c, col) in piece])
    paths = []
    for (t, o) in [(0, 0)] + [(t, o) for t in range(1, 7) for o in range(4)]:
        if shapes[t][o] == template:
            path = getPath(board, minr, minc, t, o, col)
            if path != -1:
                paths.append(path)
    if len(paths) == 0:
        return -1
    else:
        return random.choice(paths)
    
def getPath(board, r, c, t, o, col):
    global shapes
    global displacement
    global startData
    space = []
    for it in range(len(shapes[t])):
        space.append({})
    for oi in range(len(space)):
         for ri in range(-4, 16):
             space[oi][ri] = [None] * 10
    ri, ci, oi = startData[t]
    
    dist = lambda rparam, cparam, oparam, tmpr = r, tmpc = c, tmpo = o: abs(rparam - tmpr) + abs(cparam - tmpc) + 6 - 3 * abs(abs(oparam - tmpo) - 2) + math.copysign(100, rparam - tmpr - 1) + 100 
    isValid = lambda rparam, cparam: rparam >= -4 and rparam < 16 and cparam >= 0 and cparam < 10

    neighbors = []
    heapq.heappush(neighbors, (dist(ri, ci, oi), 1 - ri + random.randrange(5), abs(abs(oi - o) - 2), ri, ci, oi, 4, 0))
    space[oi][ri][ci] = 4
    success = False
    while neighbors:
        priority, greed, turn, ri, ci, oi, numonlevel, sofar = heapq.heappop(neighbors)
        if dist(ri, ci, oi) == 0:
            success = True
            break
        
        if ri < 15 and space[oi][ri + 1][ci] == None:
            go = True
            for (pr, pc) in shapes[t][oi]:
                if not isValid(pr + ri + 1, pc + ci):
                    go = False
                elif board[pr + ri + 1][pc + ci]:
                    space[oi][ri + 1][ci] = -1
                    go = False
            if go:
                space[oi][ri + 1][ci] = 0
                heapq.heappush(neighbors, (sofar + 1 + dist(ri + 1, ci, oi), 0  - ri + random.randrange(5), abs(abs(oi - o) - 2), ri + 1, ci, oi, 0, sofar + 1))
            
        if numonlevel != 4:
            if ci < 9 and (space[oi][ri][ci + 1] == None or space[oi][ri][ci + 1] >  numonlevel + 1):
                go = True
                for (pr, pc) in shapes[t][oi]:
                    if not isValid(pr + ri, pc + ci + 1):
                        go = False
                    elif board[pr + ri][pc + ci + 1]:
                        space[oi][ri][ci + 1] = -1
                        go = False
                if go:
                    space[oi][ri][ci + 1] = numonlevel + 1
                    heapq.heappush(neighbors, (sofar + 1 + dist(ri, ci + 1, oi), 1 - ri + random.randrange(5), abs(abs(oi - o) - 2), ri, ci + 1, oi, numonlevel + 1, sofar + 1))
            if ci > 0 and (space[oi][ri][ci - 1] == None or space[oi][ri][ci - 1] >  numonlevel + 1):
                go = True
                for (pr, pc) in shapes[t][oi]:
                    if not isValid(pr + ri, pc + ci - 1):
                        go = False
                    elif board[pr + ri][pc + ci - 1]:
                        space[oi][ri][ci - 1] = -1
                        go = False
                if go:
                    space[oi][ri][ci - 1] = numonlevel + 1
                    heapq.heappush(neighbors, (sofar + 1 + dist(ri, ci - 1, oi), 1 - ri + random.randrange(5), abs(abs(oi - o) - 2), ri, ci - 1, oi, numonlevel + 1, sofar + 1))
            if t != 0:
                dr = displacement[t][(oi + 1) % 4][0] - displacement[t][oi][0]
                dc = displacement[t][(oi + 1) % 4][1] - displacement[t][oi][1]
                if isValid(ri + dr, ci + dc) and (space[(oi + 1) % 4][ri + dr][ci + dc] == None or space[(oi + 1) % 4][ri + dr][ci + dc] > numonlevel + 1):
                    go = True
                    for (pr, pc) in shapes[t][(oi + 1) % 4]:
                        if not isValid(pr + ri + dr, pc + ci + dc):
                            go = False
                        elif board[pr + ri + dr][pc + ci + dc]:
                            space[(oi + 1) % 4][ri + dr][ci + dc] = -1
                            go = False
                    if go:
                        space[(oi + 1) % 4][dr + ri][dc + ci] = numonlevel + 1
                        heapq.heappush(neighbors, (sofar + 3 + dist(ri + dr, ci + dc, (oi + 1) % 4), 1 - ri - dr + random.randrange(5), abs(abs((oi + 1) % 4 - o) - 2), ri + dr, ci + dc, (oi + 1) % 4, numonlevel + 1, sofar + 3))
                dr = displacement[t][(oi - 1) % 4][0] - displacement[t][oi][0]
                dc = displacement[t][(oi - 1) % 4][1] - displacement[t][oi][1]
                if isValid(ri + dr, ci + dc) and (space[(oi - 1) % 4][ri + dr][ci + dc] == None or space[(oi - 1) % 4][ri + dr][ci + dc] > numonlevel + 1):
                    go = True
                    for (pr, pc) in shapes[t][(oi - 1) % 4]:
                        if not isValid(pr + ri + dr, pc + ci + dc):
                            go = False
                        elif board[pr + ri + dr][pc + ci + dc]:
                            space[(oi - 1) % 4][ri + dr][ci + dc] = -1
                            go = False
                    if go:
                        space[(oi - 1) % 4][dr + ri][dc + ci] = numonlevel + 1
                        heapq.heappush(neighbors, (sofar + 3 + dist(ri + dr, ci + dc, (oi - 1) % 4), 1 - ri - dr + random.randrange(5), abs(abs((oi - 1) % 4 - o) - 2), ri + dr, ci + dc, (oi - 1) % 4, numonlevel + 1, sofar + 3))
    
    if not success:
        return -1
    
    path = []
    newLine = True
    while (r, c, o) != startData[t]:
        piece = [(r + dr, c + dc, col) for (dr, dc) in shapes[t][o]]
        numonlevel = space[o][r][c]
        if newLine:
            for i in range(4 - numonlevel):
                path.append(piece)
            newLine = False
        path.append(piece)
        if numonlevel == 0:
            r = r - 1
            newLine = True
            continue
        if c > 0 and space[o][r][c - 1] == numonlevel - 1:
            c = c - 1
            continue
        if c < 9 and space[o][r][c + 1] == numonlevel - 1:
            c = c + 1
            continue
        dr = displacement[t][(o + 1) % 4][0] - displacement[t][o][0]
        dc = displacement[t][(o + 1) % 4][1] - displacement[t][o][1]
        if t > 0 and isValid(r + dr, c + dc) and space[(o + 1) % 4][r + dr][c + dc] == numonlevel - 1:
            o = (o + 1) % 4
            r = r + dr
            c = c + dc
            continue
        dr = displacement[t][(o - 1) % 4][0] - displacement[t][o][0]
        dc = displacement[t][(o - 1) % 4][1] - displacement[t][o][1]
        if t > 0 and isValid(r + dr, c + dc) and space[(o - 1) % 4][r + dr][c + dc] == numonlevel - 1:
            o = (o - 1) % 4
            r = r + dr
            c = c + dc
            continue
    
    path.append([(r + dr, c + dc, col) for (dr, dc) in shapes[t][o]])
    path.append([(r + dr, c + dc, col) for (dr, dc) in shapes[t][o]])
    return path

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
            break
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        break
    else:
        continue
    clock.tick(4)
    del event

while pygame.event.poll().type != pygame.NOEVENT:
    pass

screen.fill(white)
screen.blit(pygame.font.Font(None, 43).render("Click to Continue", True, black), (2, 170))


pygame.display.update()

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
                pygame.mixer.music.fadeout(500)
            else:
                pygame.time.wait(500)
            break
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if music:
            pygame.mixer.music.fadeout(500)
        else:
            pygame.time.wait(500)
        break
    else:
        continue
    clock.tick(4)
    del event


screen.fill(white)
screen.blit(pygame.font.Font(None, 60).render("Game Over", True, black), (10, 70))

pygame.display.update()

for i in range(10):
    while pygame.event.poll().type != pygame.NOEVENT:
        pass
    clock.tick(4)


pygame.mixer.music.load("song.wav")
pygame.mixer.music.play(-1)
if not music:
    pygame.mixer.music.pause()






while 1:

	
	board = {}
	for i in range(-4, 16):
	    board[i] = [None] * 10
	piece = []
	selected = []
	path = [piece]
	numPieces = 0
	moveDelay = 30
	ticks = 30
	colorRange = 2
	colors = [(r, g, b) for r in range(0, 255, 75) \
	                    for g in range(0, 255, 75) \
	                    for b in range(0, 255, 75) \
	                    if r != g and g != b and r != b]
	random.shuffle(colors)
	colors = colors[:10]
	
	avoid = [random.randrange(10) for r in range(8, 16)]
	take = [random.choice([c for c in range(10) if c != avoid[r - 8]]) for r in range(8, 16)]
	
	colorBoard(board, [(r, c) for r in range(8, 16) for c in range(10) if (random.randrange(18) - 8 < r and c != avoid[r - 8]) or c == take[r- 8]], colors[:colorRange])
	
	while 1:
	    t = random.randrange(7)
	    sr, sc, o = startData[t]
	    col = random.choice(colors[:colorRange])
	    for (r2, c2, col2) in selected:
	        board[r2][c2] = col2
	    selected = piece
	    piece = [(sr + dr, sc + dc, col) for (dr, dc) in shapes[t][o]]
	    while not [1 for (r, c, col) in piece if r > 14 or board[r + 1][c] or (r + 1, c) in [(r2, c2) for (r2, c2, col2) in selected]]:
	        piece = [(r + 1, c, col) for (r, c, col) in piece]
	    if [1 for (r, c, col) in piece if r < 0]:
	        break
	for (r, c, col) in selected:
	    board[r][c] = col
	selected = [(r, c) for (r, c, col) in selected]
	path = generatePath(board, piece)
	
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
	        if mousePressed and moveDelay != 30:
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
	        elif selected and moveDelay != 30:
	            already = [itm for itm in selected if itm and itm[0] == int(itm[0])]
	            notyet = [itm for itm in selected if itm and itm[0] != int(itm[0])]
                    fail = False
                    rs = [r for (r, c) in notyet]
                    rs += [r for r in range(-4, 16) if [c for c in range(10) if not (r, c) in already and board[r][c]]]
                    if rs:
                        last = rs[0]
                    for r in sorted(rs):
                        if abs(last - r) <= 1:
                            last = r
                        else:
                            fail = True
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
	                            if r != notyet[0][0]])) or \
	                fail:
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
	            old, piece = piece, path[0]
	            for (r, c, col) in old:
	                if (r, c, col) in piece:
	                    continue
	                pygame.draw.rect(screen, white, (25 * c, 25 * r, 25, 25))
	                if board[r][c]:
	                    pygame.draw.rect(screen, board[r][c], (5 + 25 * c, 5 + 25 * r, 15, 15))
	                pygame.display.update((25 * c, 25 * r, 25, 25))
	            path = path[1:]
	            if not [1 for (r, c, col) in piece if r >= 0]:
	                numPieces = numPieces + 1
	                if moveDelay == 30:
	                    moveDelay = 15
	                if moveDelay > 2 and numPieces % 2 == 0:
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
	                        selected = []
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
	                    piece = [(r1, c, col)] + [(ro, c, col) for ro in range(int(r0) - 2, int(r0) + 1)]
	                    path = generatePath(board, piece)
	                    if path == -1 or board[-1] != [None] * 10:
	                        selected = []
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
	                    locs = [(ro + int(r) - 2, co) for ro in range(3) for co in range(10) if co != c0 and not (ro == 0 and co == c1)]
	                    colorBoard(newBoards[1], locs, colors[:colorRange])
	
	                    for i in range(-4, int(r) - 2):
	                        newBoards[2][i] = board[i + 3]
	                    for i in range(int(r) - 2, int(r) + 1):
	                        newBoards[2][i] = [None] * 10
	                    for i in range(int(r) + 1, 16):
	                        newBoards[2][i] = board[i]
	                    locs = [(ro + int(r) - 2, co) for ro in range(3) for co in range(10) if co != c1 and not (ro == 0 and co == c0)]
	                    colorBoard(newBoards[2], locs, colors[:colorRange])
	                    
	                    col = random.choice(colors[:colorRange])
	                    pieces = [[], [], []]
	                    pieces[0] = [(ro, co, col) for ro in [int(r) - 1, int(r)] for co in [c0, c1]]
	                    pieces[1] = [(int(r) - 2, c1, col)] + [(ro, c0, col) for ro in range(int(r) - 2, int(r) + 1)]
	                    pieces[2] = [(int(r) - 2, c0, col)] + [(ro, c1, col) for ro in range(int(r) - 2, int(r) + 1)]
	                    
	                    paths = [[], [], []]
	                    paths[0] = generatePath(newBoards[0], pieces[0])
	                    paths[1] = generatePath(newBoards[1], pieces[1])
	                    paths[2] = generatePath(newBoards[2], pieces[2])
	                    
	                    if not [i for i in range(3) if paths[i] != -1 and newBoard[i][-1] != [None] * 10]:
	                        selected = []
	                        i = random.randrange(3)
	                        piece = pieces[i]
	                        board = newBoards[i]
	                        break
	                    
	                    i = random.choice([i for i in range(3) if paths[i] != -1])
	                    piece = pieces[i]
	                    board = newBoards[i]
	                    path = paths[i]
	                elif len(selected) == 3 and len([1 for (r, c) in selected if int(r) == r]) == 0:
	                    r = selected[0][0]
	                    c0 = selected[0][1]
	                    c1 = selected[1][1]
	                    c2 = selected[2][1]
	                    
	                    col = random.choice(colors[:colorRange])
	                    pieces = [[], [], []]
	                    pieces[0] = [(int(r), c0, col)] + [(int(r) - 1, co, col) for co in [c0, c1, c2]]
	                    pieces[1] = [(int(r), c1, col)] + [(int(r) - 1, co, col) for co in [c0, c1, c2]]
	                    pieces[2] = [(int(r), c2, col)] + [(int(r) - 1, co, col) for co in [c0, c1, c2]]
	                    
	                    
	                    newBoards = [{}, {}, {}]
	                    for i in range(-4, int(r) - 1):
	                        newBoards[0][i] = board[i + 2]
	                    for i in range(int(r) - 1, int(r) + 1):
	                        newBoards[0][i] = [None] * 10
	                    for i in range(int(r) + 1, 16):
	                        newBoards[0][i] = board[i]
	                    locs = [(ro + int(r) - 1, co) for ro in range(2) for co in range(10) if not (ro + int(r) - 1, co, col) in pieces[0]]
	                    colorBoard(newBoards[0], locs, colors[:colorRange])
	
	                    for i in range(-4, int(r) - 1):
	                        newBoards[1][i] = board[i + 2]
	                    for i in range(int(r) - 1, int(r) + 1):
	                        newBoards[1][i] = [None] * 10
	                    for i in range(int(r) + 1, 16):
	                        newBoards[1][i] = board[i]
	                    locs = [(ro + int(r) - 1, co) for ro in range(2) for co in range(10) if not (ro + int(r) - 1, co, col) in pieces[1]]
	                    colorBoard(newBoards[1], locs, colors[:colorRange])
	
	                    for i in range(-4, int(r) - 1):
	                        newBoards[2][i] = board[i + 2]
	                    for i in range(int(r) - 1, int(r) + 1):
	                        newBoards[2][i] = [None] * 10
	                    for i in range(int(r) + 1, 16):
	                        newBoards[2][i] = board[i]
	                    locs = [(ro + int(r) - 1, co) for ro in range(2) for co in range(10) if not (ro + int(r) - 1, co, col) in pieces[2]]
	                    colorBoard(newBoards[2], locs, colors[:colorRange])
	                    
	                    
	                    paths = [[], [], []]
	                    paths[0] = generatePath(newBoards[0], pieces[0])
	                    paths[1] = generatePath(newBoards[1], pieces[1])
	                    paths[2] = generatePath(newBoards[2], pieces[2])
	
	                    if not [i for i in range(3) if paths[i] != -1 and newBoards[i][-1] == [None] * 10]:
	                        selected = []
	                        i = random.randrange(3)
	                        piece = pieces[i]
	                        board = newBoards[i]
	                        break
	                    
	                    i = random.choice([i for i in range(3) if paths[i] != -1 and newBoards[i][-1] == [None] * 10])
	                    piece = pieces[i]
	                    board = newBoards[i]
	                    path = paths[i]
	                elif len(selected) == 3 and len([1 for (r, c) in selected if int(r) == r]) == 1 and len(set([r for (r, c) in selected])) == 2:
	                    [(blockr, blockc)] = [(r, c) for (r, c) in selected if r == int(r)]
	                    [c0, c1] = [c for (r, c) in selected if r != blockr]
	                    r = [r for (r, c) in selected if r != blockr][0]
	                    
	                    if blockr > r:
	                        locs = [(ro + int(r) - 1, co) for ro in range(2) for co in range(10) if co != blockc and (not co in [c0, c1] or ro != 0)]
	                        newBoard = {}
	                        for i in range(-4, int(r) - 1):
	                            newBoard[i] = board[i + 2]
	                        for i in range(int(r) - 1, int(r) + 1):
	                            newBoard[i] = [None] * 10
	                        for i in range(int(r) + 1, 16):
	                            newBoard[i] = board[i]
	                        
	                        colorBoard(newBoard, locs, colors[:colorRange])
	                        board = newBoard
	                        col = board[blockr][blockc]
	                        board[blockr][blockc] = None
	                        piece = [(blockr, blockc, col), (int(r), blockc, col), (int(r) - 1, c0, col), (int(r) - 1, c1, col)]
	                        path = generatePath(board, piece)
	                        if path == -1 or board[-1] != [None] * 10:
	                            selected = []
	                            break
	                    else:
	                        col = board[blockr][blockc]
	                        board[blockr][blockc] = 0
	                        blockr = blockr - 2
	                        pieces = [[(blockr, blockc, col), \
	                                   (blockr + 1, c0, col), \
	                                   (blockr + 1, c1, col), \
	                                   (blockr + 2, c0, col)], \
	                                  [(blockr, blockc, col), \
	                                   (blockr + 1, c0, col), \
	                                   (blockr + 1, c1, col), \
	                                   (blockr + 2, c1, col)]]    
	                        
	                        newBoards = [{}, {}, {}]
	                        for i in range(-4, int(r) - 1):
	                            newBoards[0][i] = board[i + 2]
	                        for i in range(int(r) - 1, int(r) + 1):
	                            newBoards[0][i] = [None] * 10
	                        for i in range(int(r) + 1, 16):
	                            newBoards[0][i] = board[i]
	                        locs = [(ro + int(r) - 1, co) for ro in range(2) for co in range(10) if not (ro + int(r) - 1, co, col) in pieces[0]]
	                        colorBoard(newBoards[0], locs, colors[:colorRange])
	
	                        for i in range(-4, int(r) - 1):
	                            newBoards[1][i] = board[i + 2]
	                        for i in range(int(r) - 1, int(r) + 1):
	                            newBoards[1][i] = [None] * 10
	                        for i in range(int(r) + 1, 16):
	                            newBoards[1][i] = board[i]
	                        locs = [(ro + int(r) - 1, co) for ro in range(2) for co in range(10) if not (ro + int(r) - 1, co, col) in pieces[1]]
	                        colorBoard(newBoards[1], locs, colors[:colorRange])
	                        
	                        paths = [[], []]
	                        paths[0] = generatePath(newBoards[0], pieces[0])
	                        paths[1] = generatePath(newBoards[1], pieces[1])
	                        
	                        if (paths[0] == -1 or newBoards[0][-1] != [None] * 10) and \
	                                (paths[1] == -1 or newBoards[1][-1] != [None] * 10):
	                            selected = []
	                            i = random.randrange(2)
	                            piece = pieces[i]
	                            board = newBoards[i]
	                            break
	                    
	                        i = random.choice([i for i in range(2) if paths[i] != -1 and newBoards[i][-1] == [None] * 10])
	                        piece = pieces[i]
	                        board = newBoards[i]
	                        path = paths[i]
	                elif len(selected) == 3 and len([1 for (r, c) in selected if int(r) == r]) == 1:
	                    selected.sort()
	                    col = board[selected[1][0]][selected[0][1]]
	                    board[selected[1][0]][selected[0][1]] = None
	                    piece = [(selected[1][0] - 3 + r, selected[0][1], col) for r in range(4)]
	                    r = selected[1][0]
	                    c = selected[0][1]
	                    newBoards = [{}, {}]
	                    for i in range(-4, r - 3):
	                        newBoards[0][i] = board[i + 3]
	                        newBoards[1][i] = board[i + 3]
	                    for i in range(r - 3, r + 1):
	                        newBoards[0][i] = [None] * 10
	                        newBoards[1][i] = [None] * 10
	                    for i in range(r + 1, 16):
	                        newBoards[0][i] = board[i]
	                        newBoards[1][i] = board[i]
	                    newBoards[0][r - 1] = board[r]
	                    newBoards[1][r - 2] = board[r]
	
	                    locs = [[(ro, co) for ro in [r - 3, r - 2, r] for co in range(10) if co != c], \
	                            [(ro, co) for ro in [r - 3, r - 1, r] for co in range(10) if co != c]]
	                    colorBoard(newBoards[0], locs[0], colors[:colorRange])
	                    colorBoard(newBoards[1], locs[1], colors[:colorRange])
	                    
	                    paths = [[], []]
	                    paths[0] = generatePath(newBoards[0], piece)
	                    paths[1] = generatePath(newBoards[1], piece)
	                    
	                    if (paths[0] == -1 or newBoards[0][-1] != [None] * 10) and \
	                            (paths[1] == -1 or newBoards[1][-1] != [None] * 10):
	                        selected = []
	                        i = random.randrange(2)
	                        board = newBoards[i]
	                        break
	                    
	                    i = random.choice([i for i in range(2) if paths[i] != -1 and newBoards[i][-1] == [None] * 10])
	                    board = newBoards[i]
	                    path = paths[i]
	                elif len(selected) == 3 and len([1 for (r, c) in selected if int(r) == r]) == 2:
	                    col = [board[r][c] for (r, c) in selected if int(r) == r][0]
	                    for (ro, co) in selected:
	                        if int(ro) == ro:
	                            board[ro][co] = None
	                        else:
	                            r = ro
	                            c = co
	                    piece = [(int(r), c, col), (int(r) - 1, c, col)]
	                    for (ro, co) in selected:
	                        if int(ro) == ro:
	                            if ro > r:
	                                piece.append((ro, co, col))
	                            else:
	                                piece.append((ro - 2, co, col))
	                    newBoard = {}
	                    for i in range(-4, int(r) - 1):
	                        newBoard[i] = board[i + 2]
	                    for i in range(int(r) - 1, int(r) + 1):
	                        newBoard[i] = [None] * 10
	                    for i in range(int(r) + 1, 16):
	                        newBoard[i] = board[i]
	                    locs = [(ro, co) for ro in range(int(r) - 1, int(r) + 1) for co in range(10) if co != c]
	                    colorBoard(newBoard, locs, colors[:colorRange])
	                    board = newBoard
	                    
	                    path = generatePath(board, piece)
	                    if path == -1 or board[-1] != [None] * 10:
	                        selected = []
	                        break
	                elif len(selected) == 4:
	                    for (r, c) in selected:
	                        if int(r) == r:
	                            col = board[r][c]
	                            board[r][c] = None
	                    piece = [(r, c, col) for (r, c) in selected]
	                    piece.sort()
	                    piece.reverse()
	                    changedRows = []
	                    for i in range(4):
	                        if int(piece[i][0]) != piece[i][0]:
	                            changedRows.append(int(piece[i][0]))
	                            tmpr = piece[i][0]
	                            for k in range(i, 4):
	                                if tmpr == piece[k][0]:
	                                    piece[k] = (int(piece[k][0]), piece[k][1], col)
	                                else:
	                                    piece[k] = (piece[k][0] - 1, piece[k][1], col)
	                    newBoard = {}
	                    k = -4 + len(changedRows)
	                    for i in range(-4, 16):
	                        if i in changedRows:
	                            newBoard[i] = [None] * 10
	                        else:
	                            newBoard[i] = board[k]
	                            k = k + 1
	                    colorBoard(newBoard, [(r, c) for r in changedRows for c in range(10) if not (r, c, col) in piece], colors[:colorRange])
	                    board = newBoard
	                    
	                    if board[-1] != [None] * 10:
	                        selected = []
	                        break
	                    path = generatePath(board, piece)
	                    if path == -1:
	                        selected = []
	                        break
	                else:
	                    break
	                selected = []
	                while pygame.event.poll().type != pygame.NOEVENT:
	                    pass
	
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
	for r in range(16):
	    for c in range(10):
	        if board[r][c]:
	            pygame.draw.rect(screen, board[r][c], (5 + 25 * c, 5 + 25 * r, 15, 15))
	pygame.display.update()
	clock.tick(40)
	pygame.time.wait(2000)
	while pygame.event.poll().type != pygame.NOEVENT:
	    pass
	
	screen.fill(white)
	screen.blit(pygame.font.Font(None, 43).render("Click to Continue", True, black), (2, 170))
	
	
	pygame.display.update()
	
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
                    pygame.time.wait(500)
	            break
	    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pygame.time.wait(500)
	        break
	    else:
	        continue
	    clock.tick(4)
	    del event
	
	
	screen.fill(white)
	screen.blit(pygame.font.Font(None, 60).render("Game Over", True, black), (10, 70))
	
	pygame.display.update()

        for i in range(10):
            while pygame.event.poll().type != pygame.NOEVENT:
                pass
            clock.tick(4)
