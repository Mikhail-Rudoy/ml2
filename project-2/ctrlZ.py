import pygame

pygame.init()

screen = pygame.display.set_mode((250, 400))

for x in range(10):
    for y in range(16):
        pygame.draw.rect(screen, pygame.Color(255, 255, 200, 255), ((5 + 25 * x, 5 + 25 * y), (15, 15)))

pygame.display.update()

pygame.draw.rect(screen, pygame.Color(0, 0, 255, 255), ((25, 25), (25, 25)))
pygame.draw.rect(screen, pygame.Color(255, 255, 200, 255), ((30, 30), (15, 15)))

pygame.draw.rect(screen, pygame.Color(0, 0, 255, 255), ((25, 50), (25, 25)))
pygame.draw.rect(screen, pygame.Color(255, 255, 200, 255), ((30, 55), (15, 15)))

pygame.draw.rect(screen, pygame.Color(0, 0, 255, 255), ((50, 50), (25, 25)))
pygame.draw.rect(screen, pygame.Color(255, 255, 200, 255), ((55, 55), (15, 15)))

pygame.draw.rect(screen, pygame.Color(0, 0, 255, 255), ((75, 50), (25, 25)))
pygame.draw.rect(screen, pygame.Color(255, 255, 200, 255), ((80, 55), (15, 15)))

pygame.display.update()
