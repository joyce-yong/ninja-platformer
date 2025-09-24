import sys
import pygame

class Game: 
    def __init__(self):
        pygame.init() #initialise pygame

        pygame.display.set_caption('ninja game') 
        self.screen = pygame.display.set_mode((640, 480)) #create the window, self works like attribute

        self.clock = pygame.time.Clock() #fix fps

    def run(self):
        while True:
            for event in pygame.event.get(): #handle input: touch, mouse click, resize, etc
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.clock.tick(60)

Game().run()