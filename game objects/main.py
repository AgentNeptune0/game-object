import pygame 

pygame.init()

HEIGHT = 600
WIDTH = 800
playerx = 350
playery = 250

screen = pygame.display.set_mode((WIDTH,HEIGHT))

class Cowboy(pygame.sprite.Sprite):
    def __init__(self):
        #initating parent class constructor function
        super().__init__()
        self.image = pygame.image.load("Cowboy_Left.png")
        #self.rect is a hitbox(boundary)
        self.rect = self.image.get_rect(topleft = (playerx,playery))






while True:
    screen.fill("brown")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)

    pygame.display.update()

pygame.quit()
