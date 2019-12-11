#Ian Murray
#City Simulator
import pygame

def write(msg):
    font = pygame.font.SysFont("None", 45)
    text = font.render(msg, True, (0, 0, 0))
    text = text.convert_alpha
    return text

class PygView(object):

    def __init__(self, width, height):
        
        """Initialize pygame, window, background, font,...
        """
        x = 100
        y = 100
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")
        self.width = width
        self.height = height
        #self.height = width // 4
        
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.clock = pygame.time.Clock()
        self.playtime = 0.0
        self.font = pygame.font.SysFont('mono', 20, bold=True)
        #create game board
        pygame.draw.rect(self.background, (0, 200, 100), (x, y, 300, 300))
        write("hello")


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
            write("hello")
            self.screen.blit(self.background, (0, 0))

        pygame.quit()


####

if __name__ == '__main__':

    # call with width of window and fps
    PygView(500, 500).run()
class CityElement():
    def __init__(self, name, description, cost, length, width, stats_changed):
        self.name = name
        self.description = description
        self.cost = cost
        self.length
        self.width
        self.stats_changed = stats_changed

elements = [
    CityElement("housing","Moderately priced living places on the outskirts of town", 50, 10, 10, "population+")

]





