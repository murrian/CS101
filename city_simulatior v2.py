#Ian Murray
#City Simulator
import pygame


class PygView(object):
    
    

    def __init__(self, width=500, height=500):
        
        """Initialize pygame, window, background, font,...
        """
        x = 100
        y = 100
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")
        self.width = width
        self.height = height
        #self.height = width // 4
        window = pygame.display.set_mode((self.width, self.height))
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.clock = pygame.time.Clock()
        self.playtime = 0.0
        self.font = pygame.font.SysFont('mono', 20, bold=True)
        pygame.draw.rect(self.background, (0, 200, 100), (x, y, width, height))


    def run(self):
        """The mainloop
        """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            pygame.display.flip()
            self.screen.blit(self.background, (0, 0))

        pygame.quit()


####

if __name__ == '__main__':

    # call with width of window and fps
    PygView(640, 400).run()
class CityElement():
    def __init__(self, name, description, cost, size, stats_changed):
        self.name = name
        self.description = description
        self.cost = cost
        self.size = size
        self.stats_changed = stats_changed

