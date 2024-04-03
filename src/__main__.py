from neat.genome import Genome
from neat.geneh import GeneHistory
import pygame

gh = GeneHistory(5,4)

inputs = [0.1, 0.2, 0.3, 0.4, 0.5]
target=[0.153,0.76,0.124,0.28]

g = Genome(gh)
for i in range(50):
    g.mutate()

print(f"INPUTS:",inputs)
pred=g.feed_forward(inputs)
print(f"OUTPUTS:",pred)
print(f"TARGET:",target)
mse=g.mean_squared_error(target,pred)
print("Mean squared error:", mse)
print(g)

screen = pygame.display.set_mode((600, 600))
running = True
while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                g.backpropogate(inputs, target)
            if event.key == pygame.K_a:
                g.add_node()
            if event.key == pygame.K_p:
                print(g)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        running = False

    # W Show
    screen.fill((255, 255, 255))
    g.show(screen)
    pygame.display.update()

pygame.quit()
