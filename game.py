import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
number = 0
circles = []
selectedCircle = None
selectingRangeSize = 30

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

class Circle:

    def __init__(self, title, color, pos):

        #self.number = number
        self.color = "white"
        self.size = 40

        #number += 1

        self.title = title
        self.color = color

        self.x = pos[0]
        self.y = pos[1]
        
        self.parents = []
        self.children = []

    def addParent(self, cparent):
        self.parents.append(cparent)

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

def AveragePos(pos):
    x, y = pos
    z, h = 0

    matrix = []

    for i in range(selectingRangeSize):
        z = x-(selectingRangeSize/2) + i
        for j in range(selectingRangeSize):
            h = j-(selectingRangeSize/2) + i
            matrix.append(z)


        
            




    


def drawcircle():
    pygame.draw.circle(screen, "white", pygame.mouse.get_pos(), 40)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)

    for c in circles:
        c.draw()

     

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    if (True, False, False) == pygame.mouse.get_pressed():
        for c in circles:

            averagePos = pygame.mouse.get_pos()

            if pygame.mouse.get_pos() == c
            
            c1 = Circle("one","white",pygame.mouse.get_pos())
            circles.append(c1)


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000




        


pygame.quit()