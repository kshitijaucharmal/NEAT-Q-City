from neat.genome import Genome
from neat.geneh import GeneHistory
import pygame

gh = GeneHistory(5, 4)

g = Genome(gh)
for i in range(100):
    g.mutate()

print(g)

screen = pygame.display.set_mode((600, 600))
running = True
while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        running = False

    # W Show
    screen.fill((255, 255, 255))
    g.show(screen)
    pygame.display.update()

pygame.quit()
