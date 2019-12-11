import pygame

pygame.init()
# Set size of pygame window.
screen = pygame.display.set_mode((700,700))
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

# colors 
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
brown = (189, 143, 15)
cyan = (87, 87, 176)
dark_green = (38, 169, 34)

def start_screen():
    screen.blit(background, (0, 0))
    font = pygame.font.SysFont("Helvetica", 50)
    title = font.render('City Simulator', True, white)
    start_text = font.render('Start', True, (0, 255, 125))
    instructions_text = font.render('Instructions', True, (200, 125, 0))
    screen.blit(title, (200, 150))
    screen.blit(start_text, (100, 375))
    screen.blit(instructions_text, (400, 375))

def inst_screen():
    screen.fill((0, 0, 0))
    title_font = pygame.font.SysFont("Helvetica", 50)
    insts_font = pygame.font.SysFont('Helvetica', 20)
    i_title = title_font.render('Instructions', True, (0, 0, 255))
    i_insts = insts_font.render('1.  Click and drag city elements onto the green board.', True, red)
    i_insts2 = insts_font.render('2.  Each round, You can buy elements until you run out of money.', True, red)
    i_insts3 = insts_font.render('3.  An element will increase or decrease one or more stats when placed.', True, red)
    screen.blit(i_title, (200, 150))
    screen.blit(i_insts, (0, 250))
    screen.blit(i_insts2, (0, 350))
    screen.blit(i_insts3, (0, 450))

def game_screen():
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 200, 100), (0, 0, 500, 500))
    screen.blit(text,(0, 0))
    # start sprite work
    all_sprites_list.update()
    #screen.fill(black)
    all_sprites_list.draw(screen)
class Stats():
    #population is int, happiness is a percentage, pollution a 1-10 rating, 1 being good and 10 bad, energy produced per round
    def __init__(self, population, happiness, pollution, energy):
        self.population = population
        self.happiness = happiness
        self.pollution = pollution
        self.energy = energy   
#stats include, population, happiness, energy produced, pollution, cash, round #
#each city element increases and/or decreases a stat when placed
class CityElement():
    def __init__(self, name, description, cost, length, width, el_stats):
        self.name = name
        self.description = description
        self.cost = cost
        self.length = length
        self.width = width
        self.el_stats = el_stats
        
class City():    
    def __init__(self, city_stats, player, els_bought_this_round, total_els_bought):
        self.city_stats = city_stats
        self.player = player
        self.els_bought_this_round = els_bought_this_round
        self.total_els_bought = total_els_bought
        
    def buy_element(self, player, el_name, el_cost): 
        #purchases an element if said element is in the list and if player has enough cash
        for element in tier1_elements:
            if el_name == element.name:
                if player.cash >= el_cost:
                    self.els_bought_this_round.append(element)
                    self.total_els_bought.append(element)
                    player.cash -= el_cost
                    
            
                #else display "you dont have enough cash"

    def update_stats(self):
        #changes the city's stats depending on which element is bought 
        for element in self.els_bought_this_round:
            self.city_stats.population += element.el_stats.population
            self.city_stats.happiness += element.el_stats.happiness
            self.city_stats.pollution += element.el_stats.pollution
            self.city_stats.energy += element.el_stats.energy
        #prints updated stats
        print('%d,%d,%d,%d\n' % (self.city_stats.population, self.city_stats.happiness, self.city_stats.pollution, self.city_stats.energy))

    def next_round(self):
        next_round = input("Advance to the next round? y/n ")
        print("Round: " + str(self.player.round_no))
        while True:
            
            if next_round == "y":
                self.player.round_no += 1
                self.next_round()
                return True
            elif next_round == "n":
                self.els_bought_this_round = []
                return True
            else:
                print("Please enter 'y' or 'n'")
                self.user_purchase()
                
        #handles switching rounds
    
    def user_purchase(self):
        buyable_els = ''
        for element in tier1_elements:
            buyable_els += element.name + ", "
        while self.next_round() == True:
            print("Elements for purchase: " + buyable_els)
            buy_el = input("Purchase an element?:")
            self.buy_element(self.player, buy_el, element.cost)
            self.update_stats()
            
class Player():
    # holds player name, current amount of cash, and current round
    def __init__(self, name, cash, round_no):
        self.name = name
        self.cash = cash
        self.round_no = round_no    
    #can buy an element with param name and cost if there is enough cash

class Housing(pygame.sprite.Sprite):
    def __init__(self, width, height):
        #Call the parent sprite class
        super().__init__() # initializes with sprite class
        self.image = pygame.Surface([width, height]) #creates background to blit sprite onto
        #136-137 make bg transparent
        self.image.fill(white) 
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        #138-142 draw house
        pygame.draw.rect(self.image, brown, [0, 25, width, height-25])
        pygame.draw.polygon(self.image, cyan, [(0, 25), (50, 25), (25, 0)])
    
    #checks if sprite is clicked on
    #def check_click(self, mouse_pos):
        #if self.rect.collidepoint(mouse_pos):
            

class Park(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super.__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(white)
        self.image.set_colorkey(white)
        #pygame.draw.rect(self.image, dark_green,  )
#add sprite to list and set its position
housing1 = Housing(50, 75)
all_sprites_list = pygame.sprite.Group()
housing1.rect.x = 100
housing1.rect.y = 550
all_sprites_list.add(housing1)

tier1_elements = [
    # elements that are offered at the start of the game and/or elements that offered when another tier1 is placed
    # some of these can be upgraded to tier2 elements, ex: coal plant > hydroelectric dam
    #
    CityElement("Housing", "Moderately priced living places on the outskirts of town", 50, 110, 80, Stats(100, 0, 0, 0)),
    CityElement("Park", "A place in the city for families to play and relax", 30, 80, 70, Stats(0, 3, 0, 0)),
    CityElement("Restaurant", "food place", 80, 50, 30, Stats(25, 4, 0, 0)),
    CityElement("Coal plant", "burn coal for energy to run shit", 110, 80, 70, Stats(0, -3, 3, 50)),
    CityElement("road", "makes cars able to go", 10, 50, 10, Stats(10, 0, 0, 0))
]

# start of main loop
mainloop = True
game_started = False


while mainloop:
    #sets the text font and renders the text
    pos = pygame.mouse.get_pos()
    font = pygame.font.SysFont("None", 36)
    text = font.render(str(pos), True, (255, 255, 255))
    
        
    print(game_started)
    if game_started == False:
        start_screen()
        start_rect = pygame.draw.rect(screen, (0, 255, 125), (90, 365, 125, 75), 3)
        instructions_rect = pygame.draw.rect(screen, (200, 125, 0), (390, 365, 275, 75), 3)  
    for event in pygame.event.get():

        # User presses QUIT-button.
        if event.type == pygame.QUIT:
            mainloop = False 
        elif event.type == pygame.KEYDOWN:
            # User presses ESCAPE-Key
            if event.key == pygame.K_ESCAPE:
                mainloop = False
        #
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if start_rect.collidepoint(pos):
                # if user left-clicks within the start game box, clear screen and display game board.
                    #draws game board
                    game_started = True
                    game_screen()
                if instructions_rect.collidepoint(pos):
                    game_started = True
                    inst_screen()
                if housing1.rect.collidepoint(pos):
                    bought_housing = Housing(50, 75)
                    all_sprites_list.add(bought_housing)
                    all_sprites_list.update()
                    all_sprites_list.draw(screen)
                    bought_housing.rect.x = pos[0]
                    bought_housing.rect.y = pos[1]


                
    #Update Pygame display.
    pygame.display.flip()
# Finish Pygame.  
pygame.quit()
#test to see if city attributes can be accessed

#test if buy element works correctly

test_city = City(Stats(1000, 50, 5, 100), Player('ian', 500, 1), [], [])
"""
print(test_city.total_els_bought)
test_city.buy_element(test_city.player, tier1_elements[0].name, tier1_elements[0].cost)
print(test_city.player.cash)
print(test_city.total_els_bought[0].name)
"""
#test if update_stats works
#print('%d,%d,%d,%d\n' % (test_city.city_stats.population, test_city.city_stats.happiness, test_city.city_stats.pollution, test_city.city_stats.energy))
#test_city.update_stats()
#print('%d,%d,%d,%d\n' % (test_city.city_stats.population, test_city.city_stats.happiness, test_city.city_stats.pollution, test_city.city_stats.energy))

#final test 1
#prints player name, cash, round_no,
#print('%s,%d,%d\n' % (test_city.player.name, test_city.player.cash, test_city.player.round_no))
#prints initial city stats
#print('%d,%d,%d,%d\n' % (test_city.city_stats.population, test_city.city_stats.happiness, test_city.city_stats.pollution, test_city.city_stats.energy))
#test_city.user_purchase()
           
