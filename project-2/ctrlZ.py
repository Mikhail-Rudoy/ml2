import pygame, sys

pygame.init()
screen = pygame.display.set_mode((250, 500))
clock = pygame.time.Clock()

pygame.display.set_caption("Ctrl-Z")

paused = 0
pauseText = pygame.font.Font(None, 35).render("Press \"p\" to unpause", True, (255, 255, 255))

screen.fill((255, 255, 255))
screen.blit(pygame.image.load("title.gif").convert(), (0, 120))
screen.blit(pygame.font.Font(None, 40).render("By Mikhail Rudoy", True, (0, 0, 0)), (7, 240))
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

while True:
    if paused:
        if paused == 1:
            screen.fill((0, 0, 0))
            screen.blit(pauseText, (1, 200))
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
                elif event.key == pygame.K_m:
                    pass
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        del event
        pygame.display.update()
        clock.tick(40)
