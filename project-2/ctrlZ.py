import pygame, sys

pygame.init()
screen = pygame.display.set_mode((250, 500))
clock = pygame.time.Clock()

pygame.display.set_caption("Ctrl-Z")

paused = 1
pauseText = pygame.font.Font(None, 35).render("Press \"p\" to unpause.", True, (255, 255, 255))


while True:
    if paused:
        if paused == 1:
            screen.fill((0, 0, 0))
            screen.blit(pauseText, (0, 200))
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
                if event.key == pygame.K_ESC:
                    pygame.quit()
                    sys.exit()
        del event
        clock.tick(10)
    else:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(40)
