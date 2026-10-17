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

#Creating game objects
player = Cowboy()

#Whenver working with any number of sprites, we need to create a group
players = pygame.sprite.Group()
#Adding members to the group
players.add(player)




while True:
    screen.fill("brown")

    #Displaying all the members of the "players" group
    players.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if player.rect.left > 0:
                    player.rect.x -= 20
            if event.key == pygame.K_RIGHT:
                if player.rect.right < 800:
                    player.rect.x += 20
            if event.key == pygame.K_UP:
                if player.rect.top > 0:
                    player.rect.y -= 20
            if event.key == pygame.K_DOWN:
                if player.rect.bottom < 600:
                    player.rect.y += 20

                    

    pygame.display.update()

pygame.quit()
