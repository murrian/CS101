import pygame
pygame.init()
# Set size of pygame window.
screen=pygame.display.set_mode((700,700))
# Create empty pygame surface.
background = pygame.Surface(screen.get_size())
# Fill the background white color.
background.fill((0, 0, 0))
# Convert Surface object to make blitting faster.
background = background.convert()
# Copy background to screen (position (0, 0) is upper left corner).
screen.blit(background, (0,0))
# Create Pygame clock object.  
clock = pygame.time.Clock()

mainloop = True
while mainloop:
    #sets the text font and renders the text
    pos = pygame.mouse.get_pos()
    font = pygame.font.SysFont("None", 36)
    text = font.render(str(pos), True, (255, 255, 255))
    
    for event in pygame.event.get():
        # User presses QUIT-button.
        if event.type == pygame.QUIT:
            mainloop = False 
        elif event.type == pygame.KEYDOWN:
            # User presses ESCAPE-Key
            if event.key == pygame.K_ESCAPE:
                mainloop = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                screen.blit(background,(0,0))
                pygame.draw.rect(background, (0, 200, 100), (100, 100, 500, 500))
                screen.blit(text,(0,0))
                position_color = (0, 0, 0)
    #Update Pygame display.
    pygame.display.flip()
# Finish Pygame.  
pygame.quit()

#stats include, population, happiness, energy produced, pollution, cash, round #
#each city element increases and/or decreases a stat when placed
class CityElement():
    def __init__(self, name, description, cost, length, width, stats_changed):
        self.name = name
        self.description = description
        self.cost = cost
        self.length = length
        self.width = width
        self.stats_changed = stats_changed
        
    
    #can buy an element with param name and cost if there is enough cash
    

tier1_elements = [
    # elements that are offered at the start of the game and/or elements that offered when another tier1 is placed
    # some of these can be upgraded to tier2 elements, ex: coal plant > hydroelectric dam
    CityElement("Housing", "Moderately priced living places on the outskirts of town", 50, 110, 80, "population+"),
    CityElement("Park", "A place in the city for families to play and relax", 30, 80, 70, "happiness+"),
    CityElement("Restaurant", "food place", 80, 50, 30, "happiness+"),
    CityElement("Coal plant", "burn coal for energy to run shit", 110, 80, 70, "energy produced+, pollution--" ),
    CityElement("road", "makes cars able to go", 10, 50, 10, "population+")
]



class City():
    #population is int, happiness is a percentage, pollution a 1-10 rating, 1 being good and 10 bad, energy produced per round
    def __init__(self, population, happiness, pollution, energy, player, els_bought):
        self.population = population
        self.happiness = happiness
        self.pollution = pollution
        self.energy = energy
        self.player = player
        self.els_bought = els_bought

    def buy_element(self, player, el_name, el_cost): 
        #purchases an element if said element is in the list and if player has enough cash
        for element in tier1_elements:
            if el_name == element.name:
                if player.cash >= el_cost:
                    self.els_bought.append(element)
                    player.cash -= el_cost
                #else display "you dont have enough cash"
        
    def update_stats():

class Player():
    # holds player name, current amount of cash, and current round
    def __init__(self, name, cash, round_no):
        self.name = name
        self.cash = cash
        self.round_no = round_no

#test to see if city attributes can be accessed
el_names = ""
for el in tier1_elements:
    el_names += el.name + ","
print(el_names)

#test if buy element works correctly
test_city = City(1000, 50, 5, 100, Player('ian', 500, 1), [])
print(test_city.els_bought)
test_city.buy_element(test_city.player, tier1_elements[0].name, tier1_elements[0].cost)
print(test_city.player.cash)
print(test_city.els_bought)









                
