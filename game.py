import sys
import pygame

class Game: 
    def __init__(self):
        pygame.init() #initialise pygame

        pygame.display.set_caption('ninja game') 
        self.screen = pygame.display.set_mode((640, 480)) #create the window, self works like attribute

        self.clock = pygame.time.Clock() #fix fps

        self.img = pygame.image.load('data/images/clouds/cloud1.png') #use png
        self.img.set_colorkey((0, 0, 0)) #set colour key and make transparent

        self.img_pos = [160, 260]
        self.movement = [False, False]

    def run(self):
        while True:
            self.screen.fill((14, 219, 248))

            self.img_pos[1] += self.movement[1] - self.movement[0] * 5
            self.screen.blit(self.img, self.img_pos) #top left is (0,0) screen is surface

            for event in pygame.event.get(): #handle input: touch, mouse click, resize, etc
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False

            pygame.display.update()
            self.clock.tick(60)

Game().run()