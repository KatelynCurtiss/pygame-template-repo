import pygame
import sys
import config


pygame.init()
screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
pygame.display.set_caption(config.TITLE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(config.HOT_PINK) 


def init_game():
    return pygame.display.set_mode((800,600))

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False 
        return True 


def draw_rectangle(screen, rect, color, thickness):

    pygame.draw.rect(screen, color, rect, thickness)


my_rect1 = [100, 100, 200, 150]
thickness1 = 8 

draw_rectangle(screen, my_rect1, config.GREEN, thickness1)


def draw_circle(screen, center, radius, color, thickness):
    
    pygame.draw.circle(screen, color, center, radius, thickness)

circle_center = (300, 200)  
circle_radius = 50           
circle_color = config.GREEN   
circle_thickness = 0         

draw_circle(screen, circle_center, circle_radius, circle_color, circle_thickness)

def draw_line(surface, color, start_pos, end_pos, thickness):
    

    pygame.draw.line(surface, color, start_pos, end_pos, thickness)

def main():
    screen = init_game()
    clock = pygame.time.Clock()  

    running = True
    while running:
        running = handle_events()
        screen.fill(config.WHITE)  

        
        draw_line(screen, config.BLUE, [100, 100], [700, 500], 5)  

       
        draw_line(screen, config.RED, [75, 250], [500, 300], 2)  

        pygame.display.flip()

        clock.tick(config.FPS) 

    pygame.quit()
    sys.exit()


